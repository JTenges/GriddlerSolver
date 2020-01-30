import unittest
from solver import MyGrid
from solver import isSolvable
import time
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
    
    def test_solver_trivial(self):
        columns = [
            [1],
            [1],
            [1]
        ]

        rows = [
            [1, 1],
            [1]
        ]
        myGrid = MyGrid(rows, columns)
        isSolvable(myGrid)
    
    def test_solver_small1(self):
        t = time.time()

        columns = [
            [2],
            [2, 3],
            [1, 3, 2],
            [2, 2, 1],
            [1, 5, 1],
            [1, 1, 11],
            [1, 5, 1],
            [5, 2],
            [1, 3, 3],
            [2, 3],
        ]

        rows = [
            [1],
            [1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [3, 3],
            [1, 5],
            [7],
            [5],
            [3],
            [2, 3],
            [3, 1, 1],
            [3, 1, 2],
            [2, 3],
            [4],
            [1],
            [1],
        ]

        myGrid = MyGrid(rows, columns)
        self.assertEqual(isSolvable(myGrid), True)
        print(time.time() - t)
    
    def test_solver_small2(self):
        t = time.time()

        columns = [
            [2],
            [5],
            [4, 2],
            [1, 1, 1, 7, 2],
            [14, 2],
            [4, 2],
            [5],
            [2],
        ]

        rows = [
            [2],
            [1],
            [2],
            [1],
            [1],
            [2],
            [1],
            [2],
            [2],
            [2],
            [2],
            [4],
            [4],
            [6],
            [2, 2],
            [2, 2],
            [3, 3],
            [6],
            [2],
        ]

        myGrid = MyGrid(rows, columns)
        self.assertEqual(isSolvable(myGrid), True)
        print(time.time() - t)
    
    
    def test_solver_small3(self):
        t = time.time()

        columns = [
            [5],
            [1, 1, 1],
            [3, 1],
            [1, 1, 1],
            [5],
        ]

        rows = [
            [5],
            [1, 1, 1],
            [5],
            [1, 1],
            [5],
        ]

        myGrid = MyGrid(rows, columns)
        self.assertEqual(isSolvable(myGrid), True)
        print(time.time() - t)

    def test_solver_medium1(self):
        t = time.time()
        rows = [
            [4],
            [2, 2, 5],
            [3, 3, 2, 2],
            [2, 2, 2, 2, 2],
            [14, 2, 3],
            [6, 1, 5, 5],
            [2, 1, 2, 2, 3, 3, 2],
            [6, 1, 2, 2],
            [1, 3, 1, 2],
            [1, 5, 2],
            [2, 9, 3],
            [1, 1, 4, 8],
            [6, 3, 1, 4],
            [2, 1, 1, 2, 1, 2],
            [5, 2],
        ]

        columns = [
            [1],
            [2],
            [4],
            [4],
            [2],
            [1, 4, 3],
            [4, 4, 2],
            [4, 2, 2],
            [4, 1],
            [4, 4, 2],
            [4, 7],
            [1, 3, 3],
            [2, 3],
            [3, 3],
            [4, 3],
            [2, 3],
            [1, 2],
            [1, 2, 1],
            [2, 2, 4],
            [2, 2, 1, 2],
            [2, 2, 1, 1],
            [2, 2, 4],
            [2, 2, 3],
            [15],
            [15],
        ]

        myGrid = MyGrid(rows, columns)
        isSolvable(myGrid)
        print(time.time() - t)
    
    def test_solver_large1(self):
        t = time.time()
        columns = [
            [8],
            [9],
            [7, 3],
            [8, 2],
            [8, 2],
            [10, 2, 1, 1],
            [9, 5, 2],
            [9, 10],
            [9, 6, 2],
            [9, 11],
            [6, 2, 4, 7, 2],
            [9, 1, 3, 7, 2],
            [13, 9, 1],
            [5, 17, 1],
            [1, 4, 14, 1],
            [2, 4, 12, 1],
            [1, 4, 8],
            [1, 5, 4],
            [1, 5],
            [1, 5],
            [1, 4],
            [1, 4],
            [1, 3],
            [1, 2],
            [1, 1],
        ]

        rows = [
            [5],
            [4, 10],
            [5],
            [15],
            [14],
            [3, 9],
            [4, 7],
            [3, 3],
            [4],
            [4],
            [4, 4],
            [12],
            [5, 5],
            [8, 4],
            [9, 5],
            [16],
            [9, 6],
            [8, 7],
            [8, 7],
            [6, 7],
            [6, 9],
            [4, 9],
            [2, 10],
            [13],
            [4, 5],
            [3, 5],
            [2, 1, 1],
            [1, 1, 1],
            [6],
            [11],
        ]
        myGrid = MyGrid(rows, columns)
        isSolvable(myGrid)
        print(time.time() - t)
    


    

if __name__ == '__main__':
    unittest.main()