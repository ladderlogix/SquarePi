from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QHBoxLayout
import main
import time
import json
import threading

f = open("Settings.json")
Settings = json.load(f)

BackgroundRedValue = Settings['BackgroundRedValue']
BackgroundBlueValue = Settings['BackgroundBlueValue']
BackgroundGreenValue = Settings['BackgroundGreenValue']
CircleRedValue = Settings['CircleRedValue']
CircleBlueValue = Settings['CircleBlueValue']
CircleGreenValue = Settings['CircleGreenValue']
DotsRedValue = Settings['DotsRedValue']
DotsGreenValue = Settings['DotsGreenValue']
DotsBlueValue = Settings['DotsBlueValue']

f.close()

class Ui_ProgramControl(object):

	def setupUi(self, ProgramControl):
		ProgramControl.setObjectName("ProgramControl")
		ProgramControl.resize(500, 400)
		sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
		sizePolicy.setHorizontalStretch(1)
		sizePolicy.setVerticalStretch(1)
		sizePolicy.setHeightForWidth(ProgramControl.sizePolicy().hasHeightForWidth())
		ProgramControl.setSizePolicy(sizePolicy)
		self.centralwidget = QtWidgets.QWidget(ProgramControl)
		self.centralwidget.setObjectName("centralwidget")
		self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
		self.horizontalSlider_2.setGeometry(QtCore.QRect(80, 305, 251, 31))
		self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider_2.setInvertedAppearance(False)
		self.horizontalSlider_2.setTickPosition(QtWidgets.QSlider.TicksAbove)
		self.horizontalSlider_2.setTickInterval(0)
		self.horizontalSlider_2.setObjectName("horizontalSlider_2")
		self.label = QtWidgets.QLabel(self.centralwidget)
		self.label.setGeometry(QtCore.QRect(10, 180, 71, 51))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.label_4 = QtWidgets.QLabel(self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(20, 308, 51, 21))
		self.label_4.setAlignment(QtCore.Qt.AlignCenter)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(20, 348, 51, 21))
		self.label_5.setAlignment(QtCore.Qt.AlignCenter)
		self.label_5.setObjectName("label_5")
		self.label_7 = QtWidgets.QLabel(self.centralwidget)
		self.label_7.setGeometry(QtCore.QRect(10, 110, 71, 51))
		self.label_7.setAlignment(QtCore.Qt.AlignCenter)
		self.label_7.setObjectName("label_7")
		self.label_8 = QtWidgets.QLabel(self.centralwidget)
		self.label_8.setGeometry(QtCore.QRect(9, 40, 71, 51))
		self.label_8.setAlignment(QtCore.Qt.AlignCenter)
		self.label_8.setObjectName("label_8")
		self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
		self.lcdNumber.setGeometry(QtCore.QRect(100, 110, 101, 51))
		self.lcdNumber.setProperty("value", 1.0)
		self.lcdNumber.setObjectName("lcdNumber")
		self.pushButton = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(370, 310, 111, 61))
		self.pushButton.setObjectName("pushButton")
		self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_2.setGeometry(QtCore.QRect(420, 40, 61, 41))
		self.spinBox_2.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_2.setMaximum(255)
		self.spinBox_2.setProperty("value", 255)
		self.spinBox_2.setObjectName("spinBox_2")
		self.label_2 = QtWidgets.QLabel(self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(240, 10, 61, 31))
		self.label_2.setAlignment(QtCore.Qt.AlignCenter)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(330, 10, 61, 31))
		self.label_3.setAlignment(QtCore.Qt.AlignCenter)
		self.label_3.setObjectName("label_3")
		self.label_6 = QtWidgets.QLabel(self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(420, 10, 61, 31))
		self.label_6.setAlignment(QtCore.Qt.AlignCenter)
		self.label_6.setObjectName("label_6")
		self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
		self.pushButton_2.setGeometry(QtCore.QRect(310, 240, 91, 41))
		self.pushButton_2.setObjectName("pushButton_2")
		self.pushButton_2.clicked.connect(self.Apply)
		self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_3.setGeometry(QtCore.QRect(420, 110, 61, 41))
		self.spinBox_3.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_3.setMaximum(255)
		self.spinBox_3.setProperty("value", 255)
		self.spinBox_3.setObjectName("spinBox_3")
		self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_4.setGeometry(QtCore.QRect(420, 180, 61, 41))
		self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_4.setMaximum(255)
		self.spinBox_4.setProperty("value", 255)
		self.spinBox_4.setObjectName("spinBox_4")
		self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_5.setGeometry(QtCore.QRect(330, 40, 61, 41))
		self.spinBox_5.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_5.setMaximum(255)
		self.spinBox_5.setProperty("value", 255)
		self.spinBox_5.setObjectName("spinBox_5")
		self.spinBox_6 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_6.setGeometry(QtCore.QRect(330, 110, 61, 41))
		self.spinBox_6.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_6.setMaximum(255)
		self.spinBox_6.setProperty("value", 255)
		self.spinBox_6.setObjectName("spinBox_6")
		self.spinBox_7 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_7.setGeometry(QtCore.QRect(330, 180, 61, 41))
		self.spinBox_7.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_7.setMaximum(255)
		self.spinBox_7.setProperty("value", 255)
		self.spinBox_7.setObjectName("spinBox_7")
		self.spinBox_8 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_8.setGeometry(QtCore.QRect(240, 40, 61, 41))
		self.spinBox_8.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_8.setMaximum(255)
		self.spinBox_8.setProperty("value", 255)
		self.spinBox_8.setObjectName("spinBox_8")
		self.spinBox_9 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_9.setGeometry(QtCore.QRect(240, 110, 61, 41))
		self.spinBox_9.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_9.setMaximum(255)
		self.spinBox_9.setProperty("value", 255)
		self.spinBox_9.setObjectName("spinBox_9")
		self.spinBox_10 = QtWidgets.QSpinBox(self.centralwidget)
		self.spinBox_10.setGeometry(QtCore.QRect(240, 180, 61, 41))
		self.spinBox_10.setAlignment(QtCore.Qt.AlignCenter)
		self.spinBox_10.setMaximum(255)
		self.spinBox_10.setProperty("value", 255)
		self.spinBox_10.setObjectName("spinBox_10")
		self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
		self.lcdNumber_2.setGeometry(QtCore.QRect(100, 40, 101, 51))
		self.lcdNumber_2.setProperty("value", 1.0)
		self.lcdNumber_2.setObjectName("lcdNumber_2")
		self.lcdNumber_3 = QtWidgets.QLCDNumber(self.centralwidget)
		self.lcdNumber_3.setGeometry(QtCore.QRect(100, 180, 101, 51))
		self.lcdNumber_3.setProperty("value", 1.0)
		self.lcdNumber_3.setObjectName("lcdNumber_3")
		self.horizontalSlider_3 = QtWidgets.QSlider(self.centralwidget)
		self.horizontalSlider_3.setGeometry(QtCore.QRect(80, 350, 251, 31))
		self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
		self.horizontalSlider_3.setInvertedAppearance(False)
		self.horizontalSlider_3.setTickPosition(QtWidgets.QSlider.TicksAbove)
		self.horizontalSlider_3.setTickInterval(0)
		self.horizontalSlider_3.setObjectName("horizontalSlider_3")
		ProgramControl.setCentralWidget(self.centralwidget)

		self.retranslateUi(ProgramControl)
		QtCore.QMetaObject.connectSlotsByName(ProgramControl)

	def retranslateUi(self, ProgramControl):
		_translate = QtCore.QCoreApplication.translate
		ProgramControl.setWindowTitle(_translate("ProgramControl", "Controler"))
		self.label.setText(_translate("ProgramControl", "Total Circles"))
		self.label_4.setText(_translate("ProgramControl", "Speed"))
		self.label_5.setText(_translate("ProgramControl", "Size"))
		self.label_7.setText(_translate("ProgramControl", "Green Circles"))
		self.label_8.setText(_translate("ProgramControl", "Pi"))
		self.pushButton.setText(_translate("ProgramControl", "Show Graphs"))
		self.label_2.setText(_translate("ProgramControl", "Big Circle"))
		self.label_3.setText(_translate("ProgramControl", "Dots"))
		self.label_6.setText(_translate("ProgramControl", "Background"))
		self.pushButton_2.setText(_translate("ProgramControl", "Apply"))
		self.spinBox_2.setProperty("value", BackgroundRedValue) # Background 1
		self.spinBox_3.setProperty("value", BackgroundGreenValue) # Background 2
		self.spinBox_4.setProperty("value", BackgroundBlueValue) # Background 3
		self.spinBox_5.setProperty("value", DotsRedValue) # Dots 1
		self.spinBox_6.setProperty("value", DotsGreenValue) # Dots 2
		self.spinBox_7.setProperty("value", DotsBlueValue) # Dots 3
		self.spinBox_8.setProperty("value", CircleRedValue) # Big Circle 1
		self.spinBox_9.setProperty("value", CircleGreenValue) #Big Circle 2
		self.spinBox_10.setProperty("value", CircleBlueValue) # Big Circle 3

	def UpdateText(self):
		pi, n, n2 = main.PygameMain()
		self.lcdNumber.setProperty("value", str(n))
		self.lcdNumber_2.setProperty("value", str(pi))
		self.lcdNumber_3.setProperty("value", str(n2))
		off = self.horizontalSlider_2.value()
		off = off/100
		time.sleep(off)

	def Apply(self):
		BackgroundRedValue = self.spinBox_2.value()
		BackgroundGreenValue = self.spinBox_3.value()
		BackgroundBlueValue = self.spinBox_4.value()
		CircleRedValue = self.spinBox_8.value()
		CircleGreenValue = self.spinBox_9.value()
		CircleBlueValue = self.spinBox_10.value()
		DotsRedValue = self.spinBox_5.value()
		DotsGreenValue = self.spinBox_6.value()
		DotsBlueValue = self.spinBox_7.value()

		NSettings = {}
		NSettings['BackgroundRedValue'] = BackgroundRedValue
		NSettings['BackgroundBlueValue'] = BackgroundBlueValue
		NSettings['BackgroundGreenValue'] = BackgroundGreenValue
		NSettings['CircleRedValue'] = CircleRedValue
		NSettings['CircleBlueValue'] = CircleBlueValue
		NSettings['CircleGreenValue'] = CircleGreenValue
		NSettings['DotsRedValue'] = DotsRedValue
		NSettings['DotsBlueValue'] = DotsBlueValue
		NSettings['DotsGreenValue'] = DotsGreenValue

		with open('Settings.json', 'w') as outfile:
			json.dump(NSettings, outfile)

		main.ForceReload()

def run():
	import sys
	app = QtWidgets.QApplication(sys.argv)
	ProgramControl = QtWidgets.QMainWindow()
	ui = Ui_ProgramControl()
	ui.setupUi(ProgramControl)
	ProgramControl.show()
	while True:
		ui.UpdateText()
