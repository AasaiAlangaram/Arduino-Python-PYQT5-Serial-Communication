from PyQt5.QtWidgets import *
from PyQt5 import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import sleep
import sys
import time
import serial

#Create Arduino_Serial object
#set correct COM port and Baud Rate
Arduino_Serial = serial.Serial('com3',9600)

class Realtimecurrent(QDialog):
    def __init__(self,parent=None):
        
        super(Realtimecurrent,self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon("SL.png"))
        self.setWindowTitle("Real Time Current Measurement Panel")
        self.setStyleSheet("background-color: lightblue;")
        self.resize(800,480)
        self.move(0,0)
        self.out1 = 0
        self.init_UI()

    def init_UI(self):

        self.read = QPushButton("Read", self)
        self.read.clicked.connect(self.read_data)
        self.read.setFixedSize(100, 40)
        self.read.move(10, 10)

        self.clear = QPushButton("Clear", self)
        self.clear.clicked.connect(self.clear_data)
        self.clear.setFixedSize(100, 40)
        self.clear.move(130, 10)

        self.cont =QCheckBox(self)
        self.cont.stateChanged.connect(self.up_1s)
        self.cont.move(240,20)

        self.label = QLabel("Continue (1s Delay)", self)
        setFnt = QFont("Times", 9, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 35)
        self.label.move(260, 10)

        #High Current
        self.label = QLabel("High Current", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(20, 70)

        self.Txtbrowser = QTextBrowser(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.Txtbrowser.setFont(setFnt)
        self.Txtbrowser.setFixedSize(100,30)
        self.Txtbrowser.move(140,70)

        self.label = QLabel("mA", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(250, 70)

        #Low Current
        self.label = QLabel("Low Current", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(20, 110)

        self.Txtbrowser1 = QTextBrowser(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.Txtbrowser1.setFont(setFnt)
        self.Txtbrowser1.setFixedSize(100,30)
        self.Txtbrowser1.move(140,110)

        self.label = QLabel("mA", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(250, 110)

        #Drl Current
        self.label = QLabel("Drl Current", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(20, 150)

        self.Txtbrowser2 = QTextBrowser(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.Txtbrowser2.setFont(setFnt)
        self.Txtbrowser2.setFixedSize(100,30)
        self.Txtbrowser2.move(140,150)

        self.label = QLabel("mA", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(250, 150)

        #Pstn Current
        self.label = QLabel("Pstn Current", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(20, 190)

        self.Txtbrowser3 = QTextBrowser(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.Txtbrowser3.setFont(setFnt)
        self.Txtbrowser3.setFixedSize(100,30)
        self.Txtbrowser3.move(140,190)

        self.label = QLabel("mA", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(250, 190)

        #Turn Current
        self.label = QLabel("Turn Current", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(20, 230)

        self.Txtbrowser4 = QTextBrowser(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.Txtbrowser4.setFont(setFnt)
        self.Txtbrowser4.setFixedSize(100,30)
        self.Txtbrowser4.move(140,230)

        self.label = QLabel("mA", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(250, 230)

        #SubLow Current
        self.label = QLabel("SubLow ", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(20, 270)

        self.Txtbrowser5 = QTextBrowser(self)
        setFnt = QFont("Times", 11, QFont.Bold)
        self.Txtbrowser5.setFont(setFnt)
        self.Txtbrowser5.setFixedSize(100,30)
        self.Txtbrowser5.move(140,270)

        self.label = QLabel("mA", self)
        setFnt = QFont("Times", 10, QFont.Bold)
        self.label.setFont(setFnt)
        self.label.setFixedSize(300, 30)
        self.label.move(250, 270)

        self.TimerTask=None
        
    def read_data(self):
        
        k = Arduino_Serial.readline().decode()
        print("Voltage:",k)
        
        self.Txtbrowser.setText(str(k))
        self.Txtbrowser1.setText(str(k))
        self.Txtbrowser2.setText(str(k))
        self.Txtbrowser3.setText(str(k))
        self.Txtbrowser4.setText(str(k))
        self.Txtbrowser5.setText(str(k))

    def clear_data(self):
        
        self.Txtbrowser.clear()
    
    def up_1s(self,state):
        '''
        Threading

        Continuosly Read data for every 1Sec
        '''

        try:
            if self.TimerTask == None:
                self.TimerTask = QTimer()


            if state == QtCore.Qt.Checked:
                #self.read()
                self.TimerTask.timeout.connect(self.read_data)
                self.TimerTask.start(1000)
                
            else:
                self.TimerTask.stop()
                
            pass

        except(TypeError,ValueError,AttributeError):

            print("Oops!", sys.exc_info()[0], "occured.")
            pass

#app = QApplication(sys.argv)
#screen = Realtime()
#screen.show()
#sys.exit(app.exec_())
