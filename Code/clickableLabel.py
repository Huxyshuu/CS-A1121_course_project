from PyQt6 import QtWidgets, QtGui


class ClickableLabel(QtWidgets.QLabel):
    def __init__(self):
        super(ClickableLabel, self).__init__()
        self.__name = None
        self.__selected = False
        self.setStyleSheet("background-color: white;")
        self.__otherButtons = []

    def setOtherButtons(self, button):
        self.__otherButtons.append(button)

    def getOtherButtons(self):
        return self.__otherButtons

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isSelected(self):
        return self.__selected

    def setSelected(self):
        for button in self.getOtherButtons():
            button[1].removeSelected()
        self.__selected = True

    def removeSelected(self):
        self.__selected = False
        self.setStyleSheet("background-color: white;")

    def mousePressEvent(self, ev: QtGui.QMouseEvent):
        if not self.isSelected():
            self.setStyleSheet("background-color: rgb(220, 255, 220); border: 2px solid rgb(100, 235, 100);")
            self.setSelected()
