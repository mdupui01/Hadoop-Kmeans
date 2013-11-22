#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import math

input = sys.stdin.readlines()

mean1 = [0, 15]
mean2 = [30, 15] 
mean1_old = mean1
mean2_old = mean2

X = []
Y = []
muX = []
muY = []
Xs_mean1 = []
Ys_mean1 = []
Xs_mean2 = []
Ys_mean2 = []
for i in range(20):
    Xs_mean1 = []
    Ys_mean1 = []
    Xs_mean2 = []
    Ys_mean2 = []
    
    for line in input:
        data = line.strip().split(",")
        x, y = data
        
        dist_2_mean1 = math.sqrt((mean1[0] - float(x))**2 + (mean1[1] - float(y))**2)
        dist_2_mean2 = math.sqrt((mean2[0] - float(x))**2 + (mean2[1] - float(y))**2)
        
        if dist_2_mean1 > dist_2_mean2:
            Xs_mean2.append(float(x))
            Ys_mean2.append(float(y))
        else:
            Xs_mean1.append(float(x))
            Ys_mean1.append(float(y))
            
    X_mean1 = sum(Xs_mean1)/len(Xs_mean1)
    Y_mean1 = sum(Ys_mean1)/len(Ys_mean1)
    X_mean2 = sum(Xs_mean2)/len(Xs_mean2)
    Y_mean2 = sum(Ys_mean2)/len(Ys_mean2)
    
    mean1 = [X_mean1, Y_mean1]
    mean2 = [X_mean2, Y_mean2]

    if mean1_old == mean1 and mean2_old == mean2:
        break

    mean1_old = mean1
    mean2_old = mean2

print "{0}\t{1}\t{2}".format(1, X_mean1, Y_mean1)
print "{0}\t{1}\t{2}".format(2, X_mean2, Y_mean2)
