import PyGnuplot as gp
import numpy as np
from math import *

def f(x):
    return (x**3) - (2* (x**2)) - x + 2

def g(x):
    return sin(x) * cos(x) + exp(2*x) + 2*x**4 - 10

derive = lambda function, x, h: (function(x + h) - function(x))/h

tang = [derive(f, 1, i) for i in [10**x for x in range(0, -12, -1)]]

gp.s([tang], filename="tangente.dat")

gp.c('set grid')
gp.c('set xrange[-1.5:2.5]')
gp.c('set xzeroaxis')
gp.c('set yzeroaxis')
gp.c('plot (x**3) - (2* (x**2)) - x + 2 title "função cúbica"')
gp.c('replot "tangente.dat" with lines ')

