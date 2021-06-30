'''
The key here is how the knight moves. It moves 2 moves horizontally or vertically 
and then 1 move vertically or horizontally respectively. Based on that considering
the chess board as a graph of x and y axis, create a list of possible movements along
x i.e. row and create a corresponding y list i.e. col wrt each move. This way, we will 
have 8 possible moves from any given cell.

Base condition is new cell is the destination cell, then return the moves.

Next, we need to move the knight using the 8 possible moves from any position, so for
loop wil run 8 times. To keep track of the 8 new positions, we need a queue. However,
dequeue being efficient than queue, we will use that as we can pop from both ends. We 
need to ensure that new position is valid(not out of the board) then add it to queue.
However an important thing is we should handle the case of not repeating the cell, if it
has already been considered - best thing is to keep a visited set to keep track of cells
that have already been visited. So, we can start from the source -> check if it has been 
cisited -> if not add it to visited -> if yes, then move to next item in queue -> after
adding to visited, create the new cell positions from the current cell using 8 possible
moves. For each new cell check if it is valid and then add to queue. Repeat until queue
is empty, however as it's guaranteed that a result will always be there so we will get the
result before queue is empty.

'''
from collections import deque

# class Node:

#     def __init__(self, x, y, dist=0):
#         self.x = x
#         self.y = y
#         self.dist = dist
    
#     def __hash__(self):
#         return hash((self.x, self.y, self.dist))
    
#     def __eq__(self, other):
#         return (self.x, self.y, self.dist) == (other.x, other.y, other.dist)
    

row = [2, 2, -2, -2, 1, 1, -1, -1]
col = [-1, 1, 1, -1, 2, -2, 2, -2]

the_q = deque()
visited = set() 

def isValid(x, y, N):
    return not (x<0 or y<0 or x>=N or y>=N)

def find_pos(src, dest, N):
    
    the_q.append(src)

    while the_q:
        node = the_q.popleft()
        # dist = node.dist
        dist = node[2]

        # if node.x==dest.x and node.y==dest.y:
        if node[0]==dest[0] and node[1]==dest[1]:
            return dist

        if node not in visited:
            visited.add(node)

            for i in range(8):
                # new_x = node.x + row[i]
                # new_y = node.y + col[i]
                new_x = node[0] + row[i]
                new_y = node[1] + col[i]

                if isValid(new_x, new_y, N):
                    # the_q.append(Node(new_x, new_y, dist+1))
                    the_q.append((new_x, new_y, dist+1))

def main():
    N = 10

    # src = Node(0, 7, 0)
    # dest = Node(7, 0, 0)
    src = (0, 7, 0)
    dest = (7, 0, 0)

    print("Minimum number of steps required is", find_pos(src, dest, N))
    
if __name__=='__main__':
    main()