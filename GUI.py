#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets, QtGui, QtCore
import sys


class Ui_VyberIzieb(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Ui_VyberIzieb, self).__init__(parent)
        self.showed = False
        self.setupUi(self)

    def setupUi(self, VyberIzieb):
        VyberIzieb.setObjectName("VyberIzieb")
        VyberIzieb.resize(760, 323)
        self.centralwidget = QtWidgets.QWidget(VyberIzieb)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 291, 21))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 60, 401, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 110, 171, 16))
        self.label_2.setObjectName("label_2")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(300, 110, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 140, 191, 16))
        self.label_3.setObjectName("label_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(300, 140, 110, 22))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 190, 191, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushButton_clicked2)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 190, 191, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.on_pushButton_clicked)
        VyberIzieb.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(VyberIzieb)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 760, 26))
        self.menubar.setObjectName("menubar")
        VyberIzieb.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(VyberIzieb)
        self.statusbar.setObjectName("statusbar")
        VyberIzieb.setStatusBar(self.statusbar)

        self.retranslateUi(VyberIzieb)
        QtCore.QMetaObject.connectSlotsByName(VyberIzieb)

    def retranslateUi(self, VyberIzieb):
        _translate = QtCore.QCoreApplication.translate
        VyberIzieb.setWindowTitle(_translate("VyberIzieb", "VyberIzieb"))
        self.label.setText(_translate("VyberIzieb", "Zoznam dostupnych izieb:"))
        self.comboBox.setItemText(0, _translate("VyberIzieb", "Prva dostupna"))
        self.comboBox.setItemText(1, _translate("VyberIzieb", "Druha dostupna"))
        self.comboBox.setItemText(2, _translate("VyberIzieb", "Tretia dostupna"))
        self.comboBox.setItemText(3, _translate("VyberIzieb", "Stvrta dostupna"))
        self.label_2.setText(_translate("VyberIzieb", "Planovany datum ubytovania:"))
        self.label_3.setText(_translate("VyberIzieb", "Planovany datum odubytovania:"))
        self.pushButton.setText(_translate("VyberIzieb", "Potvrdit a ukoncit"))
        self.pushButton_2.setText(_translate("VyberIzieb", "Potvrdit a vybrat dalsiu izbu"))

    def on_pushButton_clicked(self):
        if not self.showed:
            self.showed = True
            self.dialog = Ui_VyberIzieb(self)
            self.dialog.show()
            self.hide()

    def on_pushButton_clicked2(self):
        if not self.showed:
            self.showed = True
            self.dialog = Dashboard(self)
            self.dialog.show()
            self.hide()


class Dashboard(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Dashboard, self).__init__(parent)
        self.showed = False
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(595, 276)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 20, 311, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 50, 201, 21))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 120, 281, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 70, 201, 21))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 595, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        self.label.setText(_translate("MainWindow", "Vitaj na hlavnej stranke ubytovacieho systemu"))
        self.label_2.setText(_translate("MainWindow", "Pocet podanych rezervacii: 0"))
        self.pushButton.setText(_translate("MainWindow", "Rezervovat izbu"))
        self.label_3.setText(_translate("MainWindow", "Pocet schvalenych rezervacii: 0"))

    def on_pushButton_clicked(self):
        if not self.showed:
            self.showed = True
            self.dialog = Ui_VyberIzieb(self)
            self.dialog.show()
            self.hide()


class Prihlasenie(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(Prihlasenie, self).__init__(parent)
        self.showed = False
        self.setupUi(self)

    def setupUi(self, Prihlasenie):
        Prihlasenie.setObjectName("Prihlasenie")
        Prihlasenie.resize(680, 381)
        self.centralwidget = QtWidgets.QWidget(Prihlasenie)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 50, 271, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 90, 271, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(160, 50, 141, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 90, 141, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 140, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        Prihlasenie.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Prihlasenie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 26))
        self.menubar.setObjectName("menubar")
        Prihlasenie.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Prihlasenie)
        self.statusbar.setObjectName("statusbar")
        Prihlasenie.setStatusBar(self.statusbar)

        self.retranslateUi(Prihlasenie)
        QtCore.QMetaObject.connectSlotsByName(Prihlasenie)

    def retranslateUi(self, Prihlasenie):
        _translate = QtCore.QCoreApplication.translate
        Prihlasenie.setWindowTitle(_translate("Prihlasenie", "Prihlasenie"))
        self.label.setText(_translate("Prihlasenie", "Meno:"))
        self.label_2.setText(_translate("Prihlasenie", "Heslo:"))
        self.pushButton.setText(_translate("Prihlasenie", "Prihlasit"))

    def on_pushButton_clicked(self):
        if not self.showed:
            self.showed = True
            self.dialog = Dashboard(self)
            self.dialog.show()
            self.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Prihlasenie()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()