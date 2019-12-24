# 打包命令：1、安装pyinstaller  2、pyinstaller -F -w main_call.py -i logo.ico -n main
# 环境：Python version 3.6.5
# 安装 PyQt5，pyQt5-tools
# 界面：Qt Designer；PyUIC
# 这里主要是用来写业务逻辑
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_widget
from oceanEddyRecognition import Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap, QPalette, QBrush


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


# 新建MainWindow类，继承生成的HelloLogin类
class MainWindow(QtWidgets.QMainWindow, HelloLogin):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        # super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('E:/GitHub/pyQtTest/logo_2.png'))
        self.setWindowTitle('海洋涡旋自动识别系统')

        paletteMain = QPalette()
        paletteMain.setBrush(QPalette.Background, QBrush(QPixmap('E:/GitHub/pyQtTest/ocean_1.jpg')))
        self.setPalette(paletteMain)

        #         打开文件，选择图片
        self.ui.open_file.clicked.connect(self.openFile)

    def openFile(self):
        filename, _ = QFileDialog.getOpenFileName(self, "打开文件", "/", "image Files (*.png *.tif *.jpg)")
        self.ui.label_show.setPixmap(QPixmap(filename))
        self.ui.textEdit_info.setText("选择文件夹名称："+filename)


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QIcon

    app = QtWidgets.QApplication(sys.argv)
    widget = HelloLogin()
    widget.show()
    sys.exit(app.exec_())