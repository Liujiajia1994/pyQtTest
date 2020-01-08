# 这里主要是用来写业务逻辑
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets
from login import Ui_widget
from oceanEddyRecognition import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QIcon
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
        self.process_dir = ''
        self.process_gray_dir = ''
        self.fileList = []
        self.label_show_list = []
        self.label_gray_list = []

        paletteMain = QPalette()
        paletteMain.setBrush(QPalette.Background, QBrush(QPixmap('E:/GitHub/pyQtTest/login_bg.jpg')))
        self.setPalette(paletteMain)

        # 载入数据 浏览文件夹
        self.ui.open_file.clicked.connect(self.openFile)
        # 载入数据 选择预览的图片 下拉框状态变化事件
        self.ui.comboBox.currentIndexChanged.connect(self.changeImage)
        # 预处理 扩充方式 多选框 状态控制事件
        self.ui.checkBox_random.stateChanged.connect(lambda: self.augumentMethods(self.ui.checkBox_random))
        self.ui.checkBox_scale.stateChanged.connect(lambda: self.augumentMethods(self.ui.checkBox_scale))
        self.ui.checkBox_rotate.stateChanged.connect(lambda: self.augumentMethods(self.ui.checkBox_rotate))
        # 预处理 确定 按钮
        self.ui.pushButtoncheck.clicked.connect(self.preProcess)
        # 预处理 预览-扩充方式 下拉框状态变化事件
        self.ui.comboBox_2.currentIndexChanged.connect(self.changeProcessImage)
        # 预处理 预览-选择预览的图片 下拉框状态变化事件
        self.ui.comboBox_3.currentIndexChanged.connect(self.changeProcessImage)

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
        self.fileList = os.listdir(filePath)
        #  下拉框中显示文件夹下所有图片
        fileLength = len(self.fileList)
        self.ui.textEdit_info.append('\n'+'文件夹中图片个数：'+ str(fileLength))
        # 清空已有的comboBox里的所有item
        self.ui.comboBox.clear()
        # 添加新的item
        for i in range(fileLength):
            print(self.fileList[i])
            self.ui.comboBox.addItem(self.fileList[i])
        # 根据选中的图片在下方的label框中显示
        self.ui.label_show.setPixmap(QPixmap(filePath + '/' + self.fileList[0]))
        self.ui.textEdit_info.append('\n' + '灰度处理中。。。')
        # 将该文件夹下的所有图片转灰度存入文件夹中
        return_resluts = image_to_gray(self.filePath, 'E:/GitHub/pyQtTest/ImagesDataset/SAR_gray_images')
        self.gray_dir = return_resluts[0]
        gray_results = return_resluts[1]
        self.ui.textEdit_info.append('\n' + '灰度图像文件夹：'+self.gray_dir)
        self.ui.textEdit_info.append('\n'+gray_results)
        #  将灰度图像显示在label_show_gray框中
        self.ui.label_show_gray.setPixmap(QPixmap(self.gray_dir+'/'+self.fileList[0]))

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
            # 添加新的item
            # self.ui.comboBox_3.removeItem('请选择')
            for i in range(len(self.fileList)):
                self.ui.comboBox_3.addItem(self.fileList[i])
            for box in checkBoxes:
                if box.isChecked():
                    self.ui.comboBox_2.addItem(box.text())
                    self.ui.textEdit_info_2.append(box.text())
                    # 扩充处理
                    if box.text() == "随机裁剪":
                        cropResults = defined_crop(self.filePath)
                        self.process_dir = cropResults[0]
                        augument_results = cropResults[1]
                        self.ui.textEdit_info_2.append('\n' + '扩充图像文件夹：' + self.process_dir)
                        self.ui.textEdit_info_2.append('\n' + augument_results)
                    elif box.text() == "尺度变换":
                        scaleResults = scale_augmentation(self.filePath)
                        self.process_dir = scaleResults[0]
                        augument_results = scaleResults[1]
                        self.ui.textEdit_info_2.append('\n' + '扩充图像文件夹：' + self.process_dir)
                        self.ui.textEdit_info_2.append('\n' + augument_results)
                    else:
                        # 旋转变换
                        rotateResults = random_rotation(self.filePath)
                        self.process_dir = rotateResults[0]
                        augument_results = rotateResults[1]
                        self.ui.textEdit_info_2.append('\n' + '扩充图像文件夹：' + self.process_dir)
                        self.ui.textEdit_info_2.append('\n' + augument_results)
            # 默认显示
            self.label_show_list = [self.ui.label_show_one, self.ui.label_show_two, self.ui.label_show_three, self.ui.label_show_four]
            self.label_gray_list = [self.ui.label_gray_one, self.ui.label_gray_two, self.ui.label_gray_three, self.ui.label_gray_four]
            return_resluts = image_to_gray(self.process_dir,
                                           'E:/GitHub/pyQtTest/ImagesDataset/SAR_augument_gray_images')
            self.process_gray_dir = return_resluts[0]
            gray_results = return_resluts[1]
            self.ui.textEdit_info_2.append('\n' + '灰度扩充图像文件夹：' + self.process_gray_dir)
            self.ui.textEdit_info_2.append('\n' + gray_results)
            for i in range(4):
                selectedMethod = self.ui.comboBox_2.currentText()
                selectedImage = self.ui.comboBox_3.currentText()
                if selectedMethod == '请选择' or selectedImage == '请选择':
                    pass
                else:
                    imagePath = self.process_dir + '/' + os.listdir(self.process_dir)[i]
                    self.label_show_list[i].setPixmap(QPixmap(imagePath))
                    #  将灰度图像显示在label_show_gray框中
                    imageGrayPath = self.process_gray_dir + '/' + os.listdir(self.process_dir)[i]
                    self.label_gray_list[i].setPixmap(QPixmap(imageGrayPath))
        else:
            self.ui.textEdit_info_2.append("未载入数据，请至载入数据模块")

    def changeProcessImage(self):
        # 载入数据 下拉框切换
        selectedMethod = self.ui.comboBox_2.currentText()
        choose = ''
        if selectedMethod == '随机裁剪':
            choose = 'crop'
        elif selectedMethod == '尺度变换':
            choose = 'scale'
        elif selectedMethod == '旋转变换':
            choose = 'rotate'
        else:
            pass
        selectedImage = self.ui.comboBox_3.currentText()
        for i in range(4):
            if selectedImage == '请选择' or selectedMethod == '请选择':
                self.label_show_list[i].setText('暂无')
                self.label_gray_list[i].setText('暂无')
            else:
                path = '/' + selectedImage.split('.')[0]+'-'+choose+'-'+str(i+1)+'.tif'
                self.label_show_list[i].setPixmap(QPixmap(self.process_dir + path))
                self.label_gray_list[i].setPixmap(QPixmap(self.process_gray_dir + path))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = HelloLogin()
    widget.show()
    sys.exit(app.exec_())