# 这里主要是用来写业务逻辑
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_widget
from oceanEddyRecognition import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QImage
from PyQt5.QtCore import Qt
import cv2
from imageAlgorithm.image_gray import *
from imageAlgorithm.image_preprocess import *


class HelloLogin(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        # super(HelloLogin, self).__init__()
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('E:/GitHub/pyQtTest/logo_2.png'))
        self.setWindowTitle('登录')

        palette = QPalette()
        # 设置背景颜色
        # palette.setColor(QPalette.Background, Qt.blue)
        # 设置背景图片
        palette.setBrush(QPalette.Background, QBrush(QPixmap('E:/GitHub/pyQtTest/login_bg.jpg')))
        self.setPalette(palette)

        # 给登录按钮 的 点击动作绑定一个事件处理函数
        self.ui.pushButton.clicked.connect(self.login)
    #     重置 按钮
        self.ui.pushButton_2.clicked.connect(self.reSet)

    def login(self):
        user = [
            {
                "name": "admin",
                "password": "admin"
            }, {
                "name": "jiajia",
                "password": "jiajia"
            }
        ]
        isLogin = False
        for i in user:
            if self.ui.LineEdit.text().lower() == i["name"] and self.ui.LineEdit.text().lower() == i["password"]:
                isLogin = True
                try:
                    self.ui.Label_3.setText("登录成功")
                    self.hide()
                    self.child = MainWindow()
                    self.child.show()
                except:
                    self.ui.Label_3.setText("登录失败")
        if isLogin == False :
            self.ui.Label_3.setText("请重新输入")

    def reSet(self):
        self.ui.LineEdit.clear()
        self.ui.LineEdit_2.clear()


# 新建MainWindow类
class MainWindow(QtWidgets.QMainWindow, HelloLogin):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('E:/GitHub/pyQtTest/logo_2.png'))
        self.setWindowTitle('海洋涡旋自动识别系统')

        # 定义一些该类的变量
        self.filePath = ''
        self.gray_dir = ''
        # self.processMethods = []

        paletteMain = QPalette()
        paletteMain.setBrush(QPalette.Background, QBrush(QPixmap('E:/GitHub/pyQtTest/login_bg.jpg')))
        self.setPalette(paletteMain)

        # 打开文件，选择图片
        self.ui.open_file.clicked.connect(self.openFile)
        # 下拉框选中时间
        self.ui.comboBox.currentIndexChanged.connect(self.changeImage)
        # 多选框 状态控制事件
        self.ui.checkBox_random.stateChanged.connect(lambda: self.augumentMethods(self.ui.checkBox_random))
        self.ui.checkBox_scale.stateChanged.connect(lambda: self.augumentMethods(self.ui.checkBox_scale))
        self.ui.checkBox_rotate.stateChanged.connect(lambda: self.augumentMethods(self.ui.checkBox_rotate))
        # 预处理 确定按钮
        self.ui.pushButtoncheck.clicked.connect(self.preProcess)

    def openFile(self):
        # 打开文件
        # filename, _ = QFileDialog.getOpenFileName(self, "打开文件", "/", "image Files (*.png *.tif *.jpg)")
        # self.ui.label_show.setPixmap(QPixmap(filename))
        # self.ui.textEdit_info.setText("选择文件夹名称："+filename)
        # 打开文件夹
        filePath = QFileDialog.getExistingDirectory(self, "打开文件夹", "/", )
        self.filePath = filePath
        self.ui.textEdit_info.setText("选择文件夹名称：" + filePath)
        # 读取该文件夹下的所有文件
        fileList = os.listdir(filePath)
        #  下拉框中显示文件夹下所有图片
        fileLength = len(fileList)
        self.ui.textEdit_info.append('\n'+'文件夹中图片个数：'+ str(fileLength))
        # 清空已有的comboBox里的所有item
        self.ui.comboBox.clear()
        # 添加新的item
        for i in range(fileLength):
            print(fileList[i])
            self.ui.comboBox.addItem(fileList[i])
        # 根据选中的图片在下方的label框中显示
        self.ui.label_show.setPixmap(QPixmap(filePath + '/' + fileList[0]))
        self.ui.textEdit_info.append('\n' + '灰度处理中。。。')
        # 将该文件夹下的所有图片转灰度存入文件夹中
        return_resluts = image_to_gray(self.filePath)
        self.gray_dir = return_resluts[0]
        gray_results = return_resluts[1]
        self.ui.textEdit_info.append('\n' + '灰度图像文件夹：'+self.gray_dir)
        self.ui.textEdit_info.append('\n'+gray_results)
        #  将灰度图像显示在label_show_gray框中
        self.ui.label_show_gray.setPixmap(QPixmap(self.gray_dir+'/'+fileList[0]))

    def changeImage(self):
        # 载入数据 下拉框切换
        selectedImage = self.ui.comboBox.currentText()
        self.ui.label_show.setPixmap(QPixmap(self.filePath+'/'+selectedImage))
        self.ui.label_show_gray.setPixmap(QPixmap(self.gray_dir + '/' + selectedImage))

    def augumentMethods(self, checkBox):
        print(checkBox.isChecked())
        if checkBox.isChecked():
            self.ui.textEdit_info_2.append("已选择："+ checkBox.text())
        else:
            self.ui.textEdit_info_2.append("取消选择：" + checkBox.text())

    def preProcess(self):
        if self.filePath:
            self.ui.textEdit_info_2.append("已载入数据，文件路径："+self.filePath)
            # 获取多选框中的选项
            checkBoxes = [self.ui.checkBox_rotate, self.ui.checkBox_scale, self.ui.checkBox_random]
            self.ui.textEdit_info_2.append("最终确定扩充方式：")
            # 信息显示 并将 扩充方式 添加进下拉框
            self.ui.comboBox_2.clear()
            for box in checkBoxes:
                if box.isChecked():
                    self.ui.textEdit_info_2.append(box.text())
                    # 扩充处理
                    if box.text() == "随机裁剪":
                        cropResults = defined_crop(self.filePath)
                    # elif box.text() == "尺度变换":
                    #     scaleResults = scale_augmentation(self.filePath)
                    # else:
                    #     # 旋转变换
                    #     rotateResults = random_rotation(self.filePath)
                    self.ui.comboBox_2.addItem(box.text())

        else:
            self.ui.textEdit_info_2.append("未载入数据，请至载入数据模块")


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QIcon

    app = QtWidgets.QApplication(sys.argv)
    widget = HelloLogin()
    widget.show()
    sys.exit(app.exec_())