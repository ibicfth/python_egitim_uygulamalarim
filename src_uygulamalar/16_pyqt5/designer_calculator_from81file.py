# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '16_pyqt5/81_designer_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow_1):
        MainWindow_1.setObjectName("MainWindow_1")
        MainWindow_1.resize(323, 237)
        self.centralwidget = QtWidgets.QWidget(MainWindow_1)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 47, 61))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 47, 51))
        self.label_2.setObjectName("label_2")
        self.sayi_1_box = QtWidgets.QLineEdit(self.centralwidget)
        self.sayi_1_box.setGeometry(QtCore.QRect(70, 40, 50, 20))
        self.sayi_1_box.setObjectName("sayi_1_box")
        self.sayi_2_box = QtWidgets.QLineEdit(self.centralwidget)
        self.sayi_2_box.setGeometry(QtCore.QRect(70, 80, 50, 20))
        self.sayi_2_box.setObjectName("sayi_2_box")
        self.btn_toplama = QtWidgets.QPushButton(self.centralwidget)
        self.btn_toplama.setGeometry(QtCore.QRect(70, 120, 51, 23))
        self.btn_toplama.setObjectName("btn_toplama")
        self.btn_cikarma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cikarma.setGeometry(QtCore.QRect(130, 120, 51, 23))
        self.btn_cikarma.setObjectName("btn_cikarma")
        self.btn_carpma = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carpma.setGeometry(QtCore.QRect(190, 120, 51, 23))
        self.btn_carpma.setObjectName("btn_carpma")
        self.btn_bolme = QtWidgets.QPushButton(self.centralwidget)
        self.btn_bolme.setGeometry(QtCore.QRect(250, 120, 51, 23))
        self.btn_bolme.setObjectName("btn_bolme")
        self.lbl_sonuc = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sonuc.setGeometry(QtCore.QRect(70, 140, 47, 51))
        self.lbl_sonuc.setObjectName("lbl_sonuc")
        MainWindow_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 323, 21))
        self.menubar.setObjectName("menubar")
        MainWindow_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_1)
        self.statusbar.setObjectName("statusbar")
        MainWindow_1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_1)

    def retranslateUi(self, MainWindow_1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_1.setWindowTitle(_translate("MainWindow_1", "MainWindow"))
        self.label.setText(_translate("MainWindow_1", "sayı 1 : "))
        self.label_2.setText(_translate("MainWindow_1", "sayı 2 : "))
        self.btn_toplama.setText(_translate("MainWindow_1", "toplama"))
        self.btn_cikarma.setText(_translate("MainWindow_1", "çıkarma"))
        self.btn_carpma.setText(_translate("MainWindow_1", "çarpma"))
        self.btn_bolme.setText(_translate("MainWindow_1", "bölme"))
        self.lbl_sonuc.setText(_translate("MainWindow_1", "sonuc"))
