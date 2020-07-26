import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QToolTip, QMainWindow, QAction, qApp, QDesktopWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QFont, QIcon


class MyApp_Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # Tooltip 기본 설정
        QToolTip.setFont(QFont('SansSerif', 10))

        # 기본 화면에 대한 Tooltip
        self.setToolTip('This is a <b>Window</b>')

        # Window Size 설정
        W, H = 400, 300

        # Button 설정
        btn = QPushButton('Quit', self)
        btn.setToolTip('This is a <b>Quit Button</b>!')
        # Button Size 
        W_b = btn.sizeHint().width()
        H_b = btn.sizeHint().height()

        # Window Size 고려하여 Button 이동
        btn.move(W-W_b, H-H_b)
        btn.resize(btn.sizeHint())

        # Button click event
        btn.clicked.connect(QCoreApplication.instance().quit)

        # UI Title
        self.setWindowTitle('Exercise UI')
        # UI 화면 위치
        self.move(100, 300)
        # UI 사이즈 조절
        self.resize(W, H)
        self.center()
        self.show()

    def center(self):
        
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

class MyApp_MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        saveAction = QAction(QIcon('./img/save.png'), 'Exit', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save application')
        editAction = QAction(QIcon('./img/edit.png'), 'Exit', self)
        editAction.setShortcut('Ctrl+E')
        editAction.setStatusTip('Edit application')
        exitAction = QAction(QIcon('./img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Save')
        self.toolbar.addAction(saveAction)

        self.toolbar = self.addToolBar('Edit')
        self.toolbar.addAction(editAction)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.center()
        self.show()

    def center(self):
    
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp_MainWindow()
    sys.exit(app.exec_())
