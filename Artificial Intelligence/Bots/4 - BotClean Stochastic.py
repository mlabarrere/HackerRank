def getClosestDirtPosition(posr, posc,grid):
    n=5
    bx,by = posr, posc #getBotPosition(n,grid)
    distance=20000
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="d" and computeDistance(bx,by,i,j)<distance:
                distance = computeDistance(bx,by,i,j)
                dx = i
                dy = j
    return dx, dy

def computeDistance(bx,by,dx,dy):
    return ((dx-bx)**2+(dy-by)**2)**(0.5)


def getBotPosition(n,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="b":
                return i,j


def moveHorizon(x):
    if(x<0):
        print("LEFT")
    else:
        print("RIGHT")


def moveVertical(y):
    if(y<0):
        print("UP")
    else:
        print("DOWN")


def next_move(posr, posc, board):
    n=5
    grid_rework = [list(x) for x in board]
    #i_m, j_m = getBotPosition(n,grid_rework)
    i_m, j_m = posr, posc
    i_p, j_p = getClosestDirtPosition(posr, posc,grid_rework)
    x=i_p-i_m
    y=j_p-j_m
    
    if(x==0 and y==0): 
        print("CLEAN")
    
    elif(x==0):
        return moveHorizon(y)
    
    else:
        return moveVertical(x)

# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)