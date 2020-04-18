# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\taddo3\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\PyQt5\prihlasenie.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from dashboard import Ui_Dashboard


class Ui_Prihlasenie(object):
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
        self.pushButton.clicked.connect(self.go_to_dashboard)
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


    def go_to_dashboard(self):
        print('hi')
        #Prihlasenie.close()
        self.dialogs = list()
        dialog = Ui_Dashboard()
        self.dialogs.append(dialog)
        dialog.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Prihlasenie = QtWidgets.QMainWindow()
    ui = Ui_Prihlasenie()
    ui.setupUi(Prihlasenie)
    Prihlasenie.show()
    sys.exit(app.exec_())
