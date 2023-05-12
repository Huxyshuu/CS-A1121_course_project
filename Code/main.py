import math
import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QMainWindow

#custom Classes
from ui import UI

# Creating a subclass of QMainWindow for better control over the window customization
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Pipeflow - Hugo")

        #default rotation of the pipes
        self.pipeRotation = 0

        # Sets a fixed window size
        WINDOW_WIDTH = 1280
        WINDOW_HEIGHT = 850
        self.setFixedSize(QSize(WINDOW_WIDTH, WINDOW_HEIGHT))

        # Creates the UI for the program
        self.ui = UI(self)

        #self.view is initalized in the UI method
        self.grid = self.ui.grid



    def calculateFlow(self, start, end):
        # the line below extracts the pressure from the text for use in the calculation
        startHeight, endHeight = self.grid.getHeights()

        bernoulli = ((2*(start-end) + 2*9.81*(startHeight-endHeight) + 0.1) / (997*(math.pi * math.pow(0.3, 2))))

        if bernoulli > 0:
            result = math.sqrt(bernoulli)
            # flowLabel is found in UI class
            self.flowLabel.setText("<p>Flow speed: {:.3f} m/s</p>".format(result))
            return result
        else:
            self.flowLabel.setText('<p style="color: red; text-align: center;">Flow speed: ERROR m/s</p>\nPlease set the starting value to be greater than the end')
            return 0

    def rotatePipes(self):
        if self.pipeRotation == 270:
            self.pipeRotation = 0
        else:
            self.pipeRotation += 90
        self.grid.rotate(self.pipeRotation)
        self.ui.refresh(self.pipeRotation)

    def getGrid(self):
        return self.grid


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show() # Makes the window visible

    app.exec()