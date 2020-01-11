import sys
from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

import LedCurrent
import LedStatus

class MainApp(QMainWindow):
    def __init__(self,parent = None):
        super(MainApp,self).__init__(parent)
        self.init_UI()

    def init_UI(self):
        self.setWindowIcon(QtGui.QIcon("SL.png"))
        self.main_widget = App(self)
        self.setCentralWidget(self.main_widget)
        self.setStyleSheet("background-color: lightblue;")
        self.setWindowTitle("SL Arduino CAN Data Panel")
        #self.setGeometry(0,0,800,480)
        self.setFixedSize(800,480)
        self.move(0,0)
        self.show()


class App(QWidget):
    def __init__(self,parent):
        super(App,self).__init__(parent)
        self.parent = parent
        self.init_UI()

    def init_UI(self):
        self.BtnWidth = 350
        self.BtnHeight = 250
        self.x =210
        self.y =72

        self.qBox = LedCurrent.Realtimecurrent()
        self.qBox2 = LedStatus.OnOffStatus()
        

        BtncurrentMessage = QPushButton("Sensor Current Data",self)
        setFnt = QFont("Times", 14, QFont.Bold)
        BtncurrentMessage.setFont(setFnt)
        BtncurrentMessage.setToolTip("Click this button to See Led Current Values")
        BtncurrentMessage.clicked.connect(self.open1)
        BtncurrentMessage.setFixedSize(self.BtnWidth,60)
        BtncurrentMessage.move(self.x,60)

        Btnonoffstatus = QPushButton("Led OnOff Status",self)
        setFnt = QFont("Times", 14, QFont.Bold)
        Btnonoffstatus.setFont(setFnt)
        Btnonoffstatus.setToolTip("Click this button to See Led On Off Status")
        Btnonoffstatus.clicked.connect(self.open2)
        Btnonoffstatus.setFixedSize(self.BtnWidth,60)
        Btnonoffstatus.move(self.x,self.y*1+60)

    def open1(self):
        self.qBox.show()

    def open2(self):
        self.qBox2.show()

app = QApplication(sys.argv)
win = MainApp()
win.show()
sys.exit(app.exec_())

        

