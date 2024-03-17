import numpy as np

class DevideAndConquerBonus:
    def __init__(self):
        self.resultPoints = []
        self.new_points = []

    def titikTengah(self, point1, point2):
        x = (point1[0] + point2[0]) / 2
        y = (point1[1] + point2[1]) / 2
        return (x, y )
    
    def titikTengah_N(self, points):
        if len(points) == 2:
            return self.titikTengah(points[0], points[1])
        else:
            newPoints = []
            add_new_points = []
            for i in range (len(points) -1):
                temp = (self.titikTengah(points[i], points[i+1]))
                newPoints.append(temp)
                if i == 0 or i == (len(points) - 2):
                    add_new_points.append(temp)
            panjang = len(self.new_points)//2
            self.new_points.insert(panjang, add_new_points[1])
            self.new_points.insert(panjang, add_new_points[0])
            return self.titikTengah_N(newPoints)

    def newCoordinate_N(self, points, iterationNow, iterations):
        if iterationNow < iterations:
            iterationNow += 1
            self.new_points.clear()

            titikTengah = self.titikTengah_N(points)
            split = np.array_split(self.new_points,2)

            left_points = split[0].tolist()
            right_points = split[1].tolist()
            left_points.insert(0, points[0])
            left_points.append(titikTengah)
            right_points.insert(0, titikTengah)
            right_points.append(points[-1])

            self.newCoordinate_N(left_points, iterationNow, iterations)  # bagian kiri 
            self.resultPoints.append(titikTengah)  
            self.newCoordinate_N(right_points, iterationNow, iterations)  # bagian kanan

    def create_bezier(self, points, iterations):
        self.resultPoints.append(points[0])   
        self.newCoordinate_N(points, 0, iterations)
        self.resultPoints.append(points[-1]) 
        # print("ini dnc bonus")