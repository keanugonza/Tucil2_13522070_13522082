def mid_visualize(point1, point2):
    return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2 )

def mid_iterate(points, iterations):
    all_midpoints = [points]
    for _ in range(iterations):
        new_points = [points[0]]
        for i in range(len(points) - 1):
            midpointsleft = mid_visualize(points[i], points[i + 1])
            midpointsright = mid_visualize(points[i + 1], points[-1])
            midpoints = mid_visualize(midpointsleft, midpointsright)
            new_points.append(midpointsleft)
            new_points.append(midpoints)
        new_points.append(points[-1])
        all_midpoints.append(new_points)
    return all_midpoints

def main():
    points = [(0, 0), (50, 100), (100, 0)]
    iterations = 2
    result = mid_iterate(points, iterations)
    for i, midpoints in enumerate(result):
        print(f"Iteration {i+1}: {midpoints}")

if __name__ == "__main__":
    main()