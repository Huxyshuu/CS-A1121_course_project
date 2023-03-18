from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6 import QtWidgets, QtGui


class Pipes(QGraphicsPixmapItem):
    def __init__(self, pipeType):
        super(Pipes, self).__init__()

        self.type = pipeType  # Determines which type of pipe is drawn

        # self.setPixmap(QPixmap('fish.png'))