<div align="center">

# Tugas Kecil 2 IF2211 Strategi Algoritma <br/> Semester II tahun 2023/2024 <br/> 
## Membangun Kurva Bézier dengan Algoritma Titik Tengah berbasis Divide and Conquer

> This program is created to fulfill the second small assignment of the IF2211 Algorithmic Strategy course with the aim of understanding the implementation of the Divide and Conquer Algorithm in forming Bezier Curves.

## Authors 

<table style="width:100%; background-color:#87CEFA; color:#F0F8FF;">
  <tr>
    <th>Nama</th>
    <th>NIM</th>
  </tr>
  <tr>
    <td>Marzuli Suhada M</td>
    <td>13522070</td>
  </tr>
  <tr>
    <td>Keanu Amadius Gonza Wrahatno</td>
    <td>13522082</td>
  </tr>
</table>

</div>

## Table of Contents
* [General Info](#general-information)
* [Features](#features)
* [Screenshots](#screenshots)
* [Usage](#usage)
* [Project Status](#project-status)
* [Contact](#contact)


## General Information
In this assignment, the main issue to be addressed is the formation of Quadratic Bézier Curve. The objective of this task is to visualize the curve resulting from points determined using the Divide and Conquer Algorithm approach. Additionally, this task will also involve the generalization of the algorithm so that it can solve the problem of forming Bézier Curves from n points. In this small assignment, a brute force algorithm is utilized as a benchmark to be compared in terms of complexity and validity of the solution.



## Features
- Ability to form Bézier Curve with N points > 2
- Ability to visualize the curve using matplotlib and GUI format


## Screenshots
![Example screenshot](./test/test_2.png)
![Example screenshot](./test/test_4.png)
![Example screenshot](./test/bonus_test3.png)
![Example screenshot](./test/bonus_test2.png)

## Setup
- Make sure you have the following python library installed <br>
```bash
pip install numpy
```
```bash
pip install matplotlib
```

- To run our project, simply navigate to src directory and run <br>
If you want to use the CLI <br>
```bash
cd src 
```
```bash
python main.py 
```

If you want to use the GUI <br>
```bash
cd src 
```
```bash
python gui.py 
```

## How to Use
Make sure your input format is as below:

- Enter control points in the format 
x1,y1
x2,y2
x3,y3
...
xn,yn

- The input for the number of points must be at least 3.
- The input for the number of iterations must be an integer greater than 0


## Project Status
Project is:  _complete_ 

## Contact
13522070@mahasiswa.itb.ac.id (Marzuli Suhada M) <br>
13522082@mahasiswa.itb.ac.id (Keanu Amadius Gonza W.)
