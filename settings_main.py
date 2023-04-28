import sys

from PyQt5.QtWidgets import QApplication, QWidget

from interface.interface_settings import Ui_Form
from PyQt5 import QtCore, QtGui, QtWidgets


class SettingsForm(Ui_Form, QWidget):
    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)
        self.parent = parent
        self.comboBox_map.addItem("Схема")
        # map sat sat, skl
        self.comboBox_map.addItem("Спутник")
        self.comboBox_map.addItem("Гибрид")
        self.comboBox_map.setEditText("Схема")
        self.comboBox_map.currentTextChanged.connect(self.comboBox_map_editTextChanged)

    def comboBox_map_editTextChanged(self):
        type_map = {"Спутник": "sat", "Схема": "map", "Гибрид": "sat,skl"}
        self.parent.type_map = type_map[self.comboBox_map.currentText()]
        self.parent.update()
