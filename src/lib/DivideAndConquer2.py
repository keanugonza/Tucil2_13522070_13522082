import matplotlib.pyplot as plt
import time

class DevideAndConquer:
    def __init__(self):
        self.bezierPointsX = []
        self.bezierPointsY = []

    def titikTengah(self, control_point1, control_point2):
        x = (control_point1[0] + control_point2[0]) / 2
        y = (control_point1[1] + control_point2[1]) / 2
        return (x, y )

    def newCoordinate(self, ctrl1, ctrl2, ctrl3, current_iteration):
        # print("call")
        iterations = 20  # Assuming 'iterations' is defined elsewhere
        if current_iteration < iterations:
            # the next control point
            current_iteration += 1
            # calculate next mid points
            titikTengah1 = self.titikTengah(ctrl1, ctrl2)
            titikTengah2 = self.titikTengah(ctrl2, ctrl3)
            titikTengah3 = self.titikTengah(titikTengah1, titikTengah2)
            self.newCoordinate(ctrl1, titikTengah1, titikTengah3, current_iteration)  # bagian kiri 
            self.bezierPointsX.append(titikTengah3[0]) 
            self.bezierPointsY.append(titikTengah3[1])  
            self.newCoordinate(titikTengah3, titikTengah2, ctrl3, current_iteration)  # bagian kanan

    def create_bezier(self, ctrl1, ctrl2, ctrl3):
        self.bezierPointsX.clear()
        self.bezierPointsY.clear()
        self.bezierPointsX.append(ctrl1[0])  
        self.bezierPointsY.append(ctrl1[1])  
        self.newCoordinate(ctrl1, ctrl2, ctrl3, 0)
        self.bezierPointsX.append(ctrl3[0])  
        self.bezierPointsY.append(ctrl3[1])  
