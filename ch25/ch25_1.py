# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication   # 手動加入
import sys                                              # 手動加入

# from .Ui_ch25_1 import Ui_MainWindow
# 將from .Ui_ch25_1 import Ui_MainWindow的.去掉
from Ui_ch25_1 import Ui_MainWindow                     # 手動加入


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget (defaults to None)
        @type QWidget (optional)
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.Counter = 0                    # 加入類別的屬性
    
    @pyqtSlot()
    def on_QPB_Add_clicked(self):           # 當按下"ADD (+1)"按鈕時要執行的方法
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Counter = self.Counter + 1
        self.QLCD_Num.display(self.Counter) # 將Counter值顯示到QLCD_Num物件
    
    @pyqtSlot()
    def on_QPB_Sub_clicked(self):           # 當按下"SUB (-1)"按鈕時要執行的方法
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Counter = self.Counter - 1
        self.QLCD_Num.display(self.Counter) # 將Counter值顯示到QLCD_Num物件

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main_Window = MainWindow()
    Main_Window.show()
    sys.exit(app.exec_())
