import sys
import PyGnuplot as gp
from math import *
import matplotlib.pyplot as plt
import numpy as np 
from scipy.optimize import fmin

def f(x: int) -> float:
    return (x**3) - (2* (x**2)) - x + 2

def f_(x: int) -> float:
    return (3*(x**2)) - (4*x) - 1

derive = lambda f, x, h: (f(x + h) - f(x))/h

def tangent_line_gp(f, x_0, a, b):
    x = np.linspace(a, b, 200)
    y_0 = f(x_0)
    y_tan = derive(f, x_0, 0.000000001) * (x - x_0) + y_0 
    gp.s([x, y_tan], filename="tangente.dat")

    x1 = (4 + sqrt(28))/6
    x2 = (4 - sqrt(28))/6
 
    gp.c('set grid')
    gp.c('set xrange[-1.5:2.5]')
    gp.c('set xzeroaxis')
    gp.c('set yzeroaxis')
    gp.c('plot (x**3) - (2* (x**2)) - x + 2 title "função cúbica"')
    gp.c('replot "tangente.dat" with lines title "reta tangente em x = 1"')

    gp.c(f'replot "<echo {x1} {f(x1)}" title "PC1: {x1:.2f}"')
    y_0 = f(x1)
    y_tan = derive(f, x1, 0.000000001) * (x - x1) + y_0 
    gp.s([x, y_tan], filename="tangente-pc1.dat")
    gp.c('replot "tangente-pc1.dat" with lines title "reta tangente PC1"')

    gp.c(f'replot "<echo {x2} {f(x2)}" title "PC2: {x2:.2f}"')
    y_0 = f(x2)
    y_tan = derive(f, x2, 0.000000001) * (x - x2) + y_0 
    gp.s([x, y_tan], filename="tangente-pc2.dat")
    gp.c('replot "tangente-pc2.dat" with lines title "reta tangente PC2"')

    gp.c(f'replot "<echo 1 {f(1)}" title "(1, f(1))"')



if __name__ == '__main__':
    arg = sys.argv[1] if len(sys.argv) > 2 else None
    tangent_line_gp(f, 1, -1.5, 2.5)

    
