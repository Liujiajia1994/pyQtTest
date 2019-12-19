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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 781, 541))
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_file = QtWidgets.QWidget()
        self.tab_file.setObjectName("tab_file")
        self.widget = QtWidgets.QWidget(self.tab_file)
        self.widget.setGeometry(QtCore.QRect(10, 10, 361, 442))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.open_file = QtWidgets.QPushButton(self.groupBox_3)
        self.open_file.setGeometry(QtCore.QRect(100, 50, 151, 51))
        self.open_file.setIconSize(QtCore.QSize(16, 16))
        self.open_file.setObjectName("open_file")
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_info = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_info.setGeometry(QtCore.QRect(10, 40, 341, 151))
        self.textEdit_info.setObjectName("textEdit_info")
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.widget1 = QtWidgets.QWidget(self.tab_file)
        self.widget1.setGeometry(QtCore.QRect(410, 10, 351, 441))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.widget1)
        self.groupBox.setObjectName("groupBox")
        self.image_preshow = QtWidgets.QLabel(self.groupBox)
        self.image_preshow.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.image_preshow.setObjectName("image_preshow")
        self.label_show = QtWidgets.QLabel(self.groupBox)
        self.label_show.setGeometry(QtCore.QRect(10, 110, 321, 280))
        self.label_show.setMinimumSize(QtCore.QSize(280, 280))
        self.label_show.setText("")
        self.label_show.setScaledContents(True)
        self.label_show.setObjectName("label_show")
        self.spinBox_images = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_images.setGeometry(QtCore.QRect(140, 30, 171, 22))
        self.spinBox_images.setObjectName("spinBox_images")
        self.verticalLayout_3.addWidget(self.groupBox)
        self.tabWidget.addTab(self.tab_file, "")
        self.tab_process = QtWidgets.QWidget()
        self.tab_process.setObjectName("tab_process")
        self.tabWidget.addTab(self.tab_process, "")
        self.tab_extract = QtWidgets.QWidget()
        self.tab_extract.setObjectName("tab_extract")
        self.feature_info = QtWidgets.QScrollArea(self.tab_extract)
        self.feature_info.setGeometry(QtCore.QRect(430, 70, 329, 261))
        self.feature_info.setWidgetResizable(True)
        self.feature_info.setObjectName("feature_info")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 327, 259))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.feature_info.setWidget(self.scrollAreaWidgetContents)
        self.extractFeatures = QtWidgets.QLabel(self.tab_extract)
        self.extractFeatures.setGeometry(QtCore.QRect(10, 10, 60, 16))
        self.extractFeatures.setObjectName("extractFeatures")
        self.label = QtWidgets.QLabel(self.tab_extract)
        self.label.setGeometry(QtCore.QRect(430, 52, 329, 12))
        self.label.setObjectName("label")
        self.extract = QtWidgets.QPushButton(self.tab_extract)
        self.extract.setGeometry(QtCore.QRect(140, 410, 75, 31))
        self.extract.setObjectName("extract")
        self.widget2 = QtWidgets.QWidget(self.tab_extract)
        self.widget2.setGeometry(QtCore.QRect(30, 40, 301, 361))
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_Harris = QtWidgets.QCheckBox(self.widget2)
        self.checkBox_Harris.setObjectName("checkBox_Harris")
        self.verticalLayout.addWidget(self.checkBox_Harris)
        self.checkBox_GLCM = QtWidgets.QCheckBox(self.widget2)
        self.checkBox_GLCM.setObjectName("checkBox_GLCM")
        self.verticalLayout.addWidget(self.checkBox_GLCM)
        self.checkBox_FD = QtWidgets.QCheckBox(self.widget2)
        self.checkBox_FD.setObjectName("checkBox_FD")
        self.verticalLayout.addWidget(self.checkBox_FD)
        self.tabWidget.addTab(self.tab_extract, "")
        self.tab_recognize = QtWidgets.QWidget()
        self.tab_recognize.setObjectName("tab_recognize")
        self.tabWidget.addTab(self.tab_recognize, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "选择文件夹"))
        self.open_file.setText(_translate("MainWindow", "浏览文件"))
        self.groupBox_2.setTitle(_translate("MainWindow", "信息显示"))
        self.textEdit_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">选择文件夹名称：</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "预览"))
        self.image_preshow.setText(_translate("MainWindow", "选择预览的图片："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), _translate("MainWindow", "1.打开文件"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_process), _translate("MainWindow", "2.预处理"))
        self.extractFeatures.setText(_translate("MainWindow", "选择特征："))
        self.label.setText(_translate("MainWindow", "特征信息："))
        self.extract.setText(_translate("MainWindow", "提取特征"))
        self.checkBox_Harris.setText(_translate("MainWindow", "Harris角点特征"))
        self.checkBox_GLCM.setText(_translate("MainWindow", "GLCM纹理特征"))
        self.checkBox_FD.setText(_translate("MainWindow", "FD形状特征"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_extract), _translate("MainWindow", "3.特征提取"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_recognize), _translate("MainWindow", "4.训练与识别"))
