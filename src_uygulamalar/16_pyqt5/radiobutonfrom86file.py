# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '16_pyqt5/86_radiobuton.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(568, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btnUlkeler = QtWidgets.QPushButton(self.centralwidget)
        self.btnUlkeler.setGeometry(QtCore.QRect(80, 250, 75, 23))
        self.btnUlkeler.setObjectName("btnUlkeler")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lblUlkeler = QtWidgets.QLabel(self.centralwidget)
        self.lblUlkeler.setGeometry(QtCore.QRect(80, 300, 151, 31))
        self.lblUlkeler.setText("")
        self.lblUlkeler.setObjectName("lblUlkeler")
        self.lblEgitim = QtWidgets.QLabel(self.centralwidget)
        self.lblEgitim.setGeometry(QtCore.QRect(330, 300, 151, 31))
        self.lblEgitim.setText("")
        self.lblEgitim.setObjectName("lblEgitim")
        self.groupBoxUlkeler = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxUlkeler.setGeometry(QtCore.QRect(50, 10, 231, 231))
        self.groupBoxUlkeler.setObjectName("groupBoxUlkeler")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBoxUlkeler)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 20, 161, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridUlkeler = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridUlkeler.setContentsMargins(0, 0, 0, 0)
        self.gridUlkeler.setObjectName("gridUlkeler")
        self.radioAzerbaycan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioAzerbaycan.setObjectName("radioAzerbaycan")
        self.gridUlkeler.addWidget(self.radioAzerbaycan, 1, 0, 1, 1)
        self.radioKibris = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioKibris.setObjectName("radioKibris")
        self.gridUlkeler.addWidget(self.radioKibris, 2, 0, 1, 1)
        self.radioTurkiye = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioTurkiye.setObjectName("radioTurkiye")
        self.gridUlkeler.addWidget(self.radioTurkiye, 0, 0, 1, 1)
        self.radioPakistan = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioPakistan.setObjectName("radioPakistan")
        self.gridUlkeler.addWidget(self.radioPakistan, 3, 0, 1, 1)
        self.radioFilistin = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.radioFilistin.setObjectName("radioFilistin")
        self.gridUlkeler.addWidget(self.radioFilistin, 4, 0, 1, 1)
        self.groupBoxEgitim = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxEgitim.setGeometry(QtCore.QRect(300, 10, 241, 231))
        self.groupBoxEgitim.setObjectName("groupBoxEgitim")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxEgitim)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 20, 160, 211))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridEgitim = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridEgitim.setContentsMargins(0, 0, 0, 0)
        self.gridEgitim.setObjectName("gridEgitim")
        self.radioLise = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioLise.setObjectName("radioLise")
        self.gridEgitim.addWidget(self.radioLise, 1, 0, 1, 1)
        self.radioIlkokul = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioIlkokul.setObjectName("radioIlkokul")
        self.gridEgitim.addWidget(self.radioIlkokul, 0, 0, 1, 1)
        self.radioUniversite = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioUniversite.setObjectName("radioUniversite")
        self.gridEgitim.addWidget(self.radioUniversite, 2, 0, 1, 1)
        self.radioYuksekLisans = QtWidgets.QRadioButton(self.gridLayoutWidget_2)
        self.radioYuksekLisans.setObjectName("radioYuksekLisans")
        self.gridEgitim.addWidget(self.radioYuksekLisans, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 568, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnUlkeler.setText(_translate("MainWindow", "seçim al"))
        self.pushButton_2.setText(_translate("MainWindow", "seçim al"))
        self.groupBoxUlkeler.setTitle(_translate("MainWindow", "ülkeler"))
        self.radioAzerbaycan.setText(_translate("MainWindow", "Azerbaycan"))
        self.radioKibris.setText(_translate("MainWindow", "Kıbrıs"))
        self.radioTurkiye.setText(_translate("MainWindow", "Türkiye"))
        self.radioPakistan.setText(_translate("MainWindow", "Pakistan"))
        self.radioFilistin.setText(_translate("MainWindow", "Filistin"))
        self.groupBoxEgitim.setTitle(_translate("MainWindow", "eğitim"))
        self.radioLise.setText(_translate("MainWindow", "lise"))
        self.radioIlkokul.setText(_translate("MainWindow", "ilkokul"))
        self.radioUniversite.setText(_translate("MainWindow", "üniversite"))
        self.radioYuksekLisans.setText(_translate("MainWindow", "yüksek lisans"))
