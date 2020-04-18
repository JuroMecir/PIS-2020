# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\taddo3\AppData\Local\Programs\Python\Python37-32\Lib\site-packages\PyQt5\vyber_izieb.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VyberIzieb(object):
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 190, 191, 41))
        self.pushButton_2.setObjectName("pushButton_2")
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    VyberIzieb = QtWidgets.QMainWindow()
    ui = Ui_VyberIzieb()
    ui.setupUi(VyberIzieb)
    VyberIzieb.show()
    sys.exit(app.exec_())
