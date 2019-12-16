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
        self.extract = QtWidgets.QPushButton(self.centralwidget)
        self.extract.setGeometry(QtCore.QRect(140, 370, 75, 31))
        self.extract.setObjectName("extract")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 60, 369, 87))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.image_pick = QtWidgets.QLabel(self.layoutWidget)
        self.image_pick.setObjectName("image_pick")
        self.verticalLayout.addWidget(self.image_pick)
        self.open_file = QtWidgets.QPushButton(self.layoutWidget)
        self.open_file.setObjectName("open_file")
        self.verticalLayout.addWidget(self.open_file)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
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
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(450, 60, 331, 281))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.feature_info = QtWidgets.QScrollArea(self.layoutWidget1)
        self.feature_info.setWidgetResizable(True)
        self.feature_info.setObjectName("feature_info")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 327, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.feature_info.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.feature_info)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.extract.setText(_translate("MainWindow", "提取特征"))
        self.image_pick.setText(_translate("MainWindow", "选择图片："))
        self.open_file.setText(_translate("MainWindow", "浏览文件"))
        self.label_2.setText(_translate("MainWindow", "预览："))
        self.extractFeatures.setText(_translate("MainWindow", "选择特征："))
        self.checkBox_Harris.setText(_translate("MainWindow", "Harris角点特征"))
        self.checkBox_FD.setText(_translate("MainWindow", "FD形状特征"))
        self.checkBox_GLCM.setText(_translate("MainWindow", "GLCM纹理特征"))
        self.label.setText(_translate("MainWindow", "特征信息："))
