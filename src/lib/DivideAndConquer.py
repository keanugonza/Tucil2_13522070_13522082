import matplotlib.pyplot as plt
import time

class DevideAndConquer:
    def __init__(self):
        self.resultPointsX = []
        self.resultPointsY = []

    def titikTengah(self, point1, point2):
        x = (point1[0] + point2[0]) / 2
        y = (point1[1] + point2[1]) / 2
        return (x, y )

    def newCoordinate(self, point1, point2, point3, iterationNow, iterations):
        if iterationNow < iterations:
            iterationNow += 1
            titikTengah1 = self.titikTengah(point1, point2)
            titikTengah2 = self.titikTengah(point2, point3)
            titikTengah3 = self.titikTengah(titikTengah1, titikTengah2)
            self.newCoordinate(point1, titikTengah1, titikTengah3, iterationNow, iterations)  # bagian kiri 
            self.resultPointsX.append(titikTengah3[0]) 
            self.resultPointsY.append(titikTengah3[1])  
            self.newCoordinate(titikTengah3, titikTengah2, point3, iterationNow, iterations)  # bagian kanan

    def create_bezier(self, points, iterations):
        # print('ini dnc biasa')
        self.resultPointsX.append(points[0][0])  
        self.resultPointsY.append(points[0][1])  
        self.newCoordinate(points[0], points[1], points[2], 0, iterations)
        self.resultPointsX.append(points[2][0])  
        self.resultPointsY.append(points[2][1])