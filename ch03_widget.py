import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Label Box 1
        label1 = QLabel("Firse Label", self)
        #label1.setAlignment(Qt.AlignCenter)
        font1 = label1.font()
        font1.setPointSize(20)
        label1.setFont(font1)

        # Label Box 2
        label2 = QLabel("Second Label", self)
        #label2.setAlignment(Qt.AlignCenter)
        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)
        label2.setFont(font2)

        
        # Check Box
        cb = QCheckBox('Show title', self)
        #cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)
        lab1_hbox = QHBoxLayout()
        lab1_hbox.addWidget(cb)
        lab1_hbox.addWidget(label1)
        
        # Botton 1
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        # btn1.toggle() # botton 누른 상태로

        # Botton 2
        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        # Botton 3
        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)
    
        btnbox = QHBoxLayout()
        btnbox.addWidget(btn1)
        btnbox.addWidget(btn2)
        btnbox.addWidget(btn3)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(label1)
        vbox.addStretch(1)
        vbox.addWidget(label2)
        vbox.addStretch(2)
        vbox.addLayout(btnbox)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
    
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')
    

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())