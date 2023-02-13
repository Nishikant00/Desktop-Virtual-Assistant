from blue import Ui_MainWindow
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys
import rajni.py



class MainThread(QThread):
	def __init__(self):
		super(MainThread,self).__init__()
	def run(self):
		startExe = MainThread()	


class Gui_Start(QMainWindow):
	def __init__(self):
		super().__init__()
		self.gui = Ui_MainWindow
		self.gui.setUpUi(self)
		self.gui.Pushbutton_start.clicked.connect(self.startTask)
		self.gui.Pushbutton_exit.clicked.connect(self.close)

	def startTask(self):
		self.gui.label1= QtGui.QMovie("Console/live.gif")
		self.gui.Gif_1.setMovie(self.gui.label1)
		self.gui.label1.start()

		self.gui.label2= QtGui.QMovie("Console/Aqua.gif")
		self.gui.Gif_2.setMovie(self.gui.label2)
		self.gui.label2.start()


GuiApp = QApplication(sys.argv)
jarvis_gui = Gui_Start()
jarvis_gui.show()
exit(GuiApp.exec_())