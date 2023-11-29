import sys
from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QApplication

class PyAnsysUI:
    def __init__(self):
        # 从文件中加载UI定义
        self.ui = uic.loadUi("py_ansys_ui.ui")
        # 获取树形节点所有名称
        self.tree_names = []
        self._get_tree_nodenames()
        # 事件连接
        self.signal_connect_slot()
    def signal_connect_slot(self):
        """信号与槽"""
        # QTreeWidget 的点击事件
        self.ui.tree.clicked.connect(self.tree_on_clicked)
    def _get_rawtree_names(self, item):
        self.tree_names.append(item.text(0))
        for i in range(item.childCount()):
            child_item = item.child(i)
            self._get_rawtree_names(child_item)
    def _get_tree_nodenames(self):
        self._get_rawtree_names(self.ui.tree.invisibleRootItem())
        index_to_remove = [0,1,6,11] # 定义需要删除的，有子节点的父节点名称索引
        index_to_remove.sort(reverse=True)  # 将索引按照倒序排列，使得从后往前删除，避免索引错位
        for index in index_to_remove:
            self.tree_names.pop(index)
        # print(self.tree_names)
    def tree_on_clicked(self):
        try:
            tree_name = self.ui.tree.currentItem()  # 获取当前点击的树形节点名称
            page_num = self.tree_names.index(tree_name.text(0))
            self.ui.pages.setCurrentIndex(page_num)
        except:
            pass
if __name__ == "__main__":
    App = QApplication(sys.argv)    # 创建QApplication对象，作为GUI主程序入口
    py_ansys_ui = PyAnsysUI()
    py_ansys_ui.ui.show()               # 显示主窗体
    sys.exit(App.exec())   # 循环中等待退出程序

