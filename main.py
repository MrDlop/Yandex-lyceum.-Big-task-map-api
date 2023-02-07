import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PIL.ImageQt import ImageQt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from interface.interface_main import Ui_MainWindow
from PIL import Image

from getter_map import *


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.coord_x, self.coord_y = 0, 0
        self.scale = 1

        self.pushButton_searh.clicked.connect(self.pushButton_searh_clicked)

    def pushButton_searh_clicked(self):
        self.refactor_coords()
        image = map_for_coords([self.coord_x, self.coord_y], scale=self.scale)
        image = Image.open(image)
        self.label_map.setPixmap(QPixmap.fromImage(ImageQt(image)))

    def refactor_coords(self):
        self.coord_x, self.coord_y = map(float, self.lineEdit_search.text().split(","))

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == Qt.Key_PageUp:
            self.scale += 0.1
            if self.scale > 4:
                self.scale = 4

        if a0.key() == Qt.Key_PageDown:
            self.scale -= 0.1
            if self.scale < 1:
                self.scale = 1

        if a0.key() == Qt.Key_Up:
            self.coord_y = (self.coord_y + 5 + 90) % 180 - 90
        if a0.key() == Qt.Key_Down:
            self.coord_y = (self.coord_y - 5 + 90) % 180 - 90
        if a0.key() == Qt.Key_Left:
            self.coord_x = (self.coord_x + 5) % 180
        if a0.key() == Qt.Key_Right:
            self.coord_x = (self.coord_x - 5) % 180

        image = map_for_coords([self.coord_x, self.coord_y], scale=self.scale)
        image = Image.open(image)
        self.label_map.setPixmap(QPixmap.fromImage(ImageQt(image)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
