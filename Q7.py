def sort(coordinates, reference):
    x, y = reference

    coordinates.sort(
        key=lambda point: (point[0] - x) ** 2 + (point[1] - y) ** 2 
    )

    return coordinates


n = int(input("Enter number of coordinates: "))

coordinates = []

for i in range(n):
    x, y = map(int, input(f"Enter x and y of coordinate {i + 1}: ").split())
    #x= input(f"Enter x of coordinate {i + 1}: ")
    #y= input(f"Enter y of coordinate {i + 1}: ")
    coordinates.append((x, y))

ref_point = map(int, input("Enter reference x and y: ").split())

print(sort(coordinates, ref_point))
