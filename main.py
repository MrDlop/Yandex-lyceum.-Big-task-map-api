import sys

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PIL.ImageQt import ImageQt
from PIL import Image

from getter_map import *
from interface.interface_main import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    scale: float
    coord_x: float
    coord_y: float
    type_map: str

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.coord_x, self.coord_y = 55.958736, 54.735152
        self.point = None
        self.type_map = "map"
        self.scale = 1

        self.pushButton_searh.clicked.connect(self.pushButton_search_clicked)

    def refactor_coords(self):
        self.coord_x, self.coord_y = map(float, self.lineEdit_search.text().split(","))

    def update(self):
        options = dict()
        if not (self.point is None):
            options["pt"] = f"{','.join(str(i) for i in self.point)},round"
        image = map_for_coords((self.coord_x, self.coord_y),
                               type_map=self.type_map,
                               scale=self.scale,
                               **options)
        image = Image.open(image)
        self.label_map.setPixmap(QPixmap.fromImage(ImageQt(image)))

    def pushButton_search_clicked(self):
        self.refactor_coords()
        self.update()

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
            self.coord_y = self.coord_y + 0.0001
            if self.coord_y > 90:
                self.coord_y = 90
        if a0.key() == Qt.Key_Down:
            self.coord_y = self.coord_y - 0.0001
            if self.coord_y < -90:
                self.coord_y = -90
        if a0.key() == Qt.Key_Right or a0.key() == Qt.Key_6:
            self.coord_x = self.coord_x + 0.0001
            if self.coord_x > 90:
                self.coord_x = -90
        if a0.key() == Qt.Key_Left or a0.key() == Qt.Key_4:
            self.coord_x = self.coord_x - 0.0001
            if self.coord_x < -90:
                self.coord_x = 90

        self.update()

    # No active prototype
    # -------------------------------------------------------------------------------
    def replace_type(self):
        self.type_map = self.sender().text()
        self.update()

    def add_search(self):
        self.point = search_name(self.sender().text())
        self.update()

    def delete_search(self):
        self.point = None
        self.update()

    # -------------------------------------------------------------------------------


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
