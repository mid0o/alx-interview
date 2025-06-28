#!/usr/bin/python3
"""
This module contains the function to calculate the perimeter of an island.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in the grid.

    The function iterates through each cell of the grid. If a cell is land (1),
    it adds 4 to the perimeter and then subtracts 2 for each adjacent
    land cell (above or to the left) to account for shared internal edges.

    Args:
        grid (list of list of int): A 2D list representing the grid,
                                    where 0 is water and 1 is land.
                                    The grid is rectangular, and the island
                                    has no "lakes".

    Returns:
        int: The total perimeter of the island. Returns 0 if no island.
    """
    if not grid or not grid[0]:
        return 0

    height = len(grid)
    width = len(grid[0])
    perimeter = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                # Start by adding the full perimeter of a square for a land cell
                perimeter += 4

                # If the cell above is also land, subtract 2 because they
                # share an edge (one side for the current cell, one for the
                # cell above are now internal, not perimeter).
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2

                # Similarly, if the cell to the left is also land, subtract 2.
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2

    return perimeter
