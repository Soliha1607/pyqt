import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QWidget, QLayout, QVBoxLayout

from idk.main1 import Page


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Just Nothing")
        self.setFixedSize(430, 900)

        self.setStyleSheet("background-color: #1C0F0D;")
        self.layout = self.__set_up_layout()
        self.setLayout(self.layout)

    def __set_up_layout(self) -> QLayout:
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        page = Page()
        main_layout.addWidget(page)
        return main_layout


app = QApplication(sys.argv)
app.setStyleSheet("* {padding: 0px; margin: 0px;}")
window = Main()
window.show()

sys.exit(app.exec())