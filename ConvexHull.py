import numpy as np

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
    if y[i] > left[2] or y[i] > right[2]:
        Upper.append(i)
    if y[i] < left[2] or y[i] < right[2]:
        Lower.append(i)

while True:
    Current = left[0]
    for i in range(0,len(Upper))
        savedSlope = (0,0)
        if x[i] > x[current]:
            slope = (y[i]-y[current])/(x[i] - x[current])
            if savedSlope[0] <= slope:
                savedSlope = (slope,i)
