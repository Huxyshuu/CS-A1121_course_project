import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem
from PyQt6.QtGui import QPalette, QColor

#custom Classes
from grid import Grid

class MainWindow(QMainWindow): # Creating a subclass of QMainWindow for better control over the window customization

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Pipeflow - Hugo")

        self.setFixedSize(QSize(1280, 800)) # Sets a fixed window size



        self.button = QPushButton("Press Me!")
        self.button.setFixedSize(QSize(200, 200))
        self.button.clicked.connect(self.printClick) # PyCharm showing error on .connect  # it works regardless
                                                     # widget.clicked.connect(func) # Add functionality

        self.button2 = QPushButton("Press Me!")
        self.button2.setFixedSize(QSize(200, 200))
        self.button2.clicked.connect(self.printClick)

        baseLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()



        # Left side buttons
        baseLayout.addLayout(leftLayout)
        leftLayout.addWidget(self.button)


        # Grid (750, 750, 50) is a good size for a window of size (1280, 800)
        self.view = Grid(750, 750, 50)
        self.view.show()
        baseLayout.addWidget(self.view)



        # Pipes
        baseLayout.addLayout(rightLayout)
        rightLayout.addWidget(self.button2)

        widget = QWidget()
        widget.setLayout(baseLayout)
        self.setCentralWidget(widget)

    def printClick(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)


app = QApplication(sys.argv)

window = MainWindow()
window.show() # Makes the window visible

app.exec()