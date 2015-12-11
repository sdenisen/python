__author__ = 'sdenisenko'
from math import sqrt

def getDivisors(n):
    divisors = []
    for i in range(2, sqrt(n)):
        if n%i:
            divisors.append(i)
    return divisors


def getTriangleNumebr(n):
    return (1/2)*n*(n-1)

def findElement():
    pass
s = 1
f = 100

while(True):
    t = getTriangleNumebr(n)
    lenght = getDivisors(t).__len__()
    if lenght < 500:

    elif lenght>=500:
        pass





