import sys
import unittest

import PyQt6
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QLabel, QGraphicsView, QGraphicsScene
from main import MainWindow
from ui import UI
from grid import Grid
from clickableLabel import ClickableLabel

app = QApplication(sys.argv)

class TestMain(unittest.TestCase):

    window = MainWindow()

    def test_rotatePipes(self):
        # Test that the pipe rotation angle is correctly updated after calling the rotatePipes method.
        expected_result = self.window.pipeRotation + 90 if self.window.pipeRotation != 270 else 0
        self.window.rotatePipes()
        actual_result = self.window.pipeRotation
        self.assertEqual(expected_result, actual_result)

    def test_getGrid(self):
        # Test that the getGrid method returns a non-None object.
        self.assertIsNotNone(self.window.getGrid())

class TestUI(unittest.TestCase):
    window = MainWindow()
    ui = UI(window)

    def test_notice_label(self):
        # Test if the notice label is an instance of QLabel and contains the correct text
        notice = self.ui.leftLayout.itemAt(0).widget()
        self.assertIsInstance(notice, QLabel)
        self.assertIn("Instructions", notice.text())

    def test_rotate_button(self):
        # Test if the rotate button is an instance of QPushButton, contains the correct text and size
        rotate_button = self.ui.main.rotateButton
        self.assertIsInstance(rotate_button, QPushButton)
        self.assertEqual(rotate_button.text(), "Rotate")
        self.assertEqual(rotate_button.size(), PyQt6.QtCore.QSize(100, 60))

    def test_pipe_buttons(self):
        # Test if the pipe buttons are an instance of ClickableLabel and there are four of them
        pipe_buttons = self.ui.main.pipeButtons
        self.assertEqual(len(pipe_buttons), 4)
        for button in pipe_buttons:
            self.assertIsInstance(button, ClickableLabel)

    def test_clear_button(self):
        # Test if the clear button is an instance of QPushButton, contains the correct text and size
        clear_button = self.ui.main.clearButton
        self.assertIsInstance(clear_button, QPushButton)
        self.assertEqual(clear_button.text(), "Clear Grid!")
        self.assertEqual(clear_button.size(), PyQt6.QtCore.QSize(100, 60))

    def test_grid(self):
        # Test if the grid object is an instance of Grid
        grid = self.ui.grid
        self.assertIsInstance(grid, Grid)

    def test_start_input(self):
        # Test if the start input is an instance of QLineEdit, has a corresponding label and contains the correct text
        start_input = self.ui.leftLayout.itemAt(1).layout().itemAt(0).itemAt(1).widget()
        start_label = self.ui.leftLayout.itemAt(1).layout().itemAt(0).itemAt(0).widget()
        self.assertIsInstance(start_input, QLineEdit)
        self.assertIsInstance(start_label, QLabel)
        self.assertIn("Set pressure for starting point (kPa):", start_label.text())

    def test_end_input(self):
        # Test if the end input is an instance of QLineEdit, has a corresponding label and contains the correct text
        end_input = self.ui.leftLayout.itemAt(2).layout().itemAt(0).itemAt(1).widget()
        end_label = self.ui.leftLayout.itemAt(2).layout().itemAt(0).itemAt(0).widget()
        self.assertIsInstance(end_input, QLineEdit)
        self.assertIsInstance(end_label, QLabel)
        self.assertIn("Set pressure for end point (kPa):", end_label.text())

