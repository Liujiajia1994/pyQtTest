# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'oceanEddyRecognition.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_pick = QtWidgets.QLabel(self.centralwidget)
        self.image_pick.setGeometry(QtCore.QRect(30, 83, 60, 21))
        self.image_pick.setObjectName("image_pick")
        self.open_file = QtWidgets.QPushButton(self.centralwidget)
        self.open_file.setGeometry(QtCore.QRect(96, 83, 283, 23))
        self.open_file.setObjectName("open_file")
        self.gray_image = QtWidgets.QLabel(self.centralwidget)
        self.gray_image.setGeometry(QtCore.QRect(30, 112, 60, 21))
        self.gray_image.setObjectName("gray_image")
        self.extract = QtWidgets.QPushButton(self.centralwidget)
        self.extract.setGeometry(QtCore.QRect(190, 430, 75, 31))
        self.extract.setObjectName("extract")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 90, 54, 12))
        self.label.setObjectName("label")
        self.feature_info = QtWidgets.QScrollArea(self.centralwidget)
        self.feature_info.setGeometry(QtCore.QRect(500, 90, 291, 191))
        self.feature_info.setWidgetResizable(True)
        self.feature_info.setObjectName("feature_info")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 289, 189))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.feature_info.setWidget(self.scrollAreaWidgetContents)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(100, 120, 281, 171))
        self.widget.setObjectName("widget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 328, 367, 20))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.extractFeatures = QtWidgets.QLabel(self.layoutWidget)
        self.extractFeatures.setObjectName("extractFeatures")
        self.horizontalLayout.addWidget(self.extractFeatures)
        self.checkBox_Harris = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_Harris.setObjectName("checkBox_Harris")
        self.horizontalLayout.addWidget(self.checkBox_Harris)
        self.checkBox_FD = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_FD.setObjectName("checkBox_FD")
        self.horizontalLayout.addWidget(self.checkBox_FD)
        self.checkBox_GLCM = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_GLCM.setObjectName("checkBox_GLCM")
        self.horizontalLayout.addWidget(self.checkBox_GLCM)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_pick.setText(_translate("MainWindow", "选择图片："))
        self.open_file.setText(_translate("MainWindow", "浏览文件"))
        self.gray_image.setText(_translate("MainWindow", "灰度展示："))
        self.extract.setText(_translate("MainWindow", "提取特征"))
        self.label.setText(_translate("MainWindow", "特征信息："))
        self.extractFeatures.setText(_translate("MainWindow", "选择特征："))
        self.checkBox_Harris.setText(_translate("MainWindow", "Harris角点特征"))
        self.checkBox_FD.setText(_translate("MainWindow", "FD形状特征"))
        self.checkBox_GLCM.setText(_translate("MainWindow", "GLCM纹理特征"))
