#!/usr/bin/python
def displayPathtoPrincess(n,grid):
    grid_rework = [list(x) for x in grid]
    i_m = 0
    j_m = 0
    i_p = 0
    j_p = 0
    for i in range(n):
        for j in range(n):
            if grid_rework[i][j]=="p":
                i_p = i
                j_p = j
            if grid_rework[i][j]=="m":
                i_m = i
                j_m = j
    x=i_p-i_m
    y=j_p-j_m
    for i in range(0, abs(x)):
        if(x<0):
            print("UP")
        else:
            print("DOWN")

    for k in range(0,abs(y)):
        if(y<0):
            print("LEFT")
        else:
            print("RIGHT") 
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
