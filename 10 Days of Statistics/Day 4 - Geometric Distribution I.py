# Day 4: Geometric Distribution I

a,b = map(float,input().split())
# 'p' is Probability of getting a defective part which is a success
p = a/b
# 'q' is Probability of getting a non defective part which is a failure
q = 1 - p

# No of trials
n = int(input())

# Now the probability that the 1st defect is found during the 5 inspection
# Geometric distribution
g = (q**(n-1))*p
print(round(g,3))