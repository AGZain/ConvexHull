import numpy as np
import matplotlib.pyplot as plt

x = [3,4,6,4,2,3,5]
y = [2,1,3,7,4,5,4]

left = (0,float(x[0]),float(y[0]))
right = (1,float(x[1]),float(y[1]))

for i in range(0,len(x)):
    x[i] = float(x[i])
    y[i] = float(y[i])
    if x[i] < left[1]:
        left = (i, x[i], y[i])
    if x[i] > right[1]:
        right = (i, x[i], y[i])

print(left)
print(right)
Upper = []
Lower = []

for i in range(0,len(x)):
    if i == left[0]:
        continue
    if y[i] > left[2] or y[i] > right[2]:
        Upper.append(i)
    if y[i] < left[2] or y[i] < right[2]:
        Lower.append(i)
print(Upper)
line = []
line.append(left[0])
Upper.append(right[0])
Lower.append(left[0])
print("Upper:")
print(Upper)
Current = left[0]
#for the Upper half
for z in range(0,len(Upper)):

    savedSlope = (-999.,0)
    print("New Loop! " + str(len(Upper)))
    for i in Upper:
        print(i)
        print("Looking at: " + str(x[i]) + "   " + str(y[i]))
        if x[i] > x[Current]:
            slope = (y[i]-y[Current])/(x[i] - x[Current])
            print(slope)
            if savedSlope[0] < slope:
                savedSlope = (slope,i)
                Current = i
                print(str(x[i]) + "GOOD " + str(y[i]))
            #Need to look at other side of slope too. Will add later
    line.append(savedSlope[1])

    if Current == right[0]:
        break

    Upper.remove(savedSlope[1])
lineBottom = []
lineBottom.append(right[0])
print(line)
Current = right[0]
#For the bottom half:
print("LOWER ISsssssssssssssssssssssssssssssssssssssssssss")
print(Lower)
for z in range(0,len(Lower)):

    savedSlope = (-99999.,-1)
    print("New Loop! Lower:  " + str(len(Lower)))
    for i in Lower:
        print(i)
        print("Looking at: " + str(x[i]) + "   " + str(y[i]))
        if x[i] < x[Current]:
            slope = (y[i]-y[Current])/(x[i] - x[Current])
            print("SLOPE IS..")
            print(slope)
            if savedSlope[0] < slope:
                savedSlope = (slope,i)
                print(str(x[i]) + "GOOD " + str(y[i]))
            #Need to look at other side of slope too. Will add later
    lineBottom.append(savedSlope[1])


    if savedSlope[1] != -1:
        Current = savedSlope[1]
        Lower.remove(savedSlope[1])
    if Current == left[0] or len(Lower) == 0:
        break
print(lineBottom)
plt.scatter(x,y,marker='o')
i = 0
while i < len(line)-1:
    plt.plot([x[line[i]],x[line[i+1]]],[y[line[i]],y[line[i+1]]],'r--')
    i +=1

i = 0
while i < len(lineBottom)-1:
    plt.plot([x[lineBottom[i]],x[lineBottom[i+1]]],[y[lineBottom[i]],y[lineBottom[i+1]]],'r--')
    i +=1
plt.show()
