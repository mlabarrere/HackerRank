# Day 4: Binomial Distribution I


def fact(n):
    return 1 if n==0 else n*fact(n-1)

def bin_coeff(k,n):
    return fact(n)/(fact(k)*fact(n-k))

def bin_distrib(x,n,p):
    return bin_coeff(x,n)*(p**x)*(1-p)**(n-x)

def cumulative(x,n,p):
    total = 0
    for i in range(x,n+1):
        total += bin_distrib(i,n,p)
    return total

x, y = [float(i) for i in input().strip().split()]

p = x/(x+y)

print(round(cumulative(3,6,p),3))
