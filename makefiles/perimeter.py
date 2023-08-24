#!/usr/bin/python3
"""
5-main
"""

def island_perimeter(grid):
	"""
	Defines the perimeter of a given grid
	"""
    rows = len(grid)
    cols = len(grid[0])
    
    perimeter = 0
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                
                # Check adjacent cells and reduce perimeter accordingly
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2
                    
    return perimeter



grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
print(island_perimeter(grid))
