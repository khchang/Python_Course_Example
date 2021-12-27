# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
# from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication   # 手動加入
from PyQt5.QtCore import QTimer                         # 手動加入
import sys                                              # 手動加入

# from .Ui_ch25_2 import Ui_MainWindow
# 將from .Ui_ch25_2 import Ui_MainWindow的.去掉
from Ui_ch25_2 import Ui_MainWindow                     # 手動加入


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

        self.Counter_Value = 0              # 初始化計數值(屬性)

        # 初始化QTimer類別
        self.Counter_Timer = QTimer()       # 以QTimer類別建立一個self.Counter_Timer物件

        self.Counter_Timer.timeout.connect(self.Update_LCD_NUM)
        # 將timeout訊號指向self.Update_LCD_NUM方法
    
    def Update_LCD_NUM(self):
        self.Counter_Value += 1
        self.QLCD_Num.display(self.Counter_Value)

    @pyqtSlot()
    def on_QPB_Start_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        if (self.Counter_Timer.isActive() == False):    # 確認self.Counter_Timer是否在計時
            self.Counter_Timer.start(1000)              # 開始計時，計時時間1000 ms
    
    @pyqtSlot()
    def on_QPB_Stop_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Counter_Timer.stop()
    
    @pyqtSlot()
    def on_QPB_Reset_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        # raise NotImplementedError
        self.Counter_Value = 0
        self.QLCD_Num.display(self.Counter_Value)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Main_Window = MainWindow()
    Main_Window.show()
    sys.exit(app.exec_())
