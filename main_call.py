# 这里主要是用来写业务逻辑

from PyQt5 import QtCore, QtGui, QtWidgets
from login import Ui_widget


class HelloLogin(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_widget()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        # 给登录按钮 的 点击动作绑定一个事件处理函数

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
            print(self.ui.LineEdit.text())
            if self.ui.LineEdit.text() == i["name"] and self.ui.LineEdit.text() == i["password"]:
                isLogin = True
                try:
                    self.ui.text.setText("登录成功")
                except:
                    self.ui.text.setText("登录失败")
        if isLogin == False :
            self.ui.text.setText("请重新输入")
        # print("hello")
        # self.ui.text.setText("登录成功")


if __name__ == "__main__":
    import sys
    from PyQt5.QtGui import QIcon

    app = QtWidgets.QApplication(sys.argv)

    widget = HelloLogin()
    # widget = QtWidgets.QWidget()
    # ui = Ui_widget()
    # ui.setupUi(widget)

    widget.setWindowIcon(QIcon('logo.jpg'))  # 增加icon图标，如果没有图片可以没有这句
    widget.show()
    sys.exit(app.exec_())