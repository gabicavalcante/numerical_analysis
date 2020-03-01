import sys
import PyGnuplot as gp
from math import *
import matplotlib.pyplot as plt
import numpy as np 

def f(x: int) -> float:
    return (x**3) - (2* (x**2)) - x + 2

derive = lambda f, x, h: (f(x + h) - f(x))/h

tang = [derive(f, 1, i) for i in [10**x for x in range(0, -12, -1)]]

def tangent_line_gp(f, x_0, a, b):
    x = np.linspace(a, b, 200)
    y_0 = f(x_0)
    y_tan = derive(f, x_0, 0.000000001) * (x - x_0) + y_0 
    gp.s([x, y_tan], filename="tangente.dat")

    gp.c('set grid')
    gp.c('set xrange[-1.5:2.5]')
    gp.c('set xzeroaxis')
    gp.c('set yzeroaxis')
    gp.c('plot (x**3) - (2* (x**2)) - x + 2 title "função cúbica"')
    gp.c('replot "tangente.dat" with lines title "reta tangente em x = 1"')
    gp.c(f'replot "<echo -1 {f(-1)}"')
    gp.c(f'replot "<echo 1 {f(1)}" title "(1, f(1))"')


def tangent_line_plt(f, x_0, a, b):
    x = np.linspace(a, b, 200)
    y = f(x) 
    y_0 = f(x_0)
    y_tan = derive(f, x_0, 0.000000001) * (x - x_0) + y_0 
   
    #plotting
    plt.plot(x, y, 'r-')
    plt.plot(x, y_tan, 'b-')
    plt.axis([a, b, a, b])
    plt.xlabel('x')     
    plt.ylabel('y')     
    plt.title('Plot of a function with tangent line') 
    plt.show()  


if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 2 else None
    if arg == "matplot":
        tangent_line_plt(f, 1, -1.5, 2.5)
    else:
        tangent_line_gp(f, 1, -1.5, 2.5)
