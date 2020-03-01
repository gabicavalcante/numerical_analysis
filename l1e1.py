import PyGnuplot as gp
import numpy as np

def f(x):
    return (x**3) - (2* (x**2)) - x + 2

f_ = lambda x, h: (f(x + h) - f(x))/h

tang = [f_(1, i) for i in [0.1, 0.05, 0.01, 0.005, 0.001, 0.0005, 0.0001]]

gp.s([tang], filename="tangente.dat")

gp.c('set grid')
gp.c('set xrange[-1.5:2.5]')
gp.c('set xzeroaxis')
gp.c('set yzeroaxis')
gp.c('plot (x**3) - (2* (x**2)) - x + 2 title "função cúbica"')

c_plot = 'replot "tangente.dat" with lines '
gp.c(c_plot)

