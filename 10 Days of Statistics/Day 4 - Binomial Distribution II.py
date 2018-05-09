# Day 4: Binomial Distribution II


#A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are #incorrectly sized. What is the probability that a batch of 10 pistons will contain:

#    No more than 2 rejects?
#    At least 2 rejects?

# input : 12 10

def fact(n):
    return 1 if n==0 else n*fact(n-1)

def bin_coeff(k,n):
    return fact(n)/(fact(k)*fact(n-k))

def bin_distrib(x,n,p):
    return bin_coeff(x,n)*(p**x)*(1-p)**(n-x)

def cumulative_up(x,n,p):
    total = 0
    for i in range(x,n+1):
        total += bin_distrib(i,n,p)
    return total

def cumulative_down(x,n,p):
    total = 0
    for i in range(x+1):
        total += bin_distrib(i,n,p)
    return total

x, n = [int(i) for i in input().strip().split()]

p = x/100

print(round(cumulative_down(2,n,p),3))
print(round(cumulative_up(2,n,p),3))
