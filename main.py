from orbiter import Orbiter
import json

with open('inputs.json', 'r') as f:
    initval = json.load(f)

print(initval)

orbiters = {}

#Time interval
interval = initval['Interval']
#Number of intervals
num = initval['Number of Intervals']
#Displayed values
displayed = initval['Displayed Bodies']
#Axis size
minx = initval['Axes']['Min X']
maxx = initval['Axes']['Max X']
miny = initval['Axes']['Min Y']
maxy = initval['Axes']['Max Y']

for i in initval['Orbiters']:
    orbiters[i] = Orbiter(initval['Orbiters'][i]['Mass'],
                          (initval['Orbiters'][i]['X Position'], initval['Orbiters'][i]['Y Position']),
                          (initval['Orbiters'][i]['X Velocity'], initval['Orbiters'][i]['Y Velocity']),
                          initval['Orbiters'][i]['Name'],
                          initval['Orbiters'][i]['Color'],
                          initval['Orbiters'][i]['Scale'])


#Run the program
data = {}
for obj in Orbiter._orbiters:
    data[obj.__doc__] = ([], [])

for i in range(num):
    for obj in Orbiter._orbiters:
        obj.GetFgXY([(x.px, x.py, x.mass) for x in Orbiter._orbiters if x.__doc__ != obj.__doc__])
        obj.GetExtendedInfo()
        obj.vx = obj.vx + obj.netgx * interval
        obj.vy = obj.vy + obj.netgy * interval
        obj.px = obj.px + obj.vx * interval
        data[obj.__doc__][0].append(obj.px)
        obj.py = obj.py + obj.vy * interval
        data[obj.__doc__][1].append(obj.py)



#Display
if (initval['Matplotlib']):
    
    import matplotlib.pyplot as plt
    
    for obj in Orbiter._orbiters:
        if obj.__doc__ in displayed:
            plt.scatter(data[obj.__doc__][0], data[obj.__doc__][1],s=obj.scale,c=obj.color)

    plt.axis([minx, maxx, miny, maxy])
    plt.show()

