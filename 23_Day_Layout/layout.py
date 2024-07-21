import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout

class LayoutExample(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        grid = QGridLayout()

        # Widgets for VBox
        label_vbox = QLabel('Vertical Layout', self)
        button_vbox = QPushButton('Button 1', self)
        vbox.addWidget(label_vbox)
        vbox.addWidget(button_vbox)

        # Widgets for HBox
        label_hbox = QLabel('Horizontal Layout', self)
        button_hbox1 = QPushButton('Button 2', self)
        button_hbox2 = QPushButton('Button 3', self)
        hbox.addWidget(label_hbox)
        hbox.addWidget(button_hbox1)
        hbox.addWidget(button_hbox2)

        # Widgets for Grid
        label_grid = QLabel('Grid Layout', self)
        grid.addWidget(label_grid, 0, 0)
        grid.addWidget
