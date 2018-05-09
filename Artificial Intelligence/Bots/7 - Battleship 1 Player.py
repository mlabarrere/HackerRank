import random
def getListMissedShots(size,grid):
    index=0
    listMissedShots=[]
    for i in range(size):
        for j in range(size):
            if grid[i][j]=="m" or grid[i][j]=="d":
                listMissedShots.append([i,j])
                index=index+1
    
    return listMissedShots

def getListHitShots(size,grid):
    index=0
    listHitShots=[]
    for i in range(size):
        for j in range(size):
            if grid[i][j]=="h":
                listHitShots.append([i,j])
                index=index+1
    return listHitShots


def testShotAlreadyMade(row,col,listShoot): return [row,col] in listShoot

# Shooting Functions
def shootEast(row,col): print(str(row)+" "+str(col+1))
def shootWest(row,col): print(str(row)+" "+str(col-1))
def shootSouth(row,col): print(str(row-1)+" "+str(col))
def shootNorth(row,col): print(str(row+1)+" "+str(col))

# Tests nerowt valid and emptcol cell Function
def eastFree(row,col,grid): return col+1<=size-1 and grid[row][col+1]=="-"
def westFree(row,col,grid): return col-1>=0 and grid[row][col-1]=="-"
def northFree(row,col,grid): return row-1>=0 and grid[row+1][col]=="-"
def southFree(row,col,grid): return row+1<=size-1 and grid[row-1][col]=="-"

def oneHitSpotted(size,grid):
	hit=getListHitShots(size,grid)
	R_hit=hit[0][0]
	C_hit=hit[0][1]
	isShotDone=False
	while not isShotDone:
		rand=random.randint(0, 3)
		if rand == 0 and southFree(R_hit,C_hit,grid):
			shootSouth(R_hit,C_hit)
			isShotDone=True
		elif rand == 1 and northFree(R_hit,C_hit,grid):
			shootNorth(R_hit,C_hit)
			isShotDone=True
		elif rand == 2 and westFree(R_hit,C_hit,grid):
			shootWest(R_hit,C_hit)
			isShotDone=True
		elif rand == 3 and eastFree(R_hit,C_hit,grid):
			shootEast(R_hit,C_hit)
			isShotDone=True

def moreThanOneHit(size,grid):
	hit=getListHitShots(size,grid)
	for i in range(len(hit)):
		R_hit=hit[i][0]
		C_hit=hit[i][1]
		if southFree(R_hit,C_hit,grid):
			shootSouth(R_hit,C_hit)
			break
		elif northFree(R_hit,C_hit,grid):
			shootNorth(R_hit,C_hit)
			break
		elif westFree(R_hit,C_hit,grid):
			shootWest(R_hit,C_hit)
			break
		elif eastFree(R_hit,C_hit,grid):
			shootEast(R_hit,C_hit)
			break

# Is a Hit as been spotted?
def targetAcquired(size,grid): return len(getListHitShots(size,grid))>=1

def fire_at_random(size,board):
    R = random.randint(0, size-1)
    C = random.randint(0, size-1)
    listMissedShots=getListMissedShots(size,board)
    while testShotAlreadyMade(R,C,listMissedShots):
        R = random.randint(0, size-1)
        C = random.randint(0, size-1)
    print(str(R)+" "+str(C))


def huntAndTrackDown(size,grid):
    if targetAcquired(size,grid):
        if len(getListHitShots(size,grid))==1:
            oneHitSpotted(size,grid)
        else:
            moreThanOneHit(size,grid)
    else:
        fire_at_random(size,grid)


if __name__ == "__main__": 
    size = int(raw_input()) 
    board = [[j for j in raw_input().strip()] for i in range(size)]  
    huntAndTrackDown(size, board)

