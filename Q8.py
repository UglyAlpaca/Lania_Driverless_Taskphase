import csv
import math

cones = []

with open("task1/cones.csv", "r") as file:
   csv_reader = csv.reader(file)
   fields = next(csv_reader)
   for cone in csv_reader:
       cones.append(cone)

def distance_from_origin(cone):
   x = float(cone[1])
   y = float(cone[2])
   return math.sqrt(x**2 + y**2)
    
cones.sort(key=distance_from_origin)

blue = []
yellow = []

for row in cones:
    if row[3] == "blue":
        blue.append(row)
    elif row[3] == "yellow":
        yellow.append(row)


with open ("task1/blue_cones.csv", "w", newline = "") as file:
   writer = csv.writer(file)
   writer.writerow(["id","x","y","colour"])
   writer.writerows(blue)

with open ("task1/yellow_cones.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["id","x","y","colour"])
    writer.writerows(yellow)

centreline = []   

for b in blue:
    bx = float(b[1])
    by = float(b[2])
    nearest_yellow = None
    closest_distance = float("inf")

    for y in yellow:
       yx = float(y[1])
       yy = float(y[2])

       d = math.sqrt((bx -yx)**2 + (by - yy)**2 )
       if closest_distance > d:
          closest_distance = d
          nearest_yellow = y
    yx = float(nearest_yellow[1])
    yy = float(nearest_yellow[2])
    
    mx = (bx + yx) / 2
    my = (by + yy) / 2

    centreline.append([mx,my])

with open ("task1/centreline.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    writer.writerow(["x","y"])
    writer.writerows(centreline)

print("Done!")
