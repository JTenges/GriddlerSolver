import unittest
from solver import MyGrid
class TestMyGrid(unittest.TestCase):

    def test_getColumnBlocks(self):
        columns = [
            [1],
            [1]
        ]

        rows = [
            [1],
            [1]
        ]
        
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.getColumnBlocks(0), [])

        grid = [
            [True, False],
            [False, True]
        ]
        myGrid = MyGrid(rows, columns, grid=grid)
        self.assertEqual(myGrid.getColumnBlocks(0), [1])

        columns = [
            [1]
        ]

        rows = [
            [1]
        ]

        grid = [
            [True]
        ]
        myGrid = MyGrid(rows, columns, grid=grid)
        self.assertEqual(myGrid.getColumnBlocks(0), [1])

    def test_columnsSolved(self):
        columns = [
            [1],
            [1]
        ]

        rows = [
            [1],
            [1]
        ]
        
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.columnsSolved(), False)

        grid = [
            [True, False],
            [False, True]
        ]
        myGrid = MyGrid(rows, columns, grid=grid)
        self.assertEqual(myGrid.columnsSolved(), True)

        columns = [
            [1]
        ]

        rows = [
            [1]
        ]

        grid = [
            [True]
        ]
        myGrid = MyGrid(rows, columns, grid=grid)
        self.assertEqual(myGrid.columnsSolved(), True)
    
    def test_placeNextBlock(self):
        columns = [
            [1]
        ]

        rows = [
            [1]
        ]
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.grid, [[False]])
        myGrid.placeNextBlock(0)
        self.assertEqual(myGrid.grid, [[True]])
        self.assertEqual(myGrid.remainingRows, [])

        columns = [
            [1],
            [1]
        ]
        rows = [
            [1],
            [1]
        ]
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.grid, [[False, False], [False, False]])
        self.assertEqual(myGrid.remainingRows, [[1], [1]])
        myGrid.placeNextBlock(0)
        self.assertEqual(myGrid.grid, [[True, False], [False, False]])
        self.assertEqual(myGrid.remainingRows, [[1]])

        myGrid.placeNextBlock(0)
        self.assertEqual(myGrid.grid, [[True, False], [True, False]])
        self.assertEqual(myGrid.remainingRows, [])

    def test_undo(self):
        columns = [
            [1],
            [1]
        ]
        rows = [
            [1],
            [1]
        ]
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.grid, [[False, False], [False, False]])
        self.assertEqual(myGrid.remainingRows, [[1], [1]])
        myGrid.placeNextBlock(0)
        self.assertEqual(myGrid.grid, [[True, False], [False, False]])
        self.assertEqual(myGrid.remainingRows, [[1]])

        myGrid.undo()
        self.assertEqual(myGrid.grid, [[False, False], [False, False]])
        self.assertEqual(myGrid.remainingRows, [[1], [1]])

        columns = [
            [1],
            [1],
            [1]
        ]
        rows = [
            [1],
            [1],
            [1]
        ]

        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.grid, [[False, False, False], [False, False, False], [False, False, False]])
        self.assertEqual(myGrid.remainingRows, [[1], [1], [1]])
        myGrid.placeNextBlock(0)
        myGrid.placeNextBlock(0)
        myGrid.undo()
        myGrid.undo()
        self.assertEqual(myGrid.grid, [[False, False, False], [False, False, False], [False, False, False]])
        self.assertEqual(myGrid.remainingRows, [[1], [1], [1]])

    
    def test_validRowIndexes(self):
        columns = [
            [1],
            [1]
        ]
        rows = [
            [1],
            [1]
        ]
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.validRowIndexes(), range(0, 2))

        columns = [
            [1],
            [1],
            [1]
        ]
        rows = [
            [1, 1],
            [1],
            [1]
        ]
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.validRowIndexes(), range(0, 1))

        columns = [
            [],
            [],
            [],
            [],
            []
        ]
        rows = [
            [1, 1, 1]
        ]
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.validRowIndexes(), range(0, 1))

        columns = [
            [],
            [],
            [],
            [],
            []
        ]
        rows = [
            [1, 1]
        ]
        grid = [[True, False, False, False, False]]
        myGrid = MyGrid(rows, columns, grid=grid)
        self.assertEqual(myGrid.validRowIndexes(), range(2, 3))

        columns = [
            [],
            [],
            [],
            [],
            [],
            []
        ]
        rows = [
            [1, 2]
        ]
        grid = [[True, False, False, False, False, False]]
        myGrid = MyGrid(rows, columns, grid=grid)
        self.assertEqual(myGrid.validRowIndexes(), range(2, 3))

        
    
    def test_isSafePlacement(self):
        columns = [
            [1],
            [1]
        ]
        rows = [
            [1],
            [1]
        ]
        myGrid = MyGrid(rows, columns)
        self.assertEqual(myGrid.isSafePlacement(0, 1), True)

        columns = [
            [1],
            [1]
        ]
        rows = [
            [1]
        ]
        grid = [
            [False, False],
            [True, False]
        ]
        myGrid = MyGrid(rows, columns, grid=grid)
        self.assertEqual(myGrid.isSafePlacement(0, 1), False)
    
    def test_copy(self):
        columns = [
            [1],
            [1]
        ]
        rows = [
            [1],
            [1]
        ]
        myGrid1 = MyGrid(rows, columns)
        myGrid2 = myGrid1.copy()
        self.assertEqual(myGrid1.remainingRows == myGrid2.remainingRows, True)
        self.assertEqual(myGrid1.remainingRows is myGrid2.remainingRows, False)
        self.assertEqual(myGrid1.columnConditions == myGrid2.columnConditions, True)
        self.assertEqual(myGrid1.columnConditions is myGrid2.columnConditions, False)
        self.assertEqual(myGrid1.grid == myGrid2.grid, True)
        self.assertEqual(myGrid1.grid is myGrid2.grid, False)
        self.assertEqual(myGrid1.currentRowIndex == myGrid2.currentRowIndex, True)
    

if __name__ == '__main__':
    unittest.main()