import sys, os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.left, self.top = 100, 100
        self.width, self.height = 640, 480
        self.margin = 1
        self.stbar = self.statusBar()
        self.stbar.resize(self.width, 20)
        self.mnbar = self.menuBar()
        self.setWindowTitle("Test")
        self.file_view = list_widget(self) 
        self.result_view = list_widget(self) 
        self.display = QLabel("Canvas", self)
        
        self.toolbar_h = 40
        self.list_view_w = 120

        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setMouseTracking(True)
        
        self.init_App()

    def init_App(self):

        # ==============================================================
        # =================== Open Button of Toolbar ===================
        # ==============================================================
        openAction = QAction(QIcon('./img/open.png'), 'Open', self)
        openAction.setShortcut('Ctrl+O')
        openAction.setStatusTip('Open File')
        openAction.triggered.connect(self.showDialog)

        # ==============================================================
        # =================== Save Button of Toolbar ===================
        # ==============================================================
        saveAction = QAction(QIcon('./img/save.png'), 'Save', self)
        saveAction.setShortcut('Ctrl+S')
        saveAction.setStatusTip('Save File')
        # saveAction.triggered.connect(self.showDialog)

        # ==============================================================
        # =================== Exit Button of Toolbar ===================
        # ==============================================================
        exitAction = QAction(QIcon('./img/exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)


        # ==============================================================
        # ====================== Toolbar Setting =======================
        # ==============================================================
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.resize(self.width, self.toolbar_h)
        self.toolbar.addAction(openAction)
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(exitAction)
        #self.toolbar.setHeight(toolbar_h)
        self.tb_width = self.toolbar.width()
        self.tb_height = self.toolbar.height()

        # ==============================================================
        # ====================== File List Widget ======================
        # ==============================================================
        self.file_view.move(0, self.tb_height+3*self.margin) 
        self.file_view.resize(self.list_view_w, self.height-self.tb_height-self.stbar.height()-4*self.margin)
        self.file_view.list_box.resize(self.list_view_w, self.height-self.tb_height-self.stbar.height()-4*self.margin)


        # ==============================================================
        # ===================== Result List Widget =====================
        # ==============================================================
        self.result_view.move(self.width-self.list_view_w, self.tb_height+3*self.margin) 
        self.result_view.resize(self.list_view_w, self.height-self.tb_height-self.stbar.height()-4*self.margin)
        self.result_view.list_box.resize(self.list_view_w, self.height-self.tb_height-self.stbar.height()-4*self.margin)
        
        # ==============================================================
        # ======================= Display Widget =======================
        # ==============================================================
        self.img_width = self.width-2*self.list_view_w
        self.img_height = self.height-self.tb_height-self.stbar.height()-4*self.margin
        self.display.setMaximumWidth(self.img_width)
        # self.display.setMinimumHeight(self.img_height)
        self.display.setMaximumWidth(self.img_width)
        # self.display.setMinimumHeight(self.img_height)
        self.display.setMouseTracking(True)
        self.display.move(self.list_view_w, self.tb_height+3*self.margin)
        self.display.resize(self.img_width, self.img_height)
        self.display.setAlignment(Qt.AlignCenter)
        
        # ==============================================================
        # ======================= Read & Display =======================
        # ==============================================================
        self.file_view.list_box.clicked.connect(self.read_img)

        self.show()

    def mouseMoveEvent(self, event): 
        txt = "Mouse 위치 : x={0},y={1}, global={2},{3}".format(event.x()-self.list_view_w, event.y()-self.toolbar.height(), 
        event.globalX()-self.list_view_w, event.globalY()-self.stbar.height()) 
        self.stbar.showMessage(txt) 

    def showDialog(self):
        self.fname = QFileDialog.getExistingDirectory(self, 'Open file')
        # self.fname = './img'
        file_list = [i for i in sorted(os.listdir(self.fname)) if i.split('.')[1] in ['jpg', 'jpeg', 'png', 'bmp', 'tiff']]
        model = QStandardItemModel()
        for f in file_list:
            model.appendRow(QStandardItem(f))
            
        self.file_view.list_box.setModel(model)
    
    
    def read_img(self, index):
        path = self.fname 
        itms = self.file_view.list_box.selectedIndexes()
        #print(path, itms)
        img_path = os.path.join(path, itms[0].data())
        print(img_path)
        pixmap= QPixmap(img_path).scaled(self.img_width, self.img_height)
        self.display.setPixmap(pixmap)
    
    def on_row_changed(self, current, previous):
        print('Row %d selected' % current.row())

class list_widget(QWidget):
    def __init__(self, parent):
        super(list_widget, self).__init__(parent)
        self.list_box = QListView(self)
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())