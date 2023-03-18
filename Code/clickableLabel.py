from PyQt6 import QtWidgets, QtGui


class ClickableLabel(QtWidgets.QLabel):
    def __init__(self):
        super(ClickableLabel, self).__init__()
        self.__name = None
        self.__selected = False
        self.setStyleSheet("background-color: white;")

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def isSelected(self):
        return self.__selected

    def setSelected(self):
        self.__selected = True

    def removeSelected(self):
        self.__selected = False

    def mousePressEvent(self, ev: QtGui.QMouseEvent):
        if not self.isSelected():
            self.setStyleSheet("background-color: pink;")
            self.setSelected()

        print(self.getName())
