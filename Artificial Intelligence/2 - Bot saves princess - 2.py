#!/usr/bin/python
def getPrincessPosition(n,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="p":
                return i, j

def getMarioPosition(n,grid):
    for i in range(n):
        for j in range(n):
            if grid[i][j]=="m":
                return i, j

def moveHorizon(x):
    if(x<0):
        return "LEFT"
    else:
        return "RIGHT"

def moveVertical(y):
    if(y<0):
        return "UP"
    else:
        return "DOWN"

def nextMove(n,r,c,grid):
    grid_rework = [list(x) for x in grid]
    i_m, j_m = getMarioPosition(n,grid_rework)
    i_p, j_p = getPrincessPosition(n,grid_rework)
    x=i_p-i_m
    y=j_p-j_m
    if(x==0):
        return moveHorizon(y)
    else:
        return moveVertical(x)

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
