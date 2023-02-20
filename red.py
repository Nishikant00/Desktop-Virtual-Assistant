from blue import *
import rajni
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sys




class MainThread(QThread):
	
	def __init__(self):
		super(MainThread,self).__init__()
	

startExe = MainThread()

class Gui_S(QMainWindow):
	def __init__(self):
		super().__init__()
		self.gui = Ui_RAJNI()
		self.gui.setupUi(self)
		
		
		

	
		
	startExe.start()



GuiApp = QApplication(sys.argv)
rajni_gui = Gui_S()
rajni_gui.show()
exit(GuiApp.exec_())




	


