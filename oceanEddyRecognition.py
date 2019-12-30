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
        MainWindow.resize(789, 550)
        MainWindow.setMinimumSize(QtCore.QSize(789, 550))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(-1, 9, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setStyleSheet("QTabWidget::pane{\n"
"    border:none;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QTabWidget::tab-bar{\n"
"    alignment:left;\n"
"}\n"
"QTabBar::tab{\n"
"    background:transparent;\n"
"    min-width:30ex;\n"
"    min-height:10ex;\n"
"}\n"
"QTabBar::tab:hover{\n"
"    background:rgb(255, 255, 255, 100);\n"
"}\n"
"QTabBar::tab:selected{\n"
"    border-color: white;\n"
"    background:white;\n"
"    color:green;\n"
"}\n"
"")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_file = QtWidgets.QWidget()
        self.tab_file.setStyleSheet("")
        self.tab_file.setObjectName("tab_file")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_file)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_file)
        self.groupBox_3.setMinimumSize(QtCore.QSize(359, 217))
        self.groupBox_3.setObjectName("groupBox_3")
        self.open_file = QtWidgets.QPushButton(self.groupBox_3)
        self.open_file.setGeometry(QtCore.QRect(100, 50, 151, 51))
        self.open_file.setStyleSheet("QPushButton{  \n"
"    border: 1px solid #ffffff;    \n"
"    background-color:#62d8fe;\n"
"    border-style: solid;  \n"
"    border-radius:5px;  \n"
"    width: 100px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"} \n"
"QPushButton:hover{     \n"
"    border: 1px solid #ffffff;  \n"
"    background-color:#d6f7fe;\n"
"    border-style: solid;  \n"
"    border-radius:5px;  \n"
"    width: 40px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"}\n"
"QPushButton:pressed{  \n"
"    background-color:#EAF0FF;  \n"
"    border: 1px solid #AAB4C4;  \n"
"    width: 40px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"    border-radius:5px;  \n"
"}")
        self.open_file.setIconSize(QtCore.QSize(16, 16))
        self.open_file.setObjectName("open_file")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_file)
        self.groupBox_2.setMinimumSize(QtCore.QSize(359, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textEdit_info = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEdit_info.setGeometry(QtCore.QRect(10, 40, 341, 151))
        self.textEdit_info.setObjectName("textEdit_info")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout.setStretch(0, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.groupBox = QtWidgets.QGroupBox(self.tab_file)
        self.groupBox.setMinimumSize(QtCore.QSize(349, 481))
        self.groupBox.setObjectName("groupBox")
        self.image_preshow = QtWidgets.QLabel(self.groupBox)
        self.image_preshow.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.image_preshow.setObjectName("image_preshow")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(150, 30, 171, 30))
        self.comboBox.setStyleSheet("QComboBox {\n"
"    font-family: \"微软雅黑\";\n"
"    color: black;\n"
"    border: 1px #1a1a1a solid;\n"
"    background-color:#62d8fe;\n"
"}\n"
"")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 90, 351, 381))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_show = QtWidgets.QLabel(self.tab)
        self.label_show.setGeometry(QtCore.QRect(0, 0, 351, 351))
        self.label_show.setMinimumSize(QtCore.QSize(351, 351))
        self.label_show.setMaximumSize(QtCore.QSize(351, 351))
        self.label_show.setScaledContents(True)
        self.label_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show.setObjectName("label_show")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_show_gray = QtWidgets.QLabel(self.tab_2)
        self.label_show_gray.setGeometry(QtCore.QRect(0, 0, 351, 351))
        self.label_show_gray.setScaledContents(True)
        self.label_show_gray.setObjectName("label_show_gray")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("source/folder_opened_128px_1222856_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_file, icon, "")
        self.tab_process = QtWidgets.QWidget()
        self.tab_process.setObjectName("tab_process")
        self.widget = QtWidgets.QWidget(self.tab_process)
        self.widget.setGeometry(QtCore.QRect(10, 10, 753, 488))
        self.widget.setObjectName("widget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_4.setMinimumSize(QtCore.QSize(371, 217))
        self.groupBox_4.setObjectName("groupBox_4")
        self.pushButtoncheck = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButtoncheck.setGeometry(QtCore.QRect(130, 150, 101, 51))
        self.pushButtoncheck.setMinimumSize(QtCore.QSize(101, 51))
        self.pushButtoncheck.setStyleSheet("QPushButton{  \n"
"    border: 1px solid #ffffff;    \n"
"    background-color:#62d8fe;\n"
"    border-style: solid;  \n"
"    border-radius:5px;  \n"
"    width: 100px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"} \n"
"QPushButton:hover{     \n"
"    border: 1px solid #ffffff;  \n"
"    background-color:#d6f7fe;\n"
"    border-style: solid;  \n"
"    border-radius:5px;  \n"
"    width: 40px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"}\n"
"QPushButton:pressed{  \n"
"    background-color:#EAF0FF;  \n"
"    border: 1px solid #AAB4C4;  \n"
"    width: 40px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"    border-radius:5px;  \n"
"}")
        self.pushButtoncheck.setObjectName("pushButtoncheck")
        self.widget1 = QtWidgets.QWidget(self.groupBox_4)
        self.widget1.setGeometry(QtCore.QRect(50, 30, 248, 78))
        self.widget1.setObjectName("widget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_3.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 0, 0, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_2.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 0, 1, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.widget1)
        self.checkBox.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(371, 261))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_info_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_info_2.setGeometry(QtCore.QRect(10, 30, 341, 151))
        self.textEdit_info_2.setObjectName("textEdit_info_2")
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_8.setMinimumSize(QtCore.QSize(372, 481))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label = QtWidgets.QLabel(self.groupBox_8)
        self.label.setGeometry(QtCore.QRect(30, 30, 81, 41))
        self.label.setMinimumSize(QtCore.QSize(81, 41))
        self.label.setObjectName("label")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 40, 171, 30))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    font-family: \"微软雅黑\";\n"
