#run following line to create executable:
#   python -m PyInstaller --onefile xyztodz.py
import numpy
import scipy
import matplotlib
import math
import csv
import sys

#multiple arrays for testing purposes, really only needed line but I was lazy
line = []
xvals = []
yvals = []
zvals = []

filename = input("Name of csv file to convert: ")


#read values
try:
    with open(filename, newline='') as input:
        iterator = csv.reader(input, delimiter=',')
        for row in iterator:
            print(row.copy())
            xvals.append(list(map(int, row))[0])
            yvals.append(list(map(int, row))[1])
            zvals.append(list(map(int, row))[2])
            line.append(list(map(int, row)))
    input.closed
except FileNotFoundError:
        print("Couldn't find your input file. Make sure the name is correct, you did type .csv, and the file is in the same folder as this script!")
        sys.exit()


#print statements for test purposes
"""
print(line)
print(xvals)
print(yvals)
print(zvals)
"""

#find distance values
distvals = []
for x in range(len(xvals)):
    distvals.append(math.sqrt((yvals[x]-yvals[0])**2 + (xvals[x]-xvals[0])**2))

#find azimuth of line
angle = math.degrees(math.atan((yvals[len(xvals)-1]-yvals[0])/(xvals[len(xvals)-1]-xvals[0])))

#write output file
with open('OUT' + filename, 'w', newline='') as output:
    writer = csv.writer(output, delimiter=',')
    for x in range(len(distvals)):
        writer.writerow([distvals[x]] + [zvals[x]])
print('File created as OUT' + filename)
output.closed

#create graph
import matplotlib.pyplot as plt
plt.plot(distvals,zvals)
plt.ylabel('Elevation')
plt.xlabel('Distance along line in ' + str(angle) + '° direction')
plt.show()
