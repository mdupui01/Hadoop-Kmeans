#!/usr/bin/python

'''
Mapper for the hadoop k-means algorithm.
'''

import sys

input = sys.stdin.readlines()

muX1 = []
muY1 = []
muX2 = []
muY2 = []
for line in input:
    data_mapped = line.strip().split("\t")
    key, x, y = data_mapped
    
    if key == '1':
        muX1.append(float(x))
        muY1.append(float(y))
    else:
        muX2.append(float(x))
        muY2.append(float(y))

muX1_final = sum(muX1)/len(muX1)
muY1_final = sum(muY1)/len(muY1)
muX2_final = sum(muX2)/len(muX2)
muY2_final = sum(muY2)/len(muY2)

print "{0}\t{1}".format(muX1_final, muY1_final)
print "{0}\t{1}".format(muX2_final, muY2_final)