class TestGrid(unittest.TestCase):
    window = MainWindow()
    ui = UI(window)

    def test_init(self):
        # Test initialization of the grid

        grid = self.ui.grid
        self.assertIsInstance(grid, QGraphicsView)
        self.assertEqual(grid.width, 750)
        self.assertEqual(grid.height, 750)
        self.assertEqual(grid.square_size, 75)
        self.assertIsInstance(grid.scene, QGraphicsScene)
        self.assertIsInstance(grid.startPoints, list)
        self.assertIsInstance(grid.endPoints, list)
        self.assertIsInstance(grid.squares, list)
        self.assertEqual(len(grid.startPoints), len(grid.endPoints))
        self.assertEqual(len(grid.squares), (750//75) * (750//75))

    def test_removeCalcPoint(self):
        # Test removing a start or end point from the grid
        grid = self.ui.grid
        start = grid.startPoints[0]
        end = grid.endPoints[0]
        grid.setPoint(start, '../Images/Start.png', "start")
        grid.setPoint(end, '../Images/End.png', "end")
        grid.removeCalcPoint("start")
        grid.removeCalcPoint("end")

    def test_getHeights(self):
        # Test getting the height position of the start and end points
        grid = self.ui.grid
        start = grid.startPoints[0]
        end = grid.endPoints[0]
        grid.setPoint(start, '../Images/Start.png', "start")
        grid.setPoint(end, '../Images/End.png', "end")
        heights = grid.getHeights()
        self.assertEqual(len(heights), 2)
        self.assertIn(grid.currentStart.getHeightPosition(), heights)
        self.assertIn(grid.currentEnd.getHeightPosition(), heights)

    def test_setPipe(self):
        # Test setting a pipe on a grid square
        grid = self.ui.grid
        # squares index needs to be between 9 - 89 due to the rest of the squares being used for calcpoints
        square = grid.squares[10]
        grid.setPipe(square.pipe, square)
        square.setEmpty(False)
        items = grid.scene.items()
        self.assertIn(square.pipe, items)

    def test_removePipe(self):
        # Test removing a pipe from the grid
        grid = self.ui.grid
        square = grid.squares[10]
        pipe = square.pipe
        grid.setPipe(pipe, square)
        square.setEmpty(False)
        grid.removePipe(pipe)
        square.setEmpty(True)
        items = grid.scene.items()
        self.assertNotIn(pipe, items)

    def test_setType(self):
        # Test setting the type of pipe to use
        grid = Grid(400, 400, 20)
        grid.setType("../Images/CurvedPipe.png")
        self.assertEqual(grid.pipeType, "../Images/CurvedPipe.png")

    def test_rotate(self):
        # Test rotating the pipe
        grid = Grid(400, 400, 20)
        grid.rotate(90)
        self.assertEqual(grid.pipeRotation, 90)

    def test_setPoint(self):
        # Test setting a start or end point on the grid
        grid = self.ui.grid
        square1 = grid.squares[12]
        square2 = grid.squares[13]

        # Set start point
        grid.setPoint(square1, "../Images/Start.png", "start")
        self.assertIsNotNone(grid.currentStart)  # Check that currentStart was set
        self.assertEqual(grid.currentStart.getSquare(), square1)  # Check that the square is correct
        self.assertEqual(len(grid.startPoints), 10)

        # Set end point
        grid.setPoint(square2, "../Images/End.png", "end")
        self.assertIsNotNone(grid.currentEnd)  # Check that currentEnd was set
        self.assertEqual(grid.currentEnd.getSquare(), square2)  # Check that the square is correct
        self.assertEqual(len(grid.endPoints), 10)

    def test_pickNSquares(self):
        grid = self.ui.grid

        # Pick 5 squares
        squares = grid.pickNSquares(5)

        # Check that there are 5 squares
        self.assertEqual(len(squares), 5)

        # Pick 10 squares
        squares = grid.pickNSquares(10)

        # Check that there are only 100 squares
        self.assertTrue(len(squares) <= 100)

        # Check that none of the squares are in the start or end points
        for square in squares:
            self.assertNotIn(square, grid.startPoints)
            self.assertNotIn(square, grid.endPoints)

    def test_Grid(self):
        self.pipeCount = 0
        grid = self.ui.grid

        for square in grid.pickNSquares(3):
            grid.setPipe(square.pipe, square)

        for item in grid.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.pipeCount += 1

        # test if correct amount of pipes are in grid
        self.assertEqual(self.pipeCount, 3)

        grid.clearGrid()

        self.pipeCount = 0
        for item in grid.scene.items():
            # Gets the name of the class to check if it is a pipe and removes it
            if item.__class__.__name__ == 'GridPipe':
                self.pipeCount += 1

        # test if the grid really did get cleared
        self.assertEqual(self.pipeCount, 0)

        grid.clearGrid()

if __name__ == "__main__":
    unittest.main()