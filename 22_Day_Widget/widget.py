import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QVBoxLayout

class MyWidgetApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout
        layout = QVBoxLayout()

        # Label
        self.label = QLabel('Enter your name:', self)
        layout.addWidget(self.label)

        # Line Edit (Text Input)
        self.line_edit = QLineEdit(self)
        layout.addWidget(self.line_edit)

        # Button
        self.button = QPushButton('Submit', self)
        self.button.clicked.connect(self.on_click)
        layout.addWidget(self.button)

        # Set the layout to the main window
        self.setLayout(layout)

        # Window settings
        self.setWindowTitle('PyQt5 Widgets Example')
        self.setGeometry(300, 300, 300, 200)

    def on_click(self):
        name = self.line_edit.text()
        self.label.setText(f'Hello, {name}!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidgetApp()
    ex.show()
    sys.exit(app.exec_())
