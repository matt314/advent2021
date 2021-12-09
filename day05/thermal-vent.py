# Advent of Code 2021 Day05

class SeaMap:
    def __init__(self):
        self.map = dict()
        self.danger = ("none", 0)

    def __str__(self):
        cross_points = [point for point, dangerval in self.map.items() if dangerval > 1]
        return f"The most dangerous spot is {self.danger[0]}, danger level {self.danger[1]}; total dangerpoints: {len(cross_points)}"

    def printMap(self):
        return self.map

    # Increase the Danger Count of a point
    # Point is string "x,y"
    def addDanger(self, point):
        if point in self.map:
            self.map[point] += 1
        else:
            self.map[point] = 1

        if self.map[point] > self.danger[1]:
            self.danger = (point, self.map[point])
            # print(f"New Biggest Danger! {self}")

        return self.map[point]

    
    def dangerLine(self, line):
        # print(line)
        end1coord = line[0].split(",")
        end2coord = line[1].split(",")
        xends = [ int(end1coord[0]), int(end2coord[0]) ]
        yends = [ int(end1coord[1]), int(end2coord[1]) ]

        # print(xends)
        # print(yends)
        dangerpoints = list()
        if min(xends) == max(xends):
            # x is the same
            xrange = [ min(xends) ]
            yrange = list(range(min(yends), max(yends) + 1))
            for x in xrange:
                for y in yrange:
                    dangerpoints.append(f"{x},{y}")
        elif min(yends) == max(yends):
            # y is the same
            xrange = list(range(min(xends), max(xends) + 1))
            yrange = [ min(yends) ]
            for x in xrange:
                for y in yrange:
                    dangerpoints.append(f"{x},{y}")
        elif max(xends) - min(xends) == max(yends) - min(yends):
            # diagonal
            return -2
        else:
            # not a perpendicular line
            return -1

        # print(f"x: {xrange}, y: {yrange}")
        for point in dangerpoints:
            self.addDanger(f"point")

 
        return self.danger

# Read in input file
with open('input.txt', 'r') as inputfile:
    ventlines_in = inputfile.readlines()

    ventlines = list()
    for line in ventlines_in:
        ventlines.append(line.strip().split(" -> "))

map1 = SeaMap()

for line in ventlines:
    map1.dangerLine(line)

print(map1)
print(len(map1.printMap()))
