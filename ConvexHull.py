import numpy as np
import matplotlib.pyplot as plt
import csv

x = []
y = []
left = []
right = []
Upper = []
Lower = []
line = []
lineBottom = []

with open('data/example2.csv', 'r', encoding='utf8',errors='ignore') as csvfile:		#Opening up dictionary
    read = csv.reader(csvfile, delimiter=',', quotechar='|')
    count = 0
    for row in read:
        if count == 0:
            count += 1
            continue
        count += 1
        x.append(row[0])
        y.append(row[1])
# x = [2,3,3,4,4,5,3.5,2,5]
# y = [2,3,4,3,4,2,5,3,3]

for i in range(0,len(x)):
    x.append(x[i])
    y.append(y[i])


    left= (0,float(x[0]),float(y[0]))
    right = (1,float(x[1]),float(y[1]))

    for i in range(0,len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])
        if x[i] <= left[1]:
            if x[i] == left[1] and y[i] < left[2]:
                left = (i, x[i], y[i])
            if x[i] < left[1]:
                left = (i, x[i], y[i])
        if x[i] >= right[1]:
            if x[i] == right[1] and y[i] > right[2]:
                right = (i, x[i], y[i])
            if x[i] > right[1]:
                right = (i, x[i], y[i])

    for i in range(0,len(x)):
        if y[i] > left[2] or y[i] > right[2]:
            Upper.append(i)
        else:
            Lower.append(i)
    Upper.append(right[0])
    Lower.append(left[0])
    line.append(left[0])
    lineBottom.append(right[0])


Current = left[0]
for z in range(0,len(Upper)):
    savedSlope = (-999.,-1)
    for i in Upper:
        if x[i] > x[Current]:
            slope = (y[i]-y[Current])/(x[i] - x[Current])
            if savedSlope[0] < slope:
                savedSlope = (slope,i)
        elif(x[i] == x[Current] and y[i] > x[Current]):
            savedSlope = (999999999999999999,i)
    line.append(savedSlope[1])

    if savedSlope[1] != -1:
        Current = savedSlope[1]
        Upper.remove(savedSlope[1])
    if Current == right[0] or len(Lower) == 0:
        break

Current = right[0]

for z in range(0,len(Lower)):

    savedSlope = (-99999.,-1)
    for i in Lower:
        if x[i] < x[Current]:
            slope = (y[i]-y[Current])/(x[i] - x[Current])
            if savedSlope[0] < slope:
                savedSlope = (slope,i)
        elif(x[i] == x[Current] and y[i] < x[Current]):
            savedSlope = (999999999999999999,i)
    lineBottom.append(savedSlope[1])


    if savedSlope[1] != -1:
        Current = savedSlope[1]
        Lower.remove(savedSlope[1])
    if Current == left[0] or len(Lower) == 0:
        break

plt.scatter(x,y,c='b',marker='o')
i = 0
while i < len(line)-1:
    plt.plot([x[line[i]],x[line[i+1]]],[y[line[i]],y[line[i+1]]],'r--')
    i +=1

i = 0
while i < len(lineBottom)-1:
    plt.plot([x[lineBottom[i]],x[lineBottom[i+1]]],[y[lineBottom[i]],y[lineBottom[i+1]]],'r--')
    i +=1
plt.show()
