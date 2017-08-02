import math
import time

__author__ = 'sdenisenko'

pentagonals = []

def isPentagonal(n):
    return True

for n in range(1, 10000):
    pentagonals.append(n*(3*n-1)/2)
print "start...."
pentagonalsS = set(pentagonals)
result = []
start = time.time()
conts_len = pentagonals.__len__()
i = 1
while(True):
#for i, tmp in enumerate(pentagonals):
    tmp = pentagonals[i]
    for j in xrange(i, conts_len):

        tmpj = pentagonals[j]
        if  tmpj - tmp in pentagonalsS and tmp + tmpj in pentagonalsS:
            result.append((tmp, tmpj))
    i +=1
    if i == 9999:
        break

stop_time = time.time()
print (start - stop_time)
print result

start = time.time()
for i in range(0, pentagonals.__len__()):
    for j in range(i, pentagonals.__len__()):
        if pentagonals[i] + pentagonals[j] in pentagonals and math.fabs(pentagonals[i] - pentagonals[j]) in pentagonals:
            result.append((pentagonals[i], pentagonals[j]))

stop_time = time.time()
print (start - stop_time)

print result

[(1560090, 7042750)]