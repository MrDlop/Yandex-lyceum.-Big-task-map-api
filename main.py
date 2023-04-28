import os
import sys

from PyQt5 import QtGui, uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PIL import Image

from getter_map import *
# from interface.interface_main import Ui_MainWindow
from settings_main import SettingsForm


class MyWidget(QMainWindow):
    scale: float
    coord_x: float
    coord_y: float
    type_map: str

    def __init__(self):
        super().__init__()
        uic.loadUi('interface/interface_main.ui', self)

        self.coord_x, self.coord_y = 37.677751, 55.757718
        self.point = None
        self.type_map = "map"
        self.scale = 1
        self.idx = ""
        self.address = ""
        self.check = False

        self.pushButton_searh.clicked.connect(self.pushButton_search_clicked)
        self.pushButton_settings.clicked.connect(self.pushButton_settings_clicked)
        self.pushButton_cancel.clicked.connect(self.pushButton_cancel_clicked)
        self.checkBox_index.stateChanged.connect(self.index_clicked)
        self.update()

    def index_clicked(self, state):
        self.check = not self.check
        if state == Qt.Checked:
            if not (self.point is None):
                self.label.setText(self.address + " " + self.idx)
        else:
            self.label.setText(self.address)

    def refactor_coords(self):
        self.point = search_coords_for_name(self.lineEdit_search.text())
        self.address = address_obj(self.lineEdit_search.text())
        self.idx = postal_number_obj(self.lineEdit_search.text())
        if self.check:
            self.label.setText(self.address + " " + self.idx)
        else:
            self.label.setText(self.address)
        self.coord_x, self.coord_y = self.point
        self.update()

    def update(self):
        options = dict()
        if not (self.point is None):
            options["pt"] = f"{','.join(str(i) for i in self.point)},round"

        image = BytesIO(map_for_coords((self.coord_x, self.coord_y),
                                       type_map=self.type_map,
                                       scale=self.scale,
                                       **options).content)
        image = Image.open(image)
        self.label_map.setPixmap(QPixmap.fromImage(ImageQt(image)))

    def pushButton_search_clicked(self):
        self.refactor_coords()
        self.update()

    def pushButton_cancel_clicked(self):
        self.point = None
        self.address = ""
        self.idx = ""
        self.label.setText("")
        self.update()

    def pushButton_settings_clicked(self):
        self.form = SettingsForm(self)
        self.form.show()

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_PageUp:
            self.scale += 0.1
            if self.scale > 4:
                self.scale = 4

        if a0.key() == Qt.Key_PageDown:
            self.scale -= 0.1
            if self.scale < 1:
                self.scale = 1
            self.update()

        if a0.key() == Qt.Key_Up or a0.key() == Qt.Key_8:
            self.coord_y = self.coord_y + 0.0001
            if self.coord_y > 90:
                self.coord_y = 90
            self.update()

        if a0.key() == Qt.Key_Down or a0.key() == Qt.Key_2:
            self.coord_y = self.coord_y - 0.0001
            if self.coord_y < -90:
                self.coord_y = -90
            self.update()

        if a0.key() == Qt.Key_Right or a0.key() == Qt.Key_6:
            self.coord_x = self.coord_x + 0.0001
            if self.coord_x > 90:
                self.coord_x = -90
            self.update()

        if a0.key() == Qt.Key_Left or a0.key() == Qt.Key_4:
            self.coord_x = self.coord_x - 0.0001
            if self.coord_x < -90:
                self.coord_x = 90
            self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.addLibraryPath(os.getcwd() + "imageformats")
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
