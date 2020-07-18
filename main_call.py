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
from imageAlgorithm.image_featureExtract import *
from imageAlgorithm.fusionRecognition import *


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

        self.filePath = ''
        self.targetFilePath = ''
        self.gray_dir = ''
        self.process_dir = ''
        self.process_gray_dir = ''
        self.fileList = []
        self.label_show_list = []
        self.label_gray_list = []
        # 提取的几个特征的文件路径数组
        self.featureDir = []
        self.featureImagesDir = ''
        self.featureFile = 'E:\GitHub\pyQtTest\ImagesDataset'

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
        # 特征提取 特征选择 多选框
        self.ui.checkBox_GLCM.stateChanged.connect(lambda: self.extractMethods(self.ui.checkBox_GLCM))
        self.ui.checkBox_FD.stateChanged.connect(lambda: self.extractMethods(self.ui.checkBox_FD))
        self.ui.checkBox_Harris.stateChanged.connect(lambda: self.extractMethods(self.ui.checkBox_Harris))
        # 特征提取 提取特征 按钮
        self.ui.extract.clicked.connect(self.extractFeature)
        # 特征提取 下拉框选择 显示图像
        self.ui.comboBox_4.currentIndexChanged.connect(self.changeExtractImage)
        self.ui.comboBox_5.currentIndexChanged.connect(self.changeExtractImage)
        # 训练与识别 训练前 划分方式 微调框
        # self.ui.spinBox.valueChanged.connect(self.changeValue)
        # self.ui.spinBox_2.valueChanged.connect(self.changeValue)
        # 训练与识别 训练前 下拉框 融合方式
        # self.ui.comboBox_6.currentIndexChanged.connect(self.changeFusion)
        # 训练与识别 训练前 确定按钮
        self.ui.recognizeButton.clicked.connect(self.recognizeMain)

    def openFile(self):
        # 打开文件夹
        filePath = QFileDialog.getExistingDirectory(self, "打开文件夹", "/", )
        self.filePath = filePath
        self.ui.textEdit_info.setText("选择数据集文件夹名称：" + filePath)
        # 读取该文件夹下的所有文件
        self.fileList = os.listdir(filePath)
        #  下拉框中显示文件夹下所有图片
        fileLength = len(self.fileList)
        self.ui.textEdit_info.append('\n'+'数据集文件夹中图片个数：'+ str(fileLength))
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
        boxes = []
        if self.filePath:
            self.ui.textEdit_info_2.append("已载入数据，文件路径："+self.filePath)
            # 获取多选框中的选项
            checkBoxes = [self.ui.checkBox_rotate, self.ui.checkBox_scale, self.ui.checkBox_random]
            self.ui.textEdit_info_2.append("最终确定扩充方式：")
            # 信息显示 并将 扩充方式 添加进下拉框
            # 添加新的item
            for i in range(len(self.fileList)):
                self.ui.comboBox_3.addItem(self.fileList[i])
            for box in checkBoxes:
                if box.isChecked():
                    self.ui.comboBox_2.addItem(box.text())
                    self.ui.textEdit_info_2.append(box.text())
                    boxes.append(box.text())
            for box in boxes:
                # 扩充处理
                if box == "随机裁剪":
                    processResults = defined_crop(self.filePath)
                elif box == "尺度变换":
                    processResults = scale_augmentation(self.filePath)
                else:
                    # 旋转变换
                    processResults = random_rotation(self.filePath)
                self.process_dir = processResults[0]
                augument_results = processResults[1]
                self.ui.textEdit_info_2.append('\n' + box + '扩充图像文件夹：' + self.process_dir)
                self.ui.textEdit_info_2.append('\n' + augument_results)
            # 默认显示
            self.label_show_list = [self.ui.label_show_one, self.ui.label_show_two, self.ui.label_show_three,
                                    self.ui.label_show_four]
            self.label_gray_list = [self.ui.label_gray_one, self.ui.label_gray_two, self.ui.label_gray_three,
                                    self.ui.label_gray_four]
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
        # 预处理 下拉框切换
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

    def extractMethods(self, checkBox):
        # 特征提取 特征选择
        if checkBox.isChecked():
            self.ui.textEdit_info_3.append("已选择：" + checkBox.text())
        else:
            self.ui.textEdit_info_3.append("取消选择：" + checkBox.text())

    def extractFeature(self):
        if os.path.exists(self.featureFile):
            pass
        else:
            os.mkdir(self.featureFile)
        features = []
        if self.process_dir and self.filePath:
            self.ui.textEdit_info_3.append("已载入数据，文件路径："+self.filePath)
            # 获取多选框中的选项
            checkBoxes = [self.ui.checkBox_GLCM, self.ui.checkBox_FD, self.ui.checkBox_Harris]
            self.ui.textEdit_info_3.append("最终确定扩充方式：")
            # 添加新的item
            for i in range(len(self.fileList)):
                self.ui.comboBox_4.addItem(self.fileList[i])
            for box in checkBoxes:
                if box.isChecked():
                    self.ui.comboBox_5.addItem(box.text())
                    self.ui.textEdit_info_3.append(box.text())
                    features.append(box.text())
            for feature in features:
                # 特征选择
                if feature == "GLCM纹理特征":
                    featureResults = glcm_feature(self.process_dir)
                elif feature == "FD形状特征":
                    featureResults = fourier_descriptor_feature(self.process_dir)
                    self.featureImagesDir = draw_contour(self.filePath)
                else:
                    # Harris角点特征
                    featureResults = harris_feature(self.process_dir)
                    self.featureImagesDir = draw_corner(self.filePath)
                featurePath = featureResults[0]
                self.featureDir.append(featurePath)
                featureState = featureResults[1]
                self.ui.textEdit_info_3.append('\n' + feature + '所在文件：' + featurePath)
                self.ui.textEdit_info_3.append('\n' + featureState)
                line = 1
                with open(featurePath) as file_obj:
                    for content in file_obj:
                        if line <= 5:
                            line += 1
                            self.ui.textEdit_info_3.append('\n' + content)
                        else:
                            break
        else:
            self.ui.textEdit_info_3.append("未载入数据，请至载入数据模块")

    def changeExtractImage(self):
        # 特征提取 预览 下拉框切换
        selectedImage = self.ui.comboBox_4.currentText()
        selectedFeature = self.ui.comboBox_5.currentText()
        if selectedFeature == '请选择' or selectedImage == '请选择'or selectedFeature == 'GLCM纹理特征':
            self.ui.label_extract_origin.setText('暂无')
            self.ui.label_extract_gray.setText('暂无')
        else:
            # 显示
            self.ui.label_extract_origin.setPixmap(QPixmap(self.filePath+'/'+selectedImage))
            self.ui.label_extract_gray.setPixmap(QPixmap(self.featureImagesDir+'/'+selectedImage))

    def changeValue(self):
        # 训练与识别 划分方式 微调框
        if self.ui.spinBox.value() & self.ui.spinBox_2.value():
            self.ui.textEdit_info_4.append('已选择划分方式：'+str(self.ui.spinBox.value())+'次'+str(self.ui.spinBox_2.value())
                                         + '折交叉验证')
        else:
            self.ui.textEdit_info_4.append('请重新输入划分方式！')

    def changeFusion(self):
        # 训练与识别 融合方式 下拉框
        selectedFusion = self.ui.comboBox_6.currentText()
        if selectedFusion == '请选择':
           pass
        else:
            self.ui.textEdit_info_4.append('已选择融合方式：' + selectedFusion)

    def recognizeMain(self):
        textEdit = self.ui.textEdit_info_4
        num = self.ui.spinBox.value()
        fold = self.ui.spinBox_2.value()
        fusionWay = self.ui.comboBox_6.currentText()
        fileDir = []
        target_file = self.featureFile + '\\target.txt'
        if os.listdir(self.featureFile):
            if num == 0 or fold == 0:
                textEdit.append('请重新输入划分方式！')
            elif fusionWay == '请选择':
                textEdit.append('请重新选择融合方式！')
            else:
                textEdit.append('已选择划分方式：' + str(num) + '次' + str(fold) + '折交叉验证')
                textEdit.append('已选择融合方式：' + fusionWay)
                if os.path.isfile(self.featureFile+'\\feature_Harris.txt'):
                    textEdit.append('特征数据' +self.featureFile+'\\feature_Harris.txt')
                    fileDir.append(self.featureFile+'\\feature_Harris.txt')
                    flag_1 = 1
                else:
                    flag_1 = 0
                if os.path.isfile(self.featureFile+'\\feature_GLCM.txt'):
                    textEdit.append('特征数据' + self.featureFile + '\\feature_GLCM.txt')
                    fileDir.append(self.featureFile+'\\feature_GLCM.txt')
                    flag_2 = 1
                else:
                    flag_2 = 0
                if os.path.isfile(self.featureFile+'\\feature_FD.txt'):
                    textEdit.append('特征数据' + self.featureFile + '\\feature_FD.txt')
                    flag_3 = 1
                    fileDir.append(self.featureFile + '\\feature_FD.txt')
                else:
                    flag_3 = 0
                if flag_1 or flag_2 or flag_3:
                    if fusionWay == '多特征串行融合':
                        if fold < 2:
                            textEdit.append('必须在2以上，请重新输入！')
                        else:
                            value_linear, value_rbf, value_poly, value_sigmod, value_KNN, value_MLP, value_DT = fearureSerialFusin(num, fold, fileDir, target_file)
                            self.ui.lineEdit_linear.setText(str(value_linear))
                            self.ui.lineEdit_rbf.setText(str(value_rbf))
                            self.ui.lineEdit_poly.setText(str(value_poly))
                            self.ui.lineEdit_sigmod.setText(str(value_sigmod))
                            self.ui.lineEdit_KNN.setText(str(value_KNN))
                            self.ui.lineEdit_MLP.setText(str(value_MLP))
                            self.ui.lineEdit_DT.setText(str(value_DT))
                            self.ui.lineEdit_precomputed.setText(str('-----'))
                    else:
                        textEdit.append('自适应加权融合目前还在调整中！敬请期待！')
                else:
                    textEdit.append('特征集为空！请至载入数据模块重新载入数据！')
        else:
            textEdit.append('特征集为空！请至载入数据模块重新载入数据！')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = HelloLogin()
    widget.show()
    sys.exit(app.exec_())