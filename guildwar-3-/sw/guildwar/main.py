# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MAIN(object):
    def setupUi(self, MAIN):
        MAIN.setObjectName("MAIN")
        MAIN.resize(1341, 751)
        MAIN.setMinimumSize(QtCore.QSize(1341, 751))
        MAIN.setMaximumSize(QtCore.QSize(1341, 751))
        self.label = QtWidgets.QLabel(MAIN)
        self.label.setGeometry(QtCore.QRect(210, 90, 931, 91))
        self.label.setStyleSheet("color: rgb(247, 247, 238);\n"
"font: 36pt \"배달의민족 도현\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.input = QtWidgets.QPushButton(MAIN)
        self.input.setGeometry(QtCore.QRect(460, 520, 421, 61))
        self.input.setMinimumSize(QtCore.QSize(421, 61))
        self.input.setMaximumSize(QtCore.QSize(421, 61))
        self.input.setAcceptDrops(False)
        self.input.setStyleSheet("font: 20pt \"배달의민족 도현\";")
        self.input.setCheckable(False)
        self.input.setChecked(False)
        self.input.setAutoRepeat(False)
        self.input.setAutoExclusive(False)
        self.input.setDefault(False)
        self.input.setObjectName("input")
        self.find = QtWidgets.QPushButton(MAIN)
        self.find.setGeometry(QtCore.QRect(460, 620, 421, 61))
        self.find.setMinimumSize(QtCore.QSize(421, 61))
        self.find.setMaximumSize(QtCore.QSize(421, 61))
        self.find.setStyleSheet("font: 20pt \"배달의민족 도현\";")
        self.find.setObjectName("find")
        self.graphicsView = QtWidgets.QGraphicsView(MAIN)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 1341, 751))
        self.graphicsView.setMinimumSize(QtCore.QSize(1341, 751))
        self.graphicsView.setMaximumSize(QtCore.QSize(1341, 751))
        self.graphicsView.setStyleSheet("background-image: url(:/background/KakaoTalk_20200920_123437693.png);")
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsView.raise_()
        self.label.raise_()
        self.input.raise_()
        self.find.raise_()

        self.retranslateUi(MAIN)
        QtCore.QMetaObject.connectSlotsByName(MAIN)

    def retranslateUi(self, MAIN):
        _translate = QtCore.QCoreApplication.translate
        MAIN.setWindowTitle(_translate("MAIN", "Dialog"))
        self.label.setText(_translate("MAIN", "서머너즈워 길/점령전 방덱 깨기"))
        self.input.setText(_translate("MAIN", "공덱 입력"))
        self.find.setText(_translate("MAIN", "공덱 찾기"))
import main_background_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QDialog()
    ui = Ui_MAIN()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(app.exec_())
