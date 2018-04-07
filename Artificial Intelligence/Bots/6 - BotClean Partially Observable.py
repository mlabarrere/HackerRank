import random

def getClosestDirtPosition(posx, posy, dimx, dimy, grid):
    bx,by = posx, posy #getBotPosition(n,grid)
    distance=2000000
    for i in range(dimx):
        for j in range(dimy):
            if grid[i][j]=="d" and computeDistance(bx,by,i,j)<distance:
                distance = computeDistance(bx,by,i,j)
                dx = i
                dy = j

    if distance==2000000:
       dx = random.random() * dimx
       dy = random.random() * dimy

    return dx, dy

def computeDistance(bx,by,dx,dy):
    return ((dx-bx)**2+(dy-by)**2)**(0.5) # Eucledian Distance


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


def next_move(posx, posy, board):
    dimx=5
    dimy=5
    grid_rework = [list(x) for x in board]
    i_m, j_m = posx, posy
    i_p, j_p = getClosestDirtPosition(posx, posy, dimx, dimy, grid_rework)
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