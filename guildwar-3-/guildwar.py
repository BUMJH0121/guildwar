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
        db = pymysql.connect(host ='localhost', port=3306, user = "root", passwd='112200', db='mydb', charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        defense = [self.D_LEADER.currentText(), self.D_SECOND.currentText(), self.D_THIRD.currentText()]
        attack = [self.A_LEADER.currentText(), self.A_SECOND.currentText(), self.A_THIRD.currentText()]
        wod = self.WOD.currentText()
        temp = "SELECT * FROM attack_member where d_leader = %s and d_second = %s and d_third = %s and a_leader = %s and a_second = %s and a_third = %s"
        cursor.execute(temp, (defense[0], defense[1], defense[2], attack[0], attack[1], attack[2]))
        result = cursor.fetchall()
        cursor.execute(temp, (defense[0], defense[2], defense[1], attack[0], attack[1], attack[2]))
        result += cursor.fetchall()
        cursor.execute(temp, (defense[0], defense[1], defense[2], attack[0], attack[2], attack[1]))
        result += cursor.fetchall()
        cursor.execute(temp, (defense[0], defense[2], defense[1], attack[0], attack[2], attack[1]))
        result += cursor.fetchall()

        if result == ():
            if wod == '승':
                p = "INSERT INTO attack_member(d_leader, d_second, d_third, a_leader, a_second, a_third, w, f) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(p, (defense[0], defense[1], defense[2], attack[0], attack[1], attack[2], 1, 0))
            else:
                p = "INSERT INTO attack_member(d_leader, d_second, d_third, a_leader, a_second, a_third, w, f) VALUES (%s, %s, %s, %s, %s, %s, %s, %S)"
                cursor.execute(p, (defense[0], defense[1], defense[2], attack[0], attack[1], attack[2], 0, 1))
        else:
            if wod == '승':
                p = "UPDATE attack_member set w = %s where d_leader = %s and d_second = %s and d_third = %s and a_leader = %s and a_second = %s and a_third = %s"
                cursor.execute(p, (result['w']+1,result['d_leader'], result['d_second'], result['d_third'], result['a_leader'], result['a_second'], result['a_third']))
            else:
                p = "UPDATE attack_member set f = %s where d_leader = %s and d_second = %s and d_third = %s and a_leader = %s and a_second = %s and a_third = %s"
                cursor.execute(p, (result['f']+1,result['d_leader'], result['d_second'], result['d_third'], result['a_leader'], result['a_second'], result['a_third']))
        db.commit()
        db.close()

    def combo(self, state, combo):
        def keyPressEvent(self, e):
            if e.key() in [Qt.key_Return, Qt.Key_Enter]: 
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
        self.DISPLAY.clear()
        self.DISPLAY.append('   ' + '리더' + '        ' + '두번째' + '       ' + '세번째' + '       ' + '승률')
        db = pymysql.connect(host ='localhost', port=3306, user = "root", passwd='112200', db='mydb', charset='utf8')
        cursor = db.cursor(pymysql.cursors.DictCursor)
        defense = [self.D_LEADER.currentText(), self.D_SECOND.currentText(), self.D_THIRD.currentText()]
        temp = "SELECT * FROM attack_member where d_leader = %s and d_second = %s and d_third = %s"
        cursor.execute(temp, (defense[0], defense[1], defense[2]))
        result = cursor.fetchall()
        cursor.execute(temp, (defense[0], defense[2], defense[1]))
        result += tuple(cursor.fetchall())
        for r in result:
            self.DISPLAY.append('   ' + r['a_leader'] + '   ' + r['a_second'] + '   ' + r['a_third'] + '    ' + str((r['w']/(r['w']+r['f']))*100))
        db.close()

    def combo(self, state, combo):
        def keyPressEvent(self, e):
            if e.key() in [Qt.key_Return, Qt.Key_Enter]: 
                idx = combo.findText(combo.currentText())
                if idx != -1:
                    combo.setEditText(combo.itemText(idx))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_dialog = M_Dialog()
    main_dialog.show()
    app.exec_()