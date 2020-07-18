# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(420, 345)
        widget.setMinimumSize(QtCore.QSize(420, 345))
        widget.setMaximumSize(QtCore.QSize(420, 345))
        self.gridLayout = QtWidgets.QGridLayout(widget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(80, 50, 80, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Label = QtWidgets.QLabel(widget)
        self.Label.setMinimumSize(QtCore.QSize(101, 16))
        self.Label.setObjectName("Label")
        self.horizontalLayout.addWidget(self.Label)
        self.LineEdit = QtWidgets.QLineEdit(widget)
        self.LineEdit.setObjectName("LineEdit")
        self.horizontalLayout.addWidget(self.LineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Label_2 = QtWidgets.QLabel(widget)
        self.Label_2.setMinimumSize(QtCore.QSize(101, 16))
        self.Label_2.setObjectName("Label_2")
        self.horizontalLayout_2.addWidget(self.Label_2)
        self.LineEdit_2 = QtWidgets.QLineEdit(widget)
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.horizontalLayout_2.addWidget(self.LineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.checkBox = QtWidgets.QCheckBox(widget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, 20)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_2 = QtWidgets.QPushButton(widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_3.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.Label_3 = QtWidgets.QLabel(widget)
        self.Label_3.setMinimumSize(QtCore.QSize(242, 14))
        self.Label_3.setText("")
        self.Label_3.setObjectName("Label_3")
        self.verticalLayout.addWidget(self.Label_3)
        self.verticalLayout.setStretch(0, 2)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.Label.setText(_translate("widget", "姓名"))
        self.Label_2.setText(_translate("widget", "密码"))
        self.checkBox.setText(_translate("widget", "是否记住密码"))
        self.pushButton_2.setText(_translate("widget", "重置"))
        self.pushButton.setText(_translate("widget", "登录"))
