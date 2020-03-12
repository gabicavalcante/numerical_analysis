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
   
    
def points():
    x = 0 
    h = -0.5
    fx = 1

    points_x = []
    points_y = []
    
    while x > -6:
        x, f_xh = get_point(x, h, fx)  
        points_x.append(x)
        points_y.append(f_xh) 

        fx = f_xh

    x = 0 
    h = 0.5
    fx = 1
    
    while x < 6:
        x, f_xh = get_point(x, h, fx)  
        points_x.append(x)
        points_y.append(f_xh) 

        fx = f_xh

    return(points_x, points_y)



def plot_graph(a, b):
    x = np.linspace(a, b, 200)

    gp.c('set grid')
    gp.c(f'set xrange[{a}:{b}]')
    gp.c('set xzeroaxis')
    gp.c('set yzeroaxis')

    gp.c(f'plot "<echo 0 1" title "(0, 1)"')

    gp.s(points(), filename="arquivos.pts")

    gp.c('replot "arquivos.pts" with lines title "f(x) no intervalo [−6:6]"')
    gp.c('replot x*cos(x) + 1 title "f(x) = x*cos(x) + 1"')


if __name__ == '__main__': 
    plot_graph(-6, 6)