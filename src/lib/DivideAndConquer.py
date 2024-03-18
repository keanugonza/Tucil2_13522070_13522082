import numpy as np

class DivideAndConquer:
    def __init__(self):
        self.resultPointsX = []
        self.resultPointsY = []

    #untuk mencari titik tengah antara 2 titik
    def titikTengah(self, point1, point2):
        return ((point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2 )

    #membentuk array kumpulan titik tengah sesuai iterasi
    def newCoordinate(self, point1, point2, point3, iterationNow, iterations):
        if iterationNow < iterations:
            iterationNow += 1
            titikTengah1 = self.titikTengah(point1, point2)
            titikTengah2 = self.titikTengah(point2, point3)
            titikTengah3 = self.titikTengah(titikTengah1, titikTengah2)
            # mencari titik tengah dari 3 titik di kiri
            self.newCoordinate(point1, titikTengah1, titikTengah3, iterationNow, iterations)  
            self.resultPointsX.append(titikTengah3[0])      #append titik tengah ke array
            self.resultPointsY.append(titikTengah3[1])      #append titik tengah ke array
            # mencari titik tengah dari 3 titik di kanan
            self.newCoordinate(titikTengah3, titikTengah2, point3, iterationNow, iterations) 

    #membuat kurva bezier
    def create_bezier(self, points, iterations):
        self.resultPointsX.append(points[0][0])  #append titik awal
        self.resultPointsY.append(points[0][1])  
        self.newCoordinate(points[0], points[1], points[2], 0, iterations) #cari titik titik tengahnya
        self.resultPointsX.append(points[2][0])  
        self.resultPointsY.append(points[2][1])  #append titik akhir