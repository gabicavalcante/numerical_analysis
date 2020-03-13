import PyGnuplot as gp
from math import * 
import numpy as np  

# f'(x): (3*(x**2)) - (4*x) - 1
def f(x: int) -> float:
    return (x**3) - (2* (x**2)) - x + 2

derive = lambda f, x, h: (f(x + h) - f(x))/h

def tangent_line_gp(f, a, b):
    x = np.linspace(a, b, 200)

    x0 = 1
    y_0 = f(x0)
    y_tan = derive(f, x0, 0.000000001) * (x - x0) + y_0  
    gp.s([x, y_tan], filename="tangente.dat")

    x1 = (4 + sqrt(28))/6
    x2 = (4 - sqrt(28))/6
 
    gp.c('set grid')
    gp.c('set xrange[-1.5:2.5]')
    gp.c('set xzeroaxis')
    gp.c('set yzeroaxis')

    # Func Cubica
    gp.c('plot (x**3) - (2* (x**2)) - x + 2 title "função cúbica"')

    # Tangente x = 1
    #gp.c('replot "tangente.dat" with lines title "reta tangente em x = 1"')
    gp.c('replot -2*x + 2 with lines title "reta tangente em x = 1"')

    # 1, f(1))
    gp.c(f'replot "<echo 1 {f(1)}" title "(1, f(1))"')

    # PC1
    gp.c(f'replot "<echo {x1} {f(x1)}" title "PC1: {x1:.2f}"')
    # PC1 tangente
    y_0 = f(x1)
    y_tan = derive(f, x1, 0.000000001) * (x - x1) + y_0 
    gp.s([x, y_tan], filename="tangente-pc1.dat")
    gp.c('replot "tangente-pc1.dat" with lines title "reta tangente PC1"')

    # PC2
    gp.c(f'replot "<echo {x2} {f(x2)}" title "PC2: {x2:.2f}"')
    # PC2 tangente
    y_0 = f(x2)
    y_tan = derive(f, x2, 0.000000001) * (x - x2) + y_0 
    gp.s([x, y_tan], filename="tangente-pc2.dat")
    gp.c('replot "tangente-pc2.dat" with lines title "reta tangente PC2"')


if __name__ == '__main__': 
    tangent_line_gp(f, -1.5, 2.5)

    
