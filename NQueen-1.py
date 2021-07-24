'''
N Queens

For checking if it's safe to place:
    1. Check in horizontal i.e. row i in range(r)
    2. Check horizontal left downwards i.e. i=i-1, j=j+1
    3. Check horizontal left upwards i.e. i=i-1, j=j-1
No need to check in vertical as we will never be placing 2 queens in same column.
Iterate row wise. Start with row 0
Check in each row, if queen can be placed in any columncheck if it's safe to place(), if not backtrack
Recurse with row+1
Base condition - row>=N


'''
N = 4
board = [['.' for i in range(N)] for j in range(N)]

def safe_to_place(board, r, c):
    
    for i in range(r):
        if board[i][c] == 'Q':
            return False

    (i,j) = (r,c)
    while i>=0 and j >=0:
        if board[i][j]=='Q':
            return False
        i= i-1
        j= j-1
    
    (i,j) = (r,c)
    while i>=0 and j <N:
        if board[i][j]=='Q':
            return False
        i= i-1
        j= j+1
    
    return True

def find_queen(board, row):
    if row>=N:
        for i in range(N):
            for j in range(N):
                print(board[i][j], end=' ')
            print()
        print()
        return
        
    for col in range(N):
        if safe_to_place(board, row, col):
            board[row][col] = 'Q'
            find_queen(board, row+1)
            board[row][col] = '.'
            
find_queen(board, 0)