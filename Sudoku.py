'''
Sudoku Solver works as follows - We are considering 9X9 box; below equation will change depending on size of box
1. Each row should have numbers from 1-9
2. Each column should have numbers from 1-9
3. Each 3X3 box should have numbers from 1-9
4. The new number should not be there already in the row
5. The new number should not be there already in the column
6. The new number should not be in that box

Straight away we need to follow this and check each row before putting number, 
each column and then each box. This way things will be very complicated and
inefficient. For simplification we use the extra space strategy and create
3 new lists/arrays to record our observation. We can create a 2D array again 
to replicate the box. However, a smart way would be to create list of dictionaries

Something like this-
[defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1}), 
defaultdict(<class 'int'>, {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1})]

Each entry can be treated as a row for rows list, col for columns list and box index for boxes list

rows - to check if a number is there in that row
cols - to check if a number is there in that column
Boxes - to check if a number is in that box

Box index to calculate index of box - the formula is (row//n)*+col//n
This can be remembered to avoid the long hustle, but the idea is if col
is in the range 0-2, no matter the row value, box number will always be
0, 3, 6. Similarly for 3-5 col, it will be 1, 4, 7

Now the idea is to first populate these lists based on our input board -
wherever you get a number, populate these list of dictionary based on the number

e.g. if 3 is present in 2nd row(1st index) then rows list would look like

[defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {3:1}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {), 
defaultdict(<class 'int'>, {})]

Similarly 3 is present in 5th column, then column list

[defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {3:1}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {}), 
defaultdict(<class 'int'>, {), 
defaultdict(<class 'int'>, {})]

Once the rows are placed as per the original board, then we iterate the board column wise.
Start with row=0, col=0 -> look for '.' in board. If you don't find it, move to next column
in same row. If at last column, then move to next row - Such iteration can be achieved by recursion
calling same function by increasin row or column. The base condition would be if we are in the last
row and last column. If we are there we should turn the flag as True. If we find a '.', start to check
which number from 1 to 9 can placed, so a for loop for 1 to 9. A check if that number can be placed is
needed i.e. if the number is not in rows, column or boxes list. If it is, move to next number in for loop
otherwise start with placing the number - make the number value in the dictionary in each list as 1 
i.e. +1 and place it in that cell in box. If moving the same way we can reach the end row and end column,
well good, return from place_next and susequently return to original bactrack call because sudoku_solved
will be True. However, if at any stage we can't place a number in a cell, then the for loop advances to 
next number and if none of number can be placed that completes that instance of backtrack call from
place_next and eventually completes that call of place_next. 

THIS IS THE IMPORTANT PART(BACKTRACK)-
Upon completion of that call, it returns from where it was called and moves further in code. If
sudoku_solved is False(which it will be as we are not in last row and column), it calls remove_num
and removes that placement from cell and thus completes that instance of call and returns from where 
it was called, and checks with next number in for loop or if needed(for loop completed) then
agains backtraces.
'''


from collections import defaultdict

class Sudoku:
    def solve_sudoku(self, board):

        def place(num, row, col):
            rows[row][num] += 1
            cols[col][num] += 1
            boxes[box_index(row, col)][num] += 1
            box[row][col] = str(num)
        
        def remove_num(num, row, col):
            del rows[row][num] 
            del cols[col][num]
            del boxes[box_index(row, col)][num]
            box[row][col] = '.'
        
        def place_next(row, col):
            if row == N-1 and col == N-1:
                sudoku_solved=True
                return
            
            if col==N-1:
                backtrack(row+1, 0)
            else:
                backtrack(row, col+1)

        def can_place(num, row, col):
            
            return num not in rows[row] and num not in cols[col] and num not in boxes[box_index]
            


        def backtrack(row=0, col=0):

            if board[row][col] == '.':
                for d in range(1, 10):
                    if can_place(d, row, col):
                        place(d, row, col)
                        place_next(row, col)

                        if not sudoku_solved:
                            remove_num(num, row, col)
            else:
                place_next(row, col)


            

        n=3
        N = n*n
        box_index = lambda row, col: (row//n)*n + col//n

        rows = [defaultdict(int) for i in range(N)]
        cols = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]

        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    num = int(board[i][j])
                    place(num, i, j)
        
        sudoku_solved = False
        backtrack()




