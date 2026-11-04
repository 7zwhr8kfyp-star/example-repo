# Lots of help from Copilot!!

grid = [["-", "#", "-", "-", "#"],
["#", "-", "-", "-", "#",],
["-", "-", "-", "-", "-"],
["#", "-", "-", "-", "-"],
["-", "-", "-", "#", "-"]]

     # Function to count '#'s                       
def grid_count(grid,row,col): 
    rows = len(grid) # 5 lists so 5 rows
    cols = len(grid[0]) # Columns is length or 1 row, so 5
    count = 0
    for r in range(row - 1, row + 2): # Checks 1 row above, current row and 1 below.
        for c in range(col - 1, col + 2): # Checks col to left and right, therefore all surrounding cells
            if 0 <= r < rows and 0 <= c < cols: # Make sure r and c are between 0 and 5
                if (r,c) != (row,col): # Dont check current cell.
                    if grid[r][c] == "#": # If surrounding cell has a '#', then add 1 to count
                        count += 1
    return count

for row in range(len(grid)):  #Loops though each row - 0-4
    for col in range(len(grid[0])): # Loops though each col - 0-4
        if grid[row][col] == "-":  # Checks if current cell has a '-' with index.
           grid[row][col] = grid_count(grid,row,col)

for row in grid:
    print(row)        