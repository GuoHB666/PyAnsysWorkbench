import sys
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QApplication

class PyAnsysUI:
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("py_ansys_ui.ui")

if __name__ == "__main__":
    App = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
    py_ansys_ui = PyAnsysUI()
    py_ansys_ui.ui.show()               # 显示主窗体
    sys.exit(App.exec())   # 循环中等待退出程序

