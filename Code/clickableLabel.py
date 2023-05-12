from PyQt6 import QtWidgets, QtGui

class ClickableLabel(QtWidgets.QLabel):
    def __init__(self):
        super(ClickableLabel, self).__init__()

        # Initialize variables to store name, selected status, other buttons, and type of label
        self.__name = None
        self.__selected = False
        self.__otherButtons = []
        self.__type = ""

        # Set default background color of label to white
        self.setStyleSheet("QLabel {background-color: white;}")

    # Set the type of the label to the given image file
    def setType(self, image):
        self.__type = image

    # Return the type of the label
    def getType(self):
        return self.__type

    # Add another button to the list of other buttons for this label
    def setOtherButtons(self, button):
        self.__otherButtons.append(button)

    # Return the list of other buttons for this button
    def getOtherButtons(self):
        return self.__otherButtons

    # Set the name of the button to the given string
    def setName(self, name):
        self.__name = name

    # Return the name of the label
    def getName(self):
        return self.__name

    # Return whether or not the button is currently selected
    def isSelected(self):
        return self.__selected

    # Set this button to be selected and deselect all other buttons in the list of other buttons
    def setSelected(self):
        for button in self.getOtherButtons():
            button.removeSelected()
        self.__selected = True

        # Change the background color and add a border to indicate selection
        self.setStyleSheet("background-color: rgb(220, 255, 220); border: 2px solid rgb(100, 235, 100);")

        # Access the main window and get the grid object to set the type of the grid to the type of this label
        main = self.parent().parent().parent()
        grid = main.getGrid()
        grid.setType(self.getType())

    # Deselect this button by setting selected status to false and resetting the background color
    def removeSelected(self):
        self.__selected = False
        self.setStyleSheet("background-color: white;")

    def mousePressEvent(self, ev: QtGui.QMouseEvent):
        if not self.isSelected():
            # If the button is not currently selected, select it
            self.setSelected()

