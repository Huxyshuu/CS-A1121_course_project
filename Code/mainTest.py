import sys
import unittest

from PyQt6.QtWidgets import QApplication
from main import MainWindow


class MainTest(unittest.TestCase):

    def setUp(self):
        self.app = QApplication(sys.argv)

        self.window = MainWindow()
        self.window.show()  # Makes the window visible

        self.grid = self.window.view


    def test_Grid(self):
        self.pipeCount = 0

        for square in self.window.view.pickNSquares(3):
            self.window.view.setPipe(square.pipe, square)

        for item in self.window.view.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.pipeCount += 1

        # test if correct amount of pipes are in grid
        self.assertEqual(self.pipeCount, 3)

        self.window.clearGrid()

        self.pipeCount = 0
        for item in self.window.view.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.pipeCount += 1

        # test if the grid really did get cleared
        self.assertEqual(self.pipeCount, 0)

        self.window.clearGrid()

    def test_Calculator(self):
        # As of 12.04.2023 now only adds the two given parameters together
        self.assertEqual(self.window.calculateFlow(100, 53), 153)
        self.assertEqual(self.window.calculateFlow(120, 53), 173)
        self.assertEqual(self.window.calculateFlow(20310, 53), 20363)
        self.assertNotEqual(self.window.calculateFlow(200, 300), 100)

    # def testWindowVisibility(self):
    #     print("vis")

    def tearDown(self):
        self.window.close()
        del self.app

if __name__ == "__main__":
    unittest.main()