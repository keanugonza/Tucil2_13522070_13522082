import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import time, os
import numpy as np
import sys
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 

# Algortima Divide and Conquer 
class Solver:
    def __init__(self):
        self.resultPoints = []
        self.new_points = []

    def titikTengah(self, point1, point2):
        x = (point1[0] + point2[0]) / 2
        y = (point1[1] + point2[1]) / 2
        return (x, y)

    def titikTengah_N(self, points):
        if len(points) == 2:
            return self.titikTengah(points[0], points[1])
        else:
            newPoints = []
            add_new_points = []
            for i in range(len(points) - 1):
                temp = (self.titikTengah(points[i], points[i + 1]))
                newPoints.append(temp)
                if i == 0 or i == (len(points) - 2):
                    add_new_points.append(temp)
            panjang = len(self.new_points) // 2
            self.new_points.insert(panjang, add_new_points[1])
            self.new_points.insert(panjang, add_new_points[0])
            return self.titikTengah_N(newPoints)

    def newCoordinate_N(self, points, iterationNow, iterations):
        if iterationNow < iterations:
            iterationNow += 1
            self.new_points.clear()

            titikTengah = self.titikTengah_N(points)
            split = np.array_split(self.new_points, 2)

            left_points = split[0].tolist()
            right_points = split[1].tolist()
            left_points.insert(0, points[0])
            left_points.append(titikTengah)
            right_points.insert(0, titikTengah)
            right_points.append(points[-1])

            self.newCoordinate_N(left_points, iterationNow, iterations)
            self.resultPoints.append(titikTengah)
            self.newCoordinate_N(right_points, iterationNow, iterations)

    def create_bezier(self, points, iterations):
        self.resultPoints.append(points[0])
        self.newCoordinate_N(points, 0, iterations)
        self.resultPoints.append(points[-1])

    def solve(self, iterations, points):
        # Timer proses
        start_time = time.time()
        self.create_bezier(points, iterations)
        end_time = time.time()
        points_fix = self.resultPoints

        # Menghitung waktu proses
        global timer
        timer = round((end_time - start_time) * 1000, 5)

        # Output hasil
        print("Divide and Conquer Approach Time:", timer, "ms")

        # Menampilkan waktu proses pada GUI
        time_result.config(text=f'{timer} ms')

        # Menampilkan kurva


class Solver2:
    def pascal_triangle(n):
        triangle = [[0] * (n + 1) for _ in range(n + 1)]
        for line in range(n + 1):
            for i in range(line + 1):
                if i == 0 or i == line:
                    triangle[line][i] = 1
                else:
                    triangle[line][i] = triangle[line - 1][i - 1] + triangle[line - 1][i]
        return triangle

    def pascal_function(n, t):
        triangle = Solver2.pascal_triangle(n)
        result = []
        for i in range(n + 1):
            coeff = triangle[n][i] * ((1 - t) ** (n - i)) * (t ** i)
            result.append(coeff)
        return result

    def bezier_pascal(points, iteration):
        precision = 1.0/2**iteration
        points_fix = []  
        t = 0
        n = len(points) - 1
        while t <= 1:
            pascal_coefficients = Solver2.pascal_function(n, t)
            x = np.sum([coeff * point[0] for coeff, point in zip(pascal_coefficients, points)])
            y = np.sum([coeff * point[1] for coeff, point in zip(pascal_coefficients, points)])
            points_fix.append((x, y))  
            t += precision
        return points_fix

    def solve2(self, points, iterations):
        # Timer proses
        start_time2 = time.time()
        Solver2.bezier_pascal(points, iterations)
        end_time2 = time.time()
        
        # Menghitung waktu proses
        global timer
        timer2 = round((end_time2 - start_time2) * 1000, 5)

        # Output hasil
        print("Brute Force Approach Time:", timer2, "ms")

        # Menampilkan waktu proses pada GUI
        time2_result.config(text=f'{timer2} ms')

def point_split(input):
    lines = input.split("\n")
    result = []
    for line in lines:
        points = line.split(",")
        result.append((int(points[0]), int(points[1])))
    return result
    
# GUI Bezier Curve Dimulai
def starting():
    global iterations
    global n
    global points
    global t
    points_fix = []

# ASSETS PATH
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

