# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(235, 301)
        Form.setMinimumSize(QtCore.QSize(190, 300))
        Form.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Form.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 234, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox_theme = QtWidgets.QComboBox(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_theme.sizePolicy().hasHeightForWidth())
        self.comboBox_theme.setSizePolicy(sizePolicy)
        self.comboBox_theme.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.comboBox_theme.setFont(font)
        self.comboBox_theme.setObjectName("comboBox_theme")
        self.gridLayout.addWidget(self.comboBox_theme, 0, 2, 1, 1)
        self.label_theme = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_theme.setFont(font)
        self.label_theme.setObjectName("label_theme")
        self.gridLayout.addWidget(self.label_theme, 0, 1, 1, 1)
        self.label_map = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.label_map.setFont(font)
        self.label_map.setObjectName("label_map")
        self.gridLayout.addWidget(self.label_map, 1, 1, 1, 1)
        self.comboBox_map = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.comboBox_map.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.comboBox_map.setFont(font)
        self.comboBox_map.setObjectName("comboBox_map")
        self.gridLayout.addWidget(self.comboBox_map, 1, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки"))
        self.label_theme.setText(_translate("Form", "Тема:"))
        self.label_map.setText(_translate("Form", "Тип карты:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
