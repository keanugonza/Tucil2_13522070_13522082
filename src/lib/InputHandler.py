import numpy
from numpy.random import Generator, PCG64

def get_points():
    while True:
        try:
            n = int(input("Masukkan banyaknya titik: "))
            if n < 2:
                print("Kurva Bezier Tidak Dapat Dibuat. Coba Input Ulang!")
                continue
            points = [tuple(map(float, input(f"Masukkan koordinat titik P{i} (pisahkan dengan spasi): ").split())) for i in range(n)]
            iterations = int(input("Masukkan jumlah iterasi: "))
            if iterations < 0:
                print("Jumlah iterasi tidak boleh negatif. Coba Input Ulang!")
                continue
            return n, points, iterations
        except ValueError:
            print("Masukkan harus berupa bilangan bulat. Coba Input Ulang!")
