import PyGnuplot as gp
from math import * 
import numpy as np  

derive = lambda x: cos(x) - x * sin(x)
# f_xh = lambda f_x, h, x: f_x + h * derive(x)
 
def get_point(x, h, fx): 
    xh = x + h
        
    f_xh = fx + h * derive(x)  
    x = xh

    return (x, f_xh)

    #points_x.append(x)
    #points_y.append(f_xh) 

    fx = f_xh
    
def negative_points():
    x = 0 
    h = -0.5
    fx = 1

    points_x = []
    points_y = []
    
    while x > -6:
        xh = x + h
        
        f_xh = fx + h * derive(x)  
        x = xh

        points_x.append(x)
        points_y.append(f_xh) 

        fx = f_xh

    return [points_x, points_y]




def plot_graph(a, b):
    x = np.linspace(a, b, 200)

    gp.c('set grid')
    gp.c(f'set xrange[{a}:{b}]')
    gp.c('set xzeroaxis')
    gp.c('set yzeroaxis')

    gp.c(f'plot "<echo 0 1" title "(0, 1)"')


negative_points()
