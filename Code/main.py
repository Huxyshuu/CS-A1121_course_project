import sys

from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow): # Creating a subclass of QMainWindow for better control over the window customization

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Pipeflow - Hugo")

        self.setFixedSize(QSize(1280, 800)) # Sets a fixed window size

        self.button = QPushButton("Press Me!")
        self.button.setFixedSize(QSize(200, 200))
        # widget.clicked.connect(func) # Add functionality
        self.button.clicked.connect(self.printClick) # PyCharm showing error on .connect  # it works regardless

        # Set the central widget of the Window.
        self.setCentralWidget(self.button)

    def printClick(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show() # Makes the window visible

app.exec()