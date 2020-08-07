import time
import argparse
import functools
import cv2 as cv
import numpy as np
import tensorflow as tf

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

print("Package Loaded !")

# Function to load an image from a file, and add a batch dimension.
def load_img(path_to_img):
    img = tf.io.read_file(path_to_img)
    img = tf.io.decode_image(img, channels=3)
    img = tf.image.convert_image_dtype(img, tf.float32)
    img = img[tf.newaxis, :]

    return img

# Function to pre-process by resizing an central cropping it.
def preprocess_image(image, target_dim):
    # Resize the image so that the shorter dimension becomes 256px.
    shape = tf.cast(tf.shape(image)[1:-1], tf.float32)
    short_dim = min(shape)
    scale = target_dim / short_dim
    new_shape = tf.cast(shape * scale, tf.int32)
    image = tf.image.resize(image, new_shape)

    # Central crop the image.
    image = tf.image.resize_with_crop_or_pad(image, target_dim, target_dim)

    return image

# Function to run style prediction on preprocessed style image.
def run_style_predict(preprocessed_style_image):
    # Load the model.
    interpreter = tf.lite.Interpreter(model_path=style_predict_path)

    # Set model input.
    interpreter.allocate_tensors()
    input_details = interpreter.get_input_details()
    interpreter.set_tensor(input_details[0]["index"], preprocessed_style_image)

    # Calculate style bottleneck.
    interpreter.invoke()
    style_bottleneck = interpreter.tensor(
        interpreter.get_output_details()[0]["index"]
        )()

    return style_bottleneck

# Run style transform on preprocessed style image
def run_style_transform(style_bottleneck, preprocessed_content_image):
    # Load the model.
    interpreter = tf.lite.Interpreter(model_path=style_transform_path)

    # Set model input.
    input_details = interpreter.get_input_details()
    interpreter.allocate_tensors()

    # Set model inputs.
    interpreter.set_tensor(input_details[0]["index"], preprocessed_content_image)
    interpreter.set_tensor(input_details[1]["index"], style_bottleneck)
    interpreter.invoke()

    # Transform content image.
    stylized_image = interpreter.tensor(
        interpreter.get_output_details()[0]["index"]
        )()

    return stylized_image

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--content_image", type=str, help="Content image", default='content.jpg')
    parser.add_argument("--style_image", type=str, help="Style image", default='style.jpg')

    args = parser.parse_args()

    dict_args = vars(args)
    
    for i in dict_args.keys():
        assert dict_args[i]!=None, '"%s" key is None Value!'%i

    style_predict_path = tf.keras.utils.get_file('style_predict.tflite', 'https://tfhub.dev/google/lite-model/magenta/arbitrary-image-stylization-v1-256/int8/prediction/1?lite-format=tflite')
    style_transform_path = tf.keras.utils.get_file('style_transform.tflite', 'https://tfhub.dev/google/lite-model/magenta/arbitrary-image-stylization-v1-256/int8/transfer/1?lite-format=tflite')

    # Load the input images.
    content_image = load_img(args.content_image)
    style_image = load_img(args.style_image)

    # Preprocess the input images.
    preprocessed_content_image = preprocess_image(content_image, 384)
    preprocessed_style_image = preprocess_image(style_image, 256)

    print('Style Image Shape:', preprocessed_style_image.shape)
    print('Content Image Shape:', preprocessed_content_image.shape)

    # Calculate style bottleneck for the preprocessed style image.
    style_bottleneck = run_style_predict(preprocessed_style_image)
    print('Style Bottleneck Shape:', style_bottleneck.shape)

    # Stylize the content image using the style bottleneck.
    stylized_image = run_style_transform(style_bottleneck, preprocessed_content_image)

    print('Stylized Image Shape:', stylized_image.shape, )

    cv.imwrite("./stylized.jpg", cv.cvtColor((stylized_image[0]*255).astype(np.uint8), cv.COLOR_RGB2BGR))