
board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
    ]


#based on backtracking algorithm
def solve(bo):
    find = find_empty(bo)
    if not find:
        return True #base condition (when no more empty cubes)
    else:
        row,col = find

    for i in range(1,10):
        if validate(bo, i, (row,col)):
            bo[row][col]=i

            if solve(bo):
                return True

            bo[row][col]=0 #inserting 0 in previous empty cubes
    return False


def validate(bo, num, pos): #board, value, pos=(i,j)
    for i in range(len(bo[0])): #checking rows
        if bo[ pos[0] ] [i]==num and pos[1]!=i: #row=pos[0] and col=i
            return False

    for i in range(len(bo)): #checking cols
        if bo[i][ pos[1] ]==num and pos[1]!=i: #i=row, col=pos[1]
            return False

    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3, box_y*3+3):
        for j in range(box_x*3, box_x*3+3):
            if bo[i][j]==num and (i,j)==pos:
                return False
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0:
            print("- - - - - - - - - - - - ")
        for j in range(len(bo[0])): #iterating row and printing numbers
            if j%3==0 and j!=0: #if index is divisible by 3 than print '|' along with number
                print(' | ', end="")

            if j==8:
                print(bo[i][j]) #dont add further spaces after last column
            else:
                print(str(bo[i][j])+" ", end="") #print in single line


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0: #0 indicate empty space
                return (i,j) #return position

print_board(board)
solve(board)
print('\n\n\n\n')
print_board(board)