"    color: black;\n"
"    border: 1px #1a1a1a solid;\n"
"    background-color:#62d8fe;\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.widget2 = QtWidgets.QWidget(self.groupBox_8)
        self.widget2.setGeometry(QtCore.QRect(10, 120, 348, 348))
        self.widget2.setObjectName("widget2")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setMinimumSize(QtCore.QSize(170, 170))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget2)
        self.label_3.setMinimumSize(QtCore.QSize(170, 170))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget2)
        self.label_4.setMinimumSize(QtCore.QSize(170, 170))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_5.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget2)
        self.label_5.setMinimumSize(QtCore.QSize(170, 170))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 1, 1, 1, 1)
        self.horizontalLayout_5.addWidget(self.groupBox_8)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("source/edit_image_128px_1169761_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_process, icon1, "")
        self.tab_extract = QtWidgets.QWidget()
        self.tab_extract.setObjectName("tab_extract")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_extract)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.tab_extract)
        self.groupBox_6.setMinimumSize(QtCore.QSize(301, 481))
        self.groupBox_6.setObjectName("groupBox_6")
        self.checkBox_FD = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_FD.setGeometry(QtCore.QRect(40, 270, 111, 16))
        self.checkBox_FD.setObjectName("checkBox_FD")
        self.checkBox_Harris = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_Harris.setGeometry(QtCore.QRect(40, 78, 111, 16))
        self.checkBox_Harris.setObjectName("checkBox_Harris")
        self.checkBox_GLCM = QtWidgets.QCheckBox(self.groupBox_6)
        self.checkBox_GLCM.setGeometry(QtCore.QRect(40, 174, 111, 16))
        self.checkBox_GLCM.setObjectName("checkBox_GLCM")
        self.horizontalLayout_3.addWidget(self.groupBox_6)
        self.extract = QtWidgets.QPushButton(self.tab_extract)
        self.extract.setMinimumSize(QtCore.QSize(101, 51))
        self.extract.setStyleSheet("QPushButton{  \n"
"    border: 1px solid #ffffff;    \n"
"    background-color:#62d8fe;\n"
"    border-style: solid;  \n"
"    border-radius:5px;  \n"
"    width: 100px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"} \n"
"QPushButton:hover{     \n"
"    border: 1px solid #ffffff;  \n"
"    background-color:#d6f7fe;\n"
"    border-style: solid;  \n"
"    border-radius:5px;  \n"
"    width: 40px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"}\n"
"QPushButton:pressed{  \n"
"    background-color:#EAF0FF;  \n"
"    border: 1px solid #AAB4C4;  \n"
"    width: 40px;  \n"
"    height:20px;  \n"
"    padding:0 0px;  \n"
"    border-radius:5px;  \n"
"}")
        self.extract.setObjectName("extract")
        self.horizontalLayout_3.addWidget(self.extract)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_extract)
        self.groupBox_7.setMinimumSize(QtCore.QSize(331, 481))
        self.groupBox_7.setObjectName("groupBox_7")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit.setGeometry(QtCore.QRect(20, 40, 291, 221))
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_3.addWidget(self.groupBox_7)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 2)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("source/image_128px_1197371_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_extract, icon2, "")
        self.tab_recognize = QtWidgets.QWidget()
        self.tab_recognize.setObjectName("tab_recognize")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("source/detective_128px_1168533_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_recognize, icon3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
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
        self.comboBox.setCurrentText(_translate("MainWindow", "暂无"))
        self.comboBox.setItemText(0, _translate("MainWindow", "暂无"))
        self.label_show.setText(_translate("MainWindow", "暂无图片"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "原图"))
        self.label_show_gray.setText(_translate("MainWindow", "暂无图片"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "灰度图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), _translate("MainWindow", "载入数据"))
        self.groupBox_4.setTitle(_translate("MainWindow", "数据扩充"))
        self.pushButtoncheck.setText(_translate("MainWindow", "确定"))
        self.checkBox_3.setText(_translate("MainWindow", "旋转变换"))
        self.checkBox_2.setText(_translate("MainWindow", "尺度变换"))
        self.checkBox.setText(_translate("MainWindow", "随机裁剪"))
        self.groupBox_5.setTitle(_translate("MainWindow", "信息显示"))
        self.textEdit_info_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">暂无</p></body></html>"))
        self.groupBox_8.setTitle(_translate("MainWindow", "预览"))
        self.label.setText(_translate("MainWindow", "扩充方式："))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "请选择"))
        self.label_2.setText(_translate("MainWindow", "暂无"))
        self.label_3.setText(_translate("MainWindow", "暂无"))
        self.label_4.setText(_translate("MainWindow", "暂无"))
        self.label_5.setText(_translate("MainWindow", "暂无"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_process), _translate("MainWindow", "预处理"))
        self.groupBox_6.setTitle(_translate("MainWindow", "特征选择"))
        self.checkBox_FD.setText(_translate("MainWindow", "FD形状特征"))
        self.checkBox_Harris.setText(_translate("MainWindow", "Harris角点特征"))
        self.checkBox_GLCM.setText(_translate("MainWindow", "GLCM纹理特征"))
        self.extract.setText(_translate("MainWindow", "提取特征"))
        self.groupBox_7.setTitle(_translate("MainWindow", "特征信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_extract), _translate("MainWindow", "特征提取"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_recognize), _translate("MainWindow", "训练与识别"))
