from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import sleep
import sys
import time


class OnOffStatus(QDialog):
    def __init__(self,parent=None):
        
        super(OnOffStatus,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("SL.png"))
        self.setWindowTitle("Led On Off Status Check Panel")
        self.setStyleSheet("background-color: lightblue;")
        self.resize(800,480)
        self.move(0,0)
        self.out1 = 0
        self.init_UI()

    def init_UI(self):
        pass
