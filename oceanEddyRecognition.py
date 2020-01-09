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
        self.image_preshow.setGeometry(QtCore.QRect(10, 30, 121, 30))
        self.image_preshow.setObjectName("image_preshow")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(130, 30, 171, 30))
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
        self.label_show.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_show.setScaledContents(True)
        self.label_show.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show.setObjectName("label_show")
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_show_gray = QtWidgets.QLabel(self.tab_2)
        self.label_show_gray.setGeometry(QtCore.QRect(0, 0, 351, 351))
        self.label_show_gray.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_show_gray.setScaledContents(True)
        self.label_show_gray.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_gray.setObjectName("label_show_gray")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/lenovo/.designer/backup/source/folder_opened_128px_1222856_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_file, icon, "")
        self.tab_process = QtWidgets.QWidget()
        self.tab_process.setObjectName("tab_process")
        self.layoutWidget = QtWidgets.QWidget(self.tab_process)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 753, 488))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget)
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
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 30, 248, 78))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkBox_rotate = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_rotate.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_rotate.setObjectName("checkBox_rotate")
        self.gridLayout_3.addWidget(self.checkBox_rotate, 0, 0, 1, 1)
        self.checkBox_scale = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_scale.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_scale.setObjectName("checkBox_scale")
        self.gridLayout_3.addWidget(self.checkBox_scale, 0, 1, 1, 1)
        self.checkBox_random = QtWidgets.QCheckBox(self.layoutWidget1)
        self.checkBox_random.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_random.setObjectName("checkBox_random")
        self.gridLayout_3.addWidget(self.checkBox_random, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_5.setMinimumSize(QtCore.QSize(371, 261))
        self.groupBox_5.setObjectName("groupBox_5")
        self.textEdit_info_2 = QtWidgets.QTextEdit(self.groupBox_5)
        self.textEdit_info_2.setGeometry(QtCore.QRect(10, 30, 341, 151))
        self.textEdit_info_2.setObjectName("textEdit_info_2")
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_8.setMinimumSize(QtCore.QSize(372, 481))
        self.groupBox_8.setObjectName("groupBox_8")
        self.label_preshow_2 = QtWidgets.QLabel(self.groupBox_8)
        self.label_preshow_2.setGeometry(QtCore.QRect(10, 80, 121, 30))
        self.label_preshow_2.setMinimumSize(QtCore.QSize(121, 30))
        self.label_preshow_2.setObjectName("label_preshow_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_2.setGeometry(QtCore.QRect(130, 80, 171, 30))
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    font-family: \"微软雅黑\";\n"
"    color: black;\n"
"    border: 1px #1a1a1a solid;\n"
"    background-color:#62d8fe;\n"
"}\n"
"")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.tabWidget_3 = QtWidgets.QTabWidget(self.groupBox_8)
        self.tabWidget_3.setGeometry(QtCore.QRect(10, 130, 351, 351))
        self.tabWidget_3.setObjectName("tabWidget_3")
        self.tab_origin = QtWidgets.QWidget()
        self.tab_origin.setObjectName("tab_origin")
        self.label_show_one = QtWidgets.QLabel(self.tab_origin)
        self.label_show_one.setGeometry(QtCore.QRect(180, 170, 171, 151))
        self.label_show_one.setStyleSheet("QLabel{border: 1px solid  rgb(213, 223, 229);}")
        self.label_show_one.setScaledContents(True)
        self.label_show_one.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_one.setObjectName("label_show_one")
        self.label_show_two = QtWidgets.QLabel(self.tab_origin)
        self.label_show_two.setGeometry(QtCore.QRect(0, 0, 171, 151))
        self.label_show_two.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_show_two.setScaledContents(True)
        self.label_show_two.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_two.setObjectName("label_show_two")
        self.label_show_three = QtWidgets.QLabel(self.tab_origin)
        self.label_show_three.setGeometry(QtCore.QRect(0, 170, 171, 151))
        self.label_show_three.setStyleSheet("QLabel{\n"
"    border: 1px solid  rgb(213, 223, 229);\n"
"}")
        self.label_show_three.setScaledContents(True)
        self.label_show_three.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_three.setObjectName("label_show_three")
        self.label_show_four = QtWidgets.QLabel(self.tab_origin)
        self.label_show_four.setGeometry(QtCore.QRect(180, 0, 171, 151))
        self.label_show_four.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_show_four.setScaledContents(True)
        self.label_show_four.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_four.setObjectName("label_show_four")
        self.tabWidget_3.addTab(self.tab_origin, "")
        self.tab_gray = QtWidgets.QWidget()
        self.tab_gray.setObjectName("tab_gray")
        self.label_gray_one = QtWidgets.QLabel(self.tab_gray)
        self.label_gray_one.setGeometry(QtCore.QRect(0, 0, 171, 151))
        self.label_gray_one.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_gray_one.setScaledContents(True)
        self.label_gray_one.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gray_one.setObjectName("label_gray_one")
        self.label_gray_two = QtWidgets.QLabel(self.tab_gray)
        self.label_gray_two.setGeometry(QtCore.QRect(180, 0, 171, 151))
        self.label_gray_two.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_gray_two.setScaledContents(True)
        self.label_gray_two.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gray_two.setObjectName("label_gray_two")
        self.label_gray_three = QtWidgets.QLabel(self.tab_gray)
        self.label_gray_three.setGeometry(QtCore.QRect(0, 170, 171, 151))
        self.label_gray_three.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_gray_three.setScaledContents(True)
        self.label_gray_three.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gray_three.setObjectName("label_gray_three")
        self.label_gray_four = QtWidgets.QLabel(self.tab_gray)
        self.label_gray_four.setGeometry(QtCore.QRect(180, 170, 171, 151))
        self.label_gray_four.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_gray_four.setScaledContents(True)
        self.label_gray_four.setAlignment(QtCore.Qt.AlignCenter)
        self.label_gray_four.setObjectName("label_gray_four")
        self.tabWidget_3.addTab(self.tab_gray, "")
        self.label_preshow_1 = QtWidgets.QLabel(self.groupBox_8)
        self.label_preshow_1.setGeometry(QtCore.QRect(10, 30, 121, 30))
        self.label_preshow_1.setObjectName("label_preshow_1")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_8)
        self.comboBox_3.setGeometry(QtCore.QRect(130, 30, 171, 30))
        self.comboBox_3.setStyleSheet("QComboBox {\n"
"    font-family: \"微软雅黑\";\n"
"    color: black;\n"
"    border: 1px #1a1a1a solid;\n"
"    background-color:#62d8fe;\n"
"}\n"
"")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.tabWidget_3.raise_()
        self.label_preshow_2.raise_()
        self.comboBox_2.raise_()
        self.label_preshow_1.raise_()
        self.comboBox_3.raise_()
        self.horizontalLayout_5.addWidget(self.groupBox_8)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/lenovo/.designer/backup/source/edit_image_128px_1169761_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_process, icon1, "")
        self.tab_extract = QtWidgets.QWidget()
        self.tab_extract.setObjectName("tab_extract")
        self.layoutWidget2 = QtWidgets.QWidget(self.tab_extract)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 752, 488))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_6 = QtWidgets.QGroupBox(self.layoutWidget2)
        self.groupBox_6.setMinimumSize(QtCore.QSize(371, 217))
        self.groupBox_6.setObjectName("groupBox_6")
        self.extract = QtWidgets.QPushButton(self.groupBox_6)
        self.extract.setGeometry(QtCore.QRect(130, 150, 107, 51))
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
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_6)
        self.layoutWidget3.setGeometry(QtCore.QRect(50, 30, 248, 78))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.checkBox_Harris = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_Harris.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_Harris.setObjectName("checkBox_Harris")
        self.gridLayout_5.addWidget(self.checkBox_Harris, 0, 0, 1, 1)
        self.checkBox_FD = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_FD.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_FD.setObjectName("checkBox_FD")
        self.gridLayout_5.addWidget(self.checkBox_FD, 0, 1, 1, 1)
        self.checkBox_GLCM = QtWidgets.QCheckBox(self.layoutWidget3)
        self.checkBox_GLCM.setMinimumSize(QtCore.QSize(120, 35))
        self.checkBox_GLCM.setObjectName("checkBox_GLCM")
        self.gridLayout_5.addWidget(self.checkBox_GLCM, 1, 0, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        self.groupBox_7 = QtWidgets.QGroupBox(self.layoutWidget2)
        self.groupBox_7.setMinimumSize(QtCore.QSize(331, 261))
        self.groupBox_7.setObjectName("groupBox_7")
        self.textEdit_info_3 = QtWidgets.QTextEdit(self.groupBox_7)
        self.textEdit_info_3.setGeometry(QtCore.QRect(10, 30, 341, 151))
        self.textEdit_info_3.setObjectName("textEdit_info_3")
        self.verticalLayout_3.addWidget(self.groupBox_7)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.groupBox_9 = QtWidgets.QGroupBox(self.layoutWidget2)
        self.groupBox_9.setMinimumSize(QtCore.QSize(371, 486))
        self.groupBox_9.setObjectName("groupBox_9")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_4.setGeometry(QtCore.QRect(130, 30, 171, 30))
        self.comboBox_4.setStyleSheet("QComboBox {\n"
"    font-family: \"微软雅黑\";\n"
"    color: black;\n"
"    border: 1px #1a1a1a solid;\n"
"    background-color:#62d8fe;\n"
"}\n"
"")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.label_extract_show_1 = QtWidgets.QLabel(self.groupBox_9)
        self.label_extract_show_1.setGeometry(QtCore.QRect(10, 30, 121, 30))
        self.label_extract_show_1.setObjectName("label_extract_show_1")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_9)
        self.comboBox_5.setGeometry(QtCore.QRect(130, 80, 171, 30))
        self.comboBox_5.setStyleSheet("QComboBox {\n"
"    font-family: \"微软雅黑\";\n"
"    color: black;\n"
"    border: 1px #1a1a1a solid;\n"
"    background-color:#62d8fe;\n"
"}\n"
"")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.label_extract_show_2 = QtWidgets.QLabel(self.groupBox_9)
        self.label_extract_show_2.setGeometry(QtCore.QRect(10, 80, 121, 30))
        self.label_extract_show_2.setMinimumSize(QtCore.QSize(121, 30))
        self.label_extract_show_2.setObjectName("label_extract_show_2")
        self.tabWidget_4 = QtWidgets.QTabWidget(self.groupBox_9)
        self.tabWidget_4.setGeometry(QtCore.QRect(10, 130, 351, 351))
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_origin_2 = QtWidgets.QWidget()
        self.tab_origin_2.setObjectName("tab_origin_2")
        self.label_extract_origin = QtWidgets.QLabel(self.tab_origin_2)
        self.label_extract_origin.setGeometry(QtCore.QRect(0, 0, 351, 321))
        self.label_extract_origin.setMinimumSize(QtCore.QSize(351, 300))
        self.label_extract_origin.setMaximumSize(QtCore.QSize(351, 351))
        self.label_extract_origin.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_extract_origin.setScaledContents(True)
        self.label_extract_origin.setAlignment(QtCore.Qt.AlignCenter)
        self.label_extract_origin.setObjectName("label_extract_origin")
        self.tabWidget_4.addTab(self.tab_origin_2, "")
        self.tab_gray_2 = QtWidgets.QWidget()
        self.tab_gray_2.setObjectName("tab_gray_2")
        self.label_extract_gray = QtWidgets.QLabel(self.tab_gray_2)
        self.label_extract_gray.setGeometry(QtCore.QRect(0, 0, 351, 321))
        self.label_extract_gray.setMinimumSize(QtCore.QSize(351, 300))
        self.label_extract_gray.setMaximumSize(QtCore.QSize(351, 351))
        self.label_extract_gray.setStyleSheet("QLabel{\n"
"    border: 1px solid rgb(213, 223, 229);\n"
"}")
        self.label_extract_gray.setScaledContents(True)
        self.label_extract_gray.setAlignment(QtCore.Qt.AlignCenter)
        self.label_extract_gray.setObjectName("label_extract_gray")
        self.tabWidget_4.addTab(self.tab_gray_2, "")
        self.horizontalLayout_2.addWidget(self.groupBox_9)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/lenovo/.designer/backup/source/image_128px_1197371_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_extract, icon2, "")
        self.tab_recognize = QtWidgets.QWidget()
        self.tab_recognize.setObjectName("tab_recognize")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/lenovo/.designer/backup/source/detective_128px_1168533_easyicon.net.ico"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.tabWidget.addTab(self.tab_recognize, icon3, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "选择文件夹"))
        self.open_file.setText(_translate("MainWindow", "浏览文件夹"))
        self.groupBox_2.setTitle(_translate("MainWindow", "信息显示"))
        self.textEdit_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">选择文件夹名称：</p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "预览"))
        self.image_preshow.setText(_translate("MainWindow", "选择预览的图片："))
        self.comboBox.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox.setItemText(0, _translate("MainWindow", "请选择"))
        self.label_show.setText(_translate("MainWindow", "暂无"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "原图"))
        self.label_show_gray.setText(_translate("MainWindow", "暂无"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "灰度图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_file), _translate("MainWindow", "载入数据"))
        self.groupBox_4.setTitle(_translate("MainWindow", "数据扩充"))
        self.pushButtoncheck.setText(_translate("MainWindow", "确定"))
        self.checkBox_rotate.setText(_translate("MainWindow", "旋转变换"))
        self.checkBox_scale.setText(_translate("MainWindow", "尺度变换"))
        self.checkBox_random.setText(_translate("MainWindow", "随机裁剪"))
        self.groupBox_5.setTitle(_translate("MainWindow", "信息显示"))
        self.textEdit_info_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.groupBox_8.setTitle(_translate("MainWindow", "预览"))
        self.label_preshow_2.setText(_translate("MainWindow", "扩充方式："))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "请选择"))
        self.label_show_one.setText(_translate("MainWindow", "暂无"))
        self.label_show_two.setText(_translate("MainWindow", "暂无"))
        self.label_show_three.setText(_translate("MainWindow", "暂无"))
        self.label_show_four.setText(_translate("MainWindow", "暂无"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_origin), _translate("MainWindow", "原图"))
        self.label_gray_one.setText(_translate("MainWindow", "暂无"))
        self.label_gray_two.setText(_translate("MainWindow", "暂无"))
        self.label_gray_three.setText(_translate("MainWindow", "暂无"))
        self.label_gray_four.setText(_translate("MainWindow", "暂无"))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_gray), _translate("MainWindow", "灰度图"))
        self.label_preshow_1.setText(_translate("MainWindow", "选择预览的图片："))
        self.comboBox_3.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "请选择"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_process), _translate("MainWindow", "预处理"))
        self.groupBox_6.setTitle(_translate("MainWindow", "特征选择"))
        self.extract.setText(_translate("MainWindow", "提取特征"))
        self.checkBox_Harris.setText(_translate("MainWindow", "Harris角点特征"))
        self.checkBox_FD.setText(_translate("MainWindow", "FD形状特征"))
        self.checkBox_GLCM.setText(_translate("MainWindow", "GLCM纹理特征"))
        self.groupBox_7.setTitle(_translate("MainWindow", "特征信息"))
        self.groupBox_9.setTitle(_translate("MainWindow", "预览"))
        self.comboBox_4.setCurrentText(_translate("MainWindow", "请选择"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "请选择"))
        self.label_extract_show_1.setText(_translate("MainWindow", "选择预览的图片："))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "请选择"))
        self.label_extract_show_2.setText(_translate("MainWindow", "选择预览的特征："))
        self.label_extract_origin.setText(_translate("MainWindow", "暂无"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_origin_2), _translate("MainWindow", "原图"))
        self.label_extract_gray.setText(_translate("MainWindow", "暂无"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_gray_2), _translate("MainWindow", "灰度图"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_extract), _translate("MainWindow", "特征提取"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_recognize), _translate("MainWindow", "训练与识别"))
