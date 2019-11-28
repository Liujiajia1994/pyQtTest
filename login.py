# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(widget)
        self.pushButton.setGeometry(QtCore.QRect(200, 190, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(widget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 190, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.Label = QtWidgets.QLabel(widget)
        self.Label.setGeometry(QtCore.QRect(81, 51, 24, 16))
        self.Label.setObjectName("Label")
        self.LineEdit = QtWidgets.QLineEdit(widget)
        self.LineEdit.setGeometry(QtCore.QRect(182, 51, 128, 20))
        self.LineEdit.setObjectName("LineEdit")
        self.Label_2 = QtWidgets.QLabel(widget)
        self.Label_2.setGeometry(QtCore.QRect(81, 90, 24, 16))
        self.Label_2.setObjectName("Label_2")
        self.LineEdit_2 = QtWidgets.QLineEdit(widget)
        self.LineEdit_2.setGeometry(QtCore.QRect(182, 90, 128, 20))
        self.LineEdit_2.setObjectName("LineEdit_2")
        self.checkBox = QtWidgets.QCheckBox(widget)
        self.checkBox.setGeometry(QtCore.QRect(120, 140, 95, 16))
        self.checkBox.setObjectName("checkBox")

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "登录"))
        self.pushButton.setText(_translate("widget", "登录"))
        self.pushButton_2.setText(_translate("widget", "重置"))
        self.Label.setText(_translate("widget", "姓名"))
        self.Label_2.setText(_translate("widget", "密码"))
        self.checkBox.setText(_translate("widget", "是否记住密码"))


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QIcon

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_widget()
    ui.setupUi(widget)
    widget.setWindowIcon(QIcon('logo.jpg'))  # 增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())