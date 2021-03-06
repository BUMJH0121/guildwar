# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

monster = open('monster_list.txt', mode = 'r', encoding = 'utf-8')
m = monster.readlines()
m_list = list(map(lambda s: s.strip(), m))
monster.close()

class Ui_s_dialog(object):
    def setupUi(self, s_dialog):
        s_dialog.setObjectName("s_dialog")
        s_dialog.resize(1341, 751)
        s_dialog.setMinimumSize(QtCore.QSize(1341, 751))
        s_dialog.setMaximumSize(QtCore.QSize(1341, 751))
        self.graphicsView = QtWidgets.QGraphicsView(s_dialog)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1341, 751))
        self.graphicsView.setMinimumSize(QtCore.QSize(1341, 751))
        self.graphicsView.setMaximumSize(QtCore.QSize(1341, 751))
        self.graphicsView.setStyleSheet("background-image: url(:/image/KakaoTalk_20200921_163222539.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.D_LEADER = QtWidgets.QComboBox(s_dialog)
        self.D_LEADER.setGeometry(QtCore.QRect(180, 80, 241, 51))
        self.D_LEADER.setEditable(True)
        self.D_LEADER.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.D_LEADER.setDuplicatesEnabled(True)
        self.D_LEADER.setObjectName("D_LEADER")
        self.D_LEADER.addItems(m_list)
        self.label = QtWidgets.QLabel(s_dialog)
        self.label.setGeometry(QtCore.QRect(30, 80, 151, 51))
        self.label.setStyleSheet("font: 20pt \"배달의민족 도현\";\n"
"color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(s_dialog)
        self.label_2.setGeometry(QtCore.QRect(460, 80, 151, 51))
        self.label_2.setStyleSheet("font: 20pt \"배달의민족 도현\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.D_SECOND = QtWidgets.QComboBox(s_dialog)
        self.D_SECOND.setGeometry(QtCore.QRect(610, 80, 241, 51))
        self.D_SECOND.setEditable(True)
        self.D_SECOND.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.D_SECOND.setDuplicatesEnabled(True)
        self.D_SECOND.setObjectName("D_SECOND")
        self.D_SECOND.addItems(m_list)
        self.label_3 = QtWidgets.QLabel(s_dialog)
        self.label_3.setGeometry(QtCore.QRect(920, 80, 151, 51))
        self.label_3.setStyleSheet("font: 20pt \"배달의민족 도현\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.D_THIRD = QtWidgets.QComboBox(s_dialog)
        self.D_THIRD.setGeometry(QtCore.QRect(1070, 80, 241, 51))
        self.D_THIRD.setEditable(True)
        self.D_THIRD.setInsertPolicy(QtWidgets.QComboBox.NoInsert)
        self.D_THIRD.setDuplicatesEnabled(True)
        self.D_THIRD.setObjectName("D_THIRD")
        self.D_THIRD.addItems(m_list)
        self.SEARCH = QtWidgets.QPushButton(s_dialog)
        self.SEARCH.setGeometry(QtCore.QRect(570, 160, 311, 41))
        self.SEARCH.setObjectName("SEARCH")
        self.DISPLAY = QtWidgets.QTextBrowser(s_dialog)
        self.DISPLAY.setGeometry(QtCore.QRect(50, 220, 1251, 451))
        self.DISPLAY.setStyleSheet("font: 14pt \"휴먼명조\";")
        self.DISPLAY.setObjectName("DISPLAY")
        self.RETURN = QtWidgets.QPushButton(s_dialog)
        self.RETURN.setGeometry(QtCore.QRect(1140, 690, 161, 51))
        self.RETURN.setObjectName("RETURN")

        self.retranslateUi(s_dialog)
        QtCore.QMetaObject.connectSlotsByName(s_dialog)

    def retranslateUi(self, s_dialog):
        _translate = QtCore.QCoreApplication.translate
        s_dialog.setWindowTitle(_translate("s_dialog", "Dialog"))
        self.label.setText(_translate("s_dialog", "LEADER : "))
        self.label_2.setText(_translate("s_dialog", "SECOND : "))
        self.label_3.setText(_translate("s_dialog", "THIRD : "))
        self.SEARCH.setText(_translate("s_dialog", "검색"))
        self.DISPLAY.setHtml(_translate("s_dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'휴먼명조\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.RETURN.setText(_translate("s_dialog", "돌아가기"))
import main_background_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    s_dialog = QtWidgets.QDialog()
    ui = Ui_s_dialog()
    ui.setupUi(s_dialog)
    s_dialog.show()
    sys.exit(app.exec_())
