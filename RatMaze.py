'''
We need to traverse the 2D aray and avoid cells with 1 - as simple as that!
We can store the node info in a list/set and later traverse it to print our
desired path. We can also use another 2D array and mark it as 1 for our path
cells.

Next up, base condition to exit/return on goal achievement. When we are in 
last cell and that is 0, we reached out goal. Then we need to move one cell
at a time - start with 1st cell move in the row direction, as you find 1 return 
False and move in same column's direction downwards. Keep repeating. The backtrack
here is that as you find 1 while moving in same row i.e. x, you move in column
downward. However, if you find 1 even there, then you backtrack and reset the target 
array's cell to 0 
'''


N=5

def printPath(path):
    print(path)
    # for i in path:
        # for j in i:
        #     print(str(j) + " ")
        # print("")

def isValid(x, y, maze):
    if x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 0: 
        return True
      
    return False

def pathToMaze(maze, x, y, path):
    if x==N-1 and y==N-1 and maze[x][y]==0:
        #path[x][y] = 1
        path.append((x,y))
        return True
    
    if isValid(x, y, maze):
        #path[x][y] = 1
        path.append((x,y))
        if pathToMaze(maze, x+1, y, path):
            return True

        if pathToMaze(maze, x, y+1, path):
            return True  

        #path[x][y]=0
        path.remove((x,y))
        return False

def findPath(maze):

    #path = [[0 for i in range(5)]for j in range(5)]
    path = []

    if pathToMaze(maze, 0, 0, path):
        printPath(path)
    
    return True


if __name__=='__main__':

    maze = [[0, 1, 0, 1, 1], 
            [0, 0, 0, 0, 0], 
            [1, 0, 1, 0, 1], 
            [0, 0, 1, 0, 0], 
            [1, 0, 0, 1, 0] 
            ]



    findPath(maze)
