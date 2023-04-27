import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QGraphicsRectItem, QGraphicsScene, QGraphicsView, QGraphicsLineItem, QGraphicsPixmapItem, QLineEdit
from PyQt6.QtGui import QPalette, QColor, QPixmap, QIntValidator

#custom Classes
from grid import Grid
from gridPipe import GridPipe
from pipeButtonCreator import PipeButtonCreator
from ui import UI


class MainWindow(QMainWindow): # Creating a subclass of QMainWindow for better control over the window customization

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pipeflow - Hugo")

        # Sets a fixed window size
        self.setFixedSize(QSize(1280, 850))

        # Creates the UI for the program
        UI(self)

    def calculateFlow(self, start, end):
        # two lines below extract the pressure from the text for use in the calculation
        result = start + end
        self.flowLabel.setText("Flow speed: {} m/s".format(result))
        return result

    def clearGrid(self):
        for item in self.view.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.view.scene.removeItem(item)
                item.remove()

    def getGrid(self):
        return self.view

    def changeEndData(self, text):
        if text:
            self.endData.setText("End point pressure: {} kPa".format(text))
        else:
            self.endData.setText("End point pressure: 0 kPa")

    def changeStartData(self, text):
        if text:
            self.startData.setText("Starting point pressure: {} kPa".format(text))
        else:
            self.startData.setText("Starting point pressure: 0 kPa")


    # self.pipe = QGraphicsPixmapItem()
    # self.pipe.setPixmap(QPixmap('../Images/StraightPipe.png').scaled(49, 49))
    # self.pipe.setOffset(self.x * 50 + 1, self.y * 50)
    # self.scene.addItem(self.pipe)
    # self.scene.removeItem(self.pipe)




if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() # Makes the window visible

    app.exec()