import unittest
from geometry.maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
    def test_reset_visited(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10,None,1)
        visited = 0
        for i in range(num_cols):
            for j in range(num_rows):
                if m1._cells[i][j].visited:
                    visited += 1
        self.assertEqual(visited,0)



if __name__ == "__main__":
    unittest.main()
