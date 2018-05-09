# Day 4: Geometric Distribution II

a,b = map(float,input().split())
p = a/b
q = 1 - p
n = int(input())

g=0;
for i in range(1,n+1):
    g += (q**(i-1))*p



print(round(g,3))