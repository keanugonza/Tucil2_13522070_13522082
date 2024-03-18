from lib.Visualizer import plot_curve
import lib.DivideAndConquer as dnc
import lib.DivideAndConquerBonus as dnc_bonus
import lib.BruteForce as bf
import lib.BruteForceBonus as bf_bonus
import lib.InputHandler as ih
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class textcolors:
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    LIGHTBLUE = '\033[94m'
    LIGHTGREEN = '\033[92m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'
    CYAN = '\033[36m'

print(textcolors.LIGHTBLUE + """
 ____  ____  ____  ____  ____  ____     ___  __  __  ____  _  _  ____ 
(  _\\ ( ___)(_   )(_  _)( ___)(  _ \\   / __)(  )(  )(  _ \\( \\/ )( ___)
 ) _ < )__)  / /_  _)(_  )__)  )   /  ( (__  )(__)(  )   / \\  /  )__) 
(____/(____)(____)(____)(____)(_)\\_)   \\___)(______)(_)\\_)  \\/  (____)
""" + textcolors.ENDC, end="")

print(textcolors.WARNING + """
   __                ___              __       ____          _____                     
  / /   __ __       / _ | ___ __ __  / /      / __/___      / ___/ ___   ___  ___ ___ _
 / _ \\ / // /      / __ |/_ // // / / /       > _/_ _/     / (_ / / _ \\ / _ \\/_ // _ `/
/_.__/ \\_, /      /_/ |_|/__/\\_,_/ /_/       |_____/       \\___/  \\___//_//_//__/\\_,_/ 
      /___/                                                                                                                         
""" + textcolors.ENDC)

# Mendapatkan input banyaknya titik dan masing-masing titiknya 
# serta besaran iterasi yang diinginkan
n, points, iterations = ih.get_points()

# Algoritma untuk spek wajib
if (n == 3):
    # Waktu eksekusi menggunakan algoritma Divide and Conquer
    bezier_dnc = dnc.DivideAndConquer()
    start_time = time.time()
    bezier_dnc.create_bezier(points, iterations)
    end_time = time.time()
    print(textcolors.BOLD + textcolors.LIGHTGREEN + "Divide and Conquer Approach Time:" + textcolors.ENDC, (end_time - start_time)*1000 , "ms")

    # Waktu eksekusi menggunakan algoritma Brute Force
    start_time = time.time()
    curve_points_bf = bf.bezier_bf(points, iterations)
    end_time = time.time()
    print(textcolors.BOLD + textcolors.LIGHTGREEN + "Brute Force Approach Time:" + textcolors.ENDC, (end_time - start_time)*1000, "ms")

    curve_points_dnc = []
    for i in range(len(bezier_dnc.resultPointsX)):
        temp = (bezier_dnc.resultPointsX[i], bezier_dnc.resultPointsY[i])
        curve_points_dnc.append(temp)

    # Mengecek bahwa kurva yang terbentuk akan sama antara kedua algoritma
    if len(curve_points_dnc) == len(curve_points_bf):
        print(textcolors.BOLD + textcolors.LIGHTGREEN + "Both DnC and Brute Force algorithms yield the same Bezier point:" + textcolors.ENDC, len(curve_points_dnc), "points")
    else:
        print(textcolors.FAIL + "Oops, there is a difference between the two algorithms." + textcolors.ENDC)

    # Visualisasi menggunakan matplotlib
    plot_curve(curve_points_dnc, points, "Divide and Conquer")
    plot_curve(curve_points_bf, points, "Brute Force")

# Algoritma untuk spek bonus
else:
    # Waktu eksekusi menggunakan algoritma Divide and Conquer
    bezier_dnc = dnc_bonus.DivideAndConquerBonus()
    start_time = time.time()
    bezier_dnc.create_bezier(points, iterations)
    end_time = time.time()
    print(textcolors.BOLD + textcolors.LIGHTGREEN + "Divide and Conquer Approach Time:" + textcolors.ENDC, (end_time - start_time)*1000 , "ms")

    # Waktu eksekusi menggunakan algoritma Brute Force
    start_time = time.time()
    curve_points_bf = bf_bonus.bezier_pascal(points, iterations)
    end_time = time.time()
    print(textcolors.BOLD + textcolors.LIGHTGREEN + "Brute Force Approach Time:" + textcolors.ENDC, (end_time - start_time)*1000 , "ms")

    # Mengecek bahwa kurva yang terbentuk akan sama antara kedua algoritma
    if len(bezier_dnc.resultPoints) == len(curve_points_bf):
        print(textcolors.BOLD + textcolors.LIGHTGREEN + "Both DnC and Brute Force algorithms yield the same Bezier point:" + textcolors.ENDC, len(bezier_dnc.resultPoints), "points")
    else:
        print(textcolors.FAIL + "Oops, there is a difference between the two algorithms." + textcolors.ENDC)

    # Visualisasi menggunakan matplotlib
    plot_curve(bezier_dnc.resultPoints, points, "Divide and Conquer")
    plot_curve(curve_points_bf, points, "Brute Force")