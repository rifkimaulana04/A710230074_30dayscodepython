import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('My PyQt5 App')
        self.setGeometry(300, 300, 300, 200)

        btn = QPushButton('Click me', self)
        btn.move(100, 80)
        btn.clicked.connect(self.showMessage)

    def showMessage(self):
        QMessageBox.information(self, 'Message', 'You clicked the button!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
