# Day 5: Poisson Distribution I

# Dependencies
from math import factorial
from math import exp

def poisson(k,lam):
    return (lam**k)*exp(-lam)/factorial(k)

average = float(input())
variable = float(input())

# Probability
print(round(poisson(variable, average), 3))
