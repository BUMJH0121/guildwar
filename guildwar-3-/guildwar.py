# _*_ coding: utf-8 _*_

import sys
import os
import main
import input
import search
import pymysql

from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

db = pymysql.connect(host ='localhost', port=3306, user = "root", passwd='112200', db='mydb', charset='utf8')
cursor = db.cursor()

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
        self.PUSH.clicked.connect(self.push)
        self.D_LEADER.currentTextChanged.connect(lambda state, combo = self.D_LEADER : self.combo(state, combo))
        self.D_SECOND.currentTextChanged.connect(lambda state, combo = self.D_SECOND : self.combo(state, combo))
        self.D_THIRD.currentTextChanged.connect(lambda state, combo = self.D_THIRD : self.combo(state, combo))
        self.A_LEADER.currentTextChanged.connect(lambda state, combo = self.A_LEADER : self.combo(state, combo))
        self.A_SECOND.currentTextChanged.connect(lambda state, combo = self.A_SECOND : self.combo(state, combo))
        self.A_THIRD.currentTextChanged.connect(lambda state, combo = self.A_THIRD : self.combo(state, combo))

    def re(self):
        self.main = M_Dialog()
        self.main.show()
        self.close()

    def push(self):
        defense = [self.D_LEADER.currentText(), self.D_SECOND.currentText(), self.D_THIRD.currentText()]
        attack = [self.A_LEADER.currentText(), self.A_SECOND.currentText(), self.A_THIRD.currentText()]
        wod = self.WOD.currentText()
        temp = "SELECT * FROM attack_member where ((d_leader = defense[0] AND d_second = defense[1] AND d_third = defense[2]) OR (d_leader = defense[0] AND d_second = defense[2] AND d_third = defense[1])) AND ((a_leader = attack[0] AND a_second = attack[1] AND a_third = attack[2]) OR (a_leader = attack[0] AND a_second = attack[2] AND a_third = attack[1]))"
        cursor.execute(temp)
        result = cursor.fetchall()
        if result == NULL:
            if wod == '승':
                insert = "INSERT INTO attack_member (d_leader, d_second, d_third, a_leader, a_second, a_third, w) VALUES (defense[0], defense[1], defense[2], attack[0], attack[1], attack[2], 1)"
                cursor.execute(insert)
            else:
                insert = "INSERT INTO attack_member (d_leader, d_second, d_third, a_leader, a_second, a_third, f) VALUES (defense[0], defense[1], defense[2], attack[0], attack[1], attack[2], 1)"
                cursor.execute(insert)
        else:
            if wod == '승':
                t = result[6]
                update = "UPDATE attack_member SET w = t+1 where ((d_leader = defense[0] AND d_second = defense[1] AND d_third = defense[2]) OR (d_leader = defense[0] AND d_second = defense[2] AND d_third = defense[1])) AND ((a_leader = attack[0] AND a_second = attack[1] AND a_third = attack[2]) OR (a_leader = attack[0] AND a_second = attack[2] AND a_third = attack[1]))"
                cursor.execute(update)
            else:
                t = result[7]
                update = "UPDATE attack_member SET f = t+1 where ((d_leader = defense[0] AND d_second = defense[1] AND d_third = defense[2]) OR (d_leader = defense[0] AND d_second = defense[2] AND d_third = defense[1])) AND ((a_leader = attack[0] AND a_second = attack[1] AND a_third = attack[2]) OR (a_leader = attack[0] AND a_second = attack[2] AND a_third = attack[1]))"
                cursor.execute(update)
        db.commit()

    def combo(self, state, combo):
        idx = combo.findText(combo.currentText())
        if idx != -1:
            combo.setEditText(combo.itemText(idx))

class S_Dialog(QDialog, search.Ui_s_dialog):
    def __init__(self):
        super(QDialog, self).__init__()
        self.setupUi(self)
        self.RETURN.clicked.connect(self.re)
        self.SEARCH.clicked.connect(self.search)
        self.D_LEADER.currentTextChanged.connect(lambda state, combo = self.D_LEADER : self.combo(state, combo))
        self.D_SECOND.currentTextChanged.connect(lambda state, combo = self.D_SECOND : self.combo(state, combo))
        self.D_THIRD.currentTextChanged.connect(lambda state, combo = self.D_THIRD : self.combo(state, combo))

    def re(self):
        self.main = M_Dialog()
        self.main.show()
        self.close()

    def search(self):
        defense = [self.D_LEADER.currentText(), self.D_SECOND.currentText(), self.D_THIRD.currentText()]

    def combo(self, state, combo):
        idx = combo.findText(combo.currentText())
        if idx != -1:
            combo.setEditText(combo.itemText(idx))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_dialog = M_Dialog()
    main_dialog.show()
    app.exec_()