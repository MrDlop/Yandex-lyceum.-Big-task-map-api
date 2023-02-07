import sys

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

        self.pushButton_searh.clicked.connect(self.pushButton_searh_clicked)

    def pushButton_searh_clicked(self):
        self.refactor_coords()
        image = map_for_coords([self.coord_x, self.coord_y])
        image = Image.open(image)
        self.label_map.setPixmap(QPixmap.fromImage(ImageQt(image)))

    def refactor_coords(self):
        self.coord_x, self.coord_y = map(float, self.lineEdit_search.text().split(","))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
