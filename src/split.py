def point_split(input):
    lines = input.split("\n")
    result = []
    for line in lines:
        points = line.split(",")
        result.append((int(points[0]), int(points[1])))

    return result

input_string = """7,8
9,2
8,7"""
result = point_split(input_string)
print(result)  # Output: [(7, 8), (9, 2), (8, 7)]