# INPUT KEYBOARD 
def open_keyboard_input():
    global iterations
    global n
    global points
    global point_string
    points_fix = []
    
    n = (n_input.get())
    iterations = (iterasi_input.get())
    point_string = (control_input.get("1.0", "end-1c"))

    if n == '' or iterations == '' or point_string == '':
        return None

    n = int(n_input.get())
    iterations = int(iterasi_input.get())
    point_string = str(control_input.get("1.0", "end-1c"))

    points = point_split(point_string)

    return n, iterations, points

def solve_keyboard():
    if open_keyboard_input() == None:
        messagebox.showerror("Error", "Please complete the input")
        return
    solver_obj = Solver()
    solver_obj2 = Solver2()
    solver_obj.solve(iterations, points)
    solver_obj2.solve2(points, iterations)

################### TKINTER GUI ###################
window = Tk()
widht = 990
height = 704
x = (window.winfo_screenwidth()//2) - (widht//2) 
y = (window.winfo_screenheight()//2) - (height//2)
window.geometry(f'{widht}x{height}+{x}+{y}')
window.resizable(False, False)
window.title('Bezier Curve Maker')
window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

page1 = Frame(window)
page1.grid(row=0, column=0, sticky='nsew')

starting()

# Background
page1.configure(bg='#FFFFFF')

# Jumlah Point
n_path = resource_path("assets/jumlah.png")
n_img = PhotoImage(file=n_path)
Label(page1, image=n_img, bg='#FFFFFF').place(x=30, y=30)
n_input = Entry(page1, width=2, border=0, font=('Microsoft YaHei UI',16), bg='#C5A2C6', fg='#5D5EAA', highlightthickness=0)
n_input.place(x=90, y=90)

# Iterasi
iterasi_path = resource_path("assets/Iterasi.png")
iterasi_img = PhotoImage(file=iterasi_path)
Label(page1, image=iterasi_img, bg='#FFFFFF').place(x=30, y=160)
iterasi_input = Entry(page1, width=2, border=0, font=('Microsoft YaHei UI',16), bg='#C5A2C6', fg='#5D5EAA', highlightthickness=0)
iterasi_input.place(x=90, y=220)

# Control Point
control_path = resource_path("assets/control.png")
control_img = PhotoImage(file=control_path)
Label(page1, image=control_img, bg='#FFFFFF').place(x=30, y=290)
control_input = Text(page1, width=12, height=10, border=0, font=('Microsoft YaHei UI', 16), bg='#F1E3F0', fg='#5D5EAA', highlightthickness=0)
control_input.place(x=50, y=330)

# Background Kurva
bgc_path = resource_path("assets/bgcurva.png")
bgc_img = PhotoImage(file=bgc_path)
Label(page1, image=bgc_img, bg='#FFFFFF').place(x=220, y=10)

# Time Brute Force
time2_path = resource_path("assets/time.png")
time2_img = PhotoImage(file=time2_path)
Label(page1, image=time2_img, bg='#FFFFFF').place(x=395, y=590)
time2_result = Label(page1, text="", font=('Microsoft YaHei UI',16), bg='#F1E3F0', fg='#5D5EAA')
time2_result.place(x=420, y=620)

# Time Divide and Conquere
time_path = resource_path("assets/time.png")
time_img = PhotoImage(file=time_path)
Label(page1, image=time_img, bg='#FFFFFF').place(x=790, y=590)
time_result = Label(page1, text="", font=('Microsoft YaHei UI',16), bg='#F1E3F0', fg='#5D5EAA')
time_result.place(x=815, y=620)

# Brute Force
dnc_path = resource_path("assets/bf.png")
dnc_img = PhotoImage(file=dnc_path)
Label(page1, image=dnc_img, bg='#FFFFFF').place(x=210, y=610)
dnc_result = Label(page1, text="", font=('Microsoft YaHei UI',16), bg='#F1E3F0', fg='#5D5EAA')

# Divide n Conquer
bf_path = resource_path("assets/dnc.png")
bf_img = PhotoImage(file=bf_path)
Label(page1, image=bf_img, bg='#FFFFFF').place(x=600, y=610)
bf_result = Label(page1, text="", font=('Microsoft YaHei UI',16), bg='#F1E3F0', fg='#5D5EAA')

# Start
start_path = resource_path("assets/start.png")
start_img = PhotoImage(file=start_path)
start_label = Label(page1, image=start_img, bg='#FFFFFF')
start_label.place(x=30, y=590)
start_btn = Button(page1, text='S T A R T', height = 1, width = 7, relief=FLAT, command=solve_keyboard)
start_btn.place(x=55, y=605)

# END
window.mainloop()