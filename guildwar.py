# _*_ coding: utf-8 _*_

import sys
import os
import main
import input
import search

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class M_Dialog(QDialog, main.Ui_m_dialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.a_input.clicked.connect(self.input)
        self.a_search.clicked.connect(self.search)


    def input(self):
        self.main = I_Dialog()
        self.main.show()
        self.close()

    def search(self):
        self.main = S_Dialog()
        self.main.show()
        self.close()


class I_Dialog(QDialog, input.Ui_i_dialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.RETURN.clicked.connect(self.re)

    def re(self):
        self.main = M_Dialog()
        self.main.show()
        self.close()


class S_Dialog(QDialog, search.Ui_s_dialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.RETURN.clicked.connect(self.re)

    def re(self):
        self.main = M_Dialog()
        self.main.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_dialog = M_Dialog()
    main_dialog.show()
    app.exec_()