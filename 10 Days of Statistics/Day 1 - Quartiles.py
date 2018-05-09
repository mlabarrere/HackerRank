# Day 1: Quartiles

def median(arr):
    if len(arr)%2 == 0:
        median = (arr[(len(arr)//2)]+arr[(len(arr)//2-1)])//2
    else:
        median = arr[(len(arr)//2)]
    return(median)

N = int(input())
X = list(map(int, input().strip().split(' ')))
X.sort()
Q1, Q2, Q3 = median(X[:(N//2)]), median(X), median(X[(N//2):] if len(X)%2==0 else X[(1+N//2):])

print(Q1)
print(Q2)
print(Q3)