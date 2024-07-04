#QTableWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Membuat model
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Age'])

        # Menambahkan data ke model
        names = ['Alice', 'Bob', 'Charlie']
        ages = [25, 32, 18]
        for i in range(3):
            name_item = QStandardItem(names[i])
            age_item = QStandardItem(str(ages[i]))
            self.model.appendRow([name_item, age_item])

        # Membuat QTableView dan mengatur modelnya
        self.table = QTableView()
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#QListWidget

from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Membuat QListWidget
        self.list_widget = QListWidget()

        # Menambahkan item ke QListWidget
        self.list_widget.addItem('Alice')
        self.list_widget.addItem('Bob')
        self.list_widget.addItem('Charlie')

        self.setCentralWidget(self.list_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#QDialog

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton, QVBoxLayout

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello!")
        layout = QVBoxLayout()
        button = QPushButton("Close")
        button.clicked.connect(self.close)
        layout.addWidget(button)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("Open Dialog")
        button.clicked.connect(self.open_dialog)
        self.setCentralWidget(button)

    def open_dialog(self):
        dialog = CustomDialog()
        dialog.exec_()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#QMessageBox

from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        button = QPushButton("Show Message")
        button.clicked.connect(self.show_message)
        self.setCentralWidget(button)

    def show_message(self):
        QMessageBox.information(self, "Hello!", "This is a message.")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

#QDateTimeEdit

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateTimeEdit
from PyQt5.QtCore import QDateTime

class DateTimeEditExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('QDateTimeEdit Example')

        layout = QVBoxLayout()

        datetime_edit = QDateTimeEdit()
        datetime_edit.setDateTime(QDateTime.currentDateTime())  # Mengatur tanggal dan waktu awal ke tanggal dan waktu saat ini
        layout.addWidget(datetime_edit)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    window = DateTimeEditExample()
    window.show()
    app.exec()
