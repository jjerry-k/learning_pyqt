import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PIL import Image
import numpy as np

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.left = 150
        self.top = 150
        self.width = 200
        self.height = 200
        self.margine = 1
        self.setupUI()
        self.setMouseTracking(True)

    def setupUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height) 
        self.setWindowTitle('Mouse Tracker') 

        self.label = QLabel(self)
        self.label.move(self.margine, self.margine) 
        self.label.resize(self.width-2*self.margine, 40)
        self.label.setStyleSheet("color: black;"
                              "border-style: solid;"
                              "border-width: 1px;"
                              "border-color: #000000;"
                              "border-radius: 1px") 

        file_list = QLabel('File', self)
        file_list.setStyleSheet("color: black;"
                              "border-style: solid;"
                              "border-width: 1px;"
                              "border-color: #000000;"
                              "border-radius: 1px")
        file_list.move(self.margine, self.margine+39)
        file_list.resize(40, self.height-39-2*self.margine)
        # self.setLayout(vbox)

        canvas = QLabel(self)
        canvas.move(40, 40)
        canvas.setStyleSheet("color: black;"
                              "border-style: solid;"
                              "border-width: 1px;"
                              "border-color: #000000;"
                              "border-radius: 1px")
        canvas.resize(self.width-self.margine-40, self.height-self.margine-40)
        canvas.setMouseTracking(True)
        
        

        
        self.show() 
        
    # def mouseMoveEvent(self, pos):
    #     x = pos.x()
    #     y = pos.y()
 
    #     text = "x: {0}, y: {1} ".format(x, y)
    #     self.label.setText(text)
    def mouseMoveEvent(self, event): 
        self.label.setText('Mouse coords: (%d : %d)' % (event.x()-40, event.y()-40)) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()
