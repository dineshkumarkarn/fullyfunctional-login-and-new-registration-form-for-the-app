# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from login import Ui_Form_l

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3

my_form = sqlite3.connect('registration.sql')
cur = my_form.cursor()


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1044, 645)
        Form.setMinimumSize(QtCore.QSize(0, 507))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        Form.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TITLE = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.TITLE.setFont(font)
        self.TITLE.setAlignment(QtCore.Qt.AlignCenter)
        self.TITLE.setObjectName("TITLE")
        self.horizontalLayout.addWidget(self.TITLE)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.enterYourUserIdLabel = QtWidgets.QLabel(Form)
        self.enterYourUserIdLabel.setObjectName("enterYourUserIdLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole,
                                  self.enterYourUserIdLabel)
        self.enterYourUserIdLineEdit = QtWidgets.QLineEdit(Form)
        self.enterYourUserIdLineEdit.setObjectName("enterYourUserIdLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole,
                                  self.enterYourUserIdLineEdit)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.LabelRole, spacerItem)
        self.fullNameLabel = QtWidgets.QLabel(Form)
        self.fullNameLabel.setObjectName("fullNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole,
                                  self.fullNameLabel)
        self.fullNameLineEdit = QtWidgets.QLineEdit(Form)
        self.fullNameLineEdit.setObjectName("fullNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole,
                                  self.fullNameLineEdit)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.LabelRole,
                                spacerItem1)
        self.dOBLabel = QtWidgets.QLabel(Form)
        self.dOBLabel.setObjectName("dOBLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole,
                                  self.dOBLabel)
        self.dOBDateEdit = QtWidgets.QDateEdit(Form)
        self.dOBDateEdit.setObjectName("dOBDateEdit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole,
                                  self.dOBDateEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.LabelRole,
                                spacerItem2)
        self.addressLabel = QtWidgets.QLabel(Form)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole,
                                  self.addressLabel)
        self.addressLineEdit = QtWidgets.QLineEdit(Form)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole,
                                  self.addressLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.LabelRole,
                                spacerItem3)
        self.mobileLabel = QtWidgets.QLabel(Form)
        self.mobileLabel.setObjectName("mobileLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole,
                                  self.mobileLabel)
        self.mobileLineEdit = QtWidgets.QLineEdit(Form)
        self.mobileLineEdit.setObjectName("mobileLineEdit")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole,
                                  self.mobileLineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(9, QtWidgets.QFormLayout.LabelRole,
                                spacerItem4)
        self.mailLabel = QtWidgets.QLabel(Form)
        self.mailLabel.setObjectName("mailLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole,
                                  self.mailLabel)
        self.mailLineEdit = QtWidgets.QLineEdit(Form)
        self.mailLineEdit.setObjectName("mailLineEdit")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole,
                                  self.mailLineEdit)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(11, QtWidgets.QFormLayout.LabelRole,
                                spacerItem5)
        self.professionLabel = QtWidgets.QLabel(Form)
        self.professionLabel.setObjectName("professionLabel")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole,
                                  self.professionLabel)
        self.professionLineEdit = QtWidgets.QLineEdit(Form)
        self.professionLineEdit.setObjectName("professionLineEdit")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole,
                                  self.professionLineEdit)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.LabelRole,
                                spacerItem6)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setAutoFillBackground(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.SpanningRole,
                                  self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.SpanningRole,
                                  self.pushButton)
        self.yourPasswordLabel = QtWidgets.QLabel(Form)
        self.yourPasswordLabel.setObjectName("yourPasswordLabel")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole,
                                  self.yourPasswordLabel)
        self.yourPasswordLineEdit = QtWidgets.QLineEdit(Form)
        self.yourPasswordLineEdit.setObjectName("yourPasswordLineEdit")
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole,
                                  self.yourPasswordLineEdit)
        self.confirmYourPasswordLabel = QtWidgets.QLabel(Form)
        self.confirmYourPasswordLabel.setObjectName("confirmYourPasswordLabel")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole,
                                  self.confirmYourPasswordLabel)
        self.confirmYourPasswordLineEdit = QtWidgets.QLineEdit(Form)
        self.confirmYourPasswordLineEdit.setObjectName(
            "confirmYourPasswordLineEdit")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole,
                                  self.confirmYourPasswordLineEdit)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(15, QtWidgets.QFormLayout.LabelRole,
                                spacerItem7)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(
            self.professionLineEdit.clear)  # type: ignore
        self.pushButton.clicked.connect(
            self.mailLineEdit.clear)  # type: ignore
        self.pushButton.clicked.connect(
            self.mobileLineEdit.clear)  # type: ignore
        self.pushButton.clicked.connect(
            self.addressLineEdit.clear)  # type: ignore
        self.pushButton.clicked.connect(
            self.fullNameLineEdit.clear)  # type: ignore
        self.pushButton.clicked.connect(self.dOBDateEdit.clear)  # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(self.submit)  # type: ignore

    def submit(self):

        sql = "SELECT userid FROM form"
        cur.execute(sql)
        a = cur.fetchall()
        df = pd.DataFrame(a)
        print(df)

        if self.enterYourUserIdLineEdit.text() in df.values:
            msg = QMessageBox()
            msg.setWindowTitle("Error in the Form")
            msg.setText("this user is present in here")
            # msg.setIcon(self,QMessageBox.warning)

            msg.exec_()
            

        elif (self.enterYourUserIdLineEdit.text() == ""
            or self.fullNameLineEdit.text() == ""
            or self.dOBDateEdit.text()== "" 
            or self.addressLineEdit.text() == ""
            or self.mobileLineEdit.text() == ""
            or self.mailLineEdit.text( ) == '' 
            or self.professionLineEdit.text() == '' 
            or self.confirmYourPasswordLineEdit.text() == '' 
            or self.yourPasswordLineEdit.text() == ''):
            print("fill the values")

            msg = QMessageBox()
            msg.setWindowTitle("Error in the Form")
            msg.setText("please fill all the boxess")
            # msg.setIcon(self,QMessageBox.warning)

            msg.exec_()

        else:
            useid = self.enterYourUserIdLineEdit.text()
            print("user id is=", self.enterYourUserIdLineEdit.text())

            name = self.fullNameLineEdit.text()
            print(self.fullNameLineEdit.text())

            dob = self.dOBDateEdit.text()
            print(self.dOBDateEdit.text())

            add = self.addressLineEdit.text()
            print(self.addressLineEdit.text())

            mobi = self.mobileLineEdit.text()
            print(self.mobileLineEdit.text())

            mail = self.mailLineEdit.text()
            print(self.mailLineEdit.text())

            pro = self.professionLineEdit.text()
            print(self.professionLineEdit.text())

            pas = self.confirmYourPasswordLineEdit.text()
            print(self.yourPasswordLineEdit.text())
            print(self.confirmYourPasswordLineEdit.text())

            cur.execute(
                '''INSERT INTO form (
                    UserId , 
                    FullName ,
                    DOB , 
                    Address, 
                    mobile , 
                    mail ,  
                    prefossion ,
                    password) 
                    VALUES(?,?,?,?,?,?,?,?);''',
                (useid, name, dob, add, mobi, mail, pro, pas))

            my_form.commit()

            self.window = QtWidgets.QWidget()
            self.ow = Ui_Form_l()
            self.ow.setupUi(self.window)
            # Form.hide()
            self.window.show()

       

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TITLE.setText(_translate("Form",
                                      "PYTHON DEVELOPERS REGISTRATION"))
        self.enterYourUserIdLabel.setText(
            _translate("Form", "enter your UserId :"))
        self.fullNameLabel.setText(_translate("Form", "Full Name :"))
        self.dOBLabel.setText(_translate("Form", "DOB :"))
        self.addressLabel.setText(_translate("Form", "Address :"))
        self.mobileLabel.setText(_translate("Form", "mobile :"))
        self.mailLabel.setText(_translate("Form", "mail :"))
        self.professionLabel.setText(_translate("Form", "Profession :"))
        self.pushButton_2.setText(_translate("Form", "Submit"))
        self.pushButton.setText(_translate("Form", "Reset"))
        self.yourPasswordLabel.setText(_translate("Form", "Your Password :"))
        self.confirmYourPasswordLabel.setText(
            _translate("Form", "Confirm your Password :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())