#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    x=0
    y=0
    if a0 > b0 : 
        x=x+1
    elif a0 < b0:
        y=y+1
    if a1 > b1 : 
        x=x+1
    elif a1 < b1:
        y=y+1
    if a2 > b2 : 
        x=x+1
    elif a2 < b2:
        y=y+1
    
    return x, y
    
    # Complete this function

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))


