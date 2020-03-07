def printGrid(grid):
    for i in range (0,9):
        print(grid[i])
    return

def find_empty(arr,l):
    for row in range (0,9):
        for column in range (0,9):
            if(arr[row][column]==0):
                l[0]=row
                l[1]=column
                return True
    return False

def check_col(arr,col,num):
    for i in range (0,9):
        if(arr[i][col]==num):
            return True
    return False

def check_row(arr,row,num):
    for j in range (0,9):
        if(arr[row][j]==num):
            return True
    return False

def check_box(arr,row,col,num):
    for i in range (0,3):
        for j in range (0,3):
            if(arr[i+row][j+col]==num):
                return True
    return False
    

def check_location_safe(arr,row,col,num):
    return not check_col(arr,col,num) and not check_row(arr,row,num) and not check_box(arr,row-row%3,col-col%3,num)
    
    

    
def solveSudoko(arr):
    l=[0,0]
    if(not find_empty(arr,l)):
        return True
    row=l[0]
    col=l[1]
    for num in range (1,10):
        if(check_location_safe(arr,row,col,num)):
            arr[row][col]=num
            if(solveSudoko(arr)):
                return True

            arr[row][col]=0
            
    return False


grid=[[3,0,6,5,0,8,4,0,0],
       [5,2,0,0,0,0,0,0,0],
       [0,8,7,0,0,0,0,3,1],
       [0,0,3,0,1,0,0,8,0],
       [9,0,0,8,6,3,0,0,5],
       [0,5,0,0,9,0,6,0,0],
       [1,3,0,0,0,0,2,5,0],
       [0,0,0,0,0,0,0,7,4],
       [0,0,5,2,0,6,3,0,0]]


"""
grid=[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
"""
if(solveSudoko(grid)):
    printGrid(grid)
else:
    print("no solution exists")





# reference:
#https://www.geeksforgeeks.org/sudoku-backtracking-7/
