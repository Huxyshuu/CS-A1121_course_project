import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsPixmapItem
from PyQt6.QtGui import QPalette, QColor, QPixmap

#custom Classes
from grid import Grid
from pipes import Pipes

class MainWindow(QMainWindow): # Creating a subclass of QMainWindow for better control over the window customization

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Pipeflow - Hugo")

        self.setFixedSize(QSize(1280, 850)) # Sets a fixed window size



        self.button = QPushButton("Press Me!")
        self.button.setFixedSize(QSize(200, 200))
        self.button.clicked.connect(self.printClick) # PyCharm showing error on .connect  # it works regardless
                                                     # widget.clicked.connect(func) # Add functionality

        self.button2 = QPushButton("Green!")
        self.button2.setFixedSize(QSize(200, 50))
        self.button2.clicked.connect(lambda: self.switchType("green")) # Lambda function allows the use of parameters here
        self.button2.setStyleSheet("background-color: white;")
        self.button3 = QPushButton("Red!")
        self.button3.setFixedSize(QSize(200, 50))
        self.button3.clicked.connect(lambda: self.switchType("red"))
        self.button3.setStyleSheet("background-color: white;")

        self.straightPipe = QLabel()
        self.straightPipe.setPixmap(QPixmap('../Images/StraightPipe.png').scaled(50, 50))
        self.straightPipe.setFixedSize(75, 75)
        self.straightPipe.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.straightPipe.setStyleSheet("background-color: white;")

        baseLayout = QHBoxLayout()
        leftLayout = QVBoxLayout()
        rightLayout = QVBoxLayout()
        topLayout = QHBoxLayout()

        baseLayout.addLayout(leftLayout)
        baseLayout.addLayout(rightLayout)

        # Left side buttons
        label = QLabel("Stuff")
        label.setFixedSize(100, 100)
        leftLayout.addWidget(label)
        leftLayout.addWidget(self.button)

        # Top right layout
        # Pipes
        pipeBox = QWidget()
        rightLayout.addWidget(pipeBox)
        pipeBox.setLayout(topLayout)
        pipeBox.setStyleSheet("border: 1px solid black; background-color: lightgray;")
        topLayout.addWidget(self.straightPipe)
        topLayout.addWidget(self.button2)
        topLayout.addWidget(self.button3)

        # Bottom right layout
        # Grid (750, 750, 50) is a good size for a window of size (1280, 900)
        self.view = Grid(750, 750, 50)
        self.view.show()
        rightLayout.addWidget(self.view)

        widget = QWidget()
        widget.setLayout(baseLayout)
        self.setCentralWidget(widget)

    def printClick(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)

    def switchType(self, type):
        print(type)




app = QApplication(sys.argv)

window = MainWindow()
window.show() # Makes the window visible

app.exec()