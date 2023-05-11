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
        self.setFixedSize(QSize(1280, 850))

        # Creates the UI for the program
        self.ui = UI(self)

        #self.view is initalized in the UI method
        self.grid = self.ui.grid



    def calculateFlow(self, start, end):
        # two lines below extract the pressure from the text for use in the calculation
        startHeight, endHeight = self.grid.getHeights()

        # loss = (4 * 0.01 * math.pow(0.28, 2)) / (math.pow(math.pi, 2) * math.pow(0.3, 5) * 997)

        #v = sqrt(2(P_start - P_end) + 2(pgh_end - pgh_start - h_end*f + h_start*f) / p)
        # bernoulli = 2 * (start - end) + 2 * (997 * 9.81 * endHeight - 997 * 9.81 * startHeight - endHeight * loss + startHeight * loss) / 997

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