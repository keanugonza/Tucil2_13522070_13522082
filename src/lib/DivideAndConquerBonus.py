import numpy as np

class DivideAndConquerBonus:
    def __init__(self):
        self.resultPoints = []
        self.new_points = []

    #mencari titik tengah antar 2 titik
    def titikTengah(self, point1, point2):
        x = (point1[0] + point2[0]) / 2
        y = (point1[1] + point2[1]) / 2
        return (x, y )
    
    #mencari titik tengah dari N titik
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

    #membuat array berisi titik-titik tengah sesuai iterasi
    def newCoordinate_N(self, points, iterationNow, iterations):
        if iterationNow < iterations:
            iterationNow += 1

            #mencari titiik tengah
            self.new_points.clear()
            titikTengah = self.titikTengah_N(points)
            split = np.array_split(self.new_points,2)

            #menambahkan titik di kiri dan di kanan titik tengah untuk diiterasi lagi
            left_points = split[0].tolist()
            right_points = split[1].tolist()
            left_points.insert(0, points[0])
            left_points.append(titikTengah)
            right_points.insert(0, titikTengah)
            right_points.append(points[-1])

            # mencari titik tengah dari N titik di kiri
            self.newCoordinate_N(left_points, iterationNow, iterations)
            self.resultPoints.append(titikTengah)   #append titik tengah ke array result
            # mencari titik tengah dari N titik di kanan
            self.newCoordinate_N(right_points, iterationNow, iterations)

    #membentuk kurva bezier
    def create_bezier(self, points, iterations):
        self.resultPoints.append(points[0])    #append titik awal
        self.newCoordinate_N(points, 0, iterations)     #cari titik titik tengah sesuai iterasi
        self.resultPoints.append(points[-1])  #append titik akhir