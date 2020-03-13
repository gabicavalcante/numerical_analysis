import PyGnuplot as gp
from math import * 
import numpy as np  

derive = lambda x: cos(x) - x * sin(x)

f = lambda x: (x * cos(x)) + 1

# impar
f_odd = lambda x, k: ((-1)**((k-1)/2)) * k * cos(x) + ((-1)**((k-1)/2)) * x * sin(x)
# par
f_even = lambda x, k: ((-1)**(k/2)) * k * sin(x) + ((-1)**(k/2)) * x * cos(x)


def taylor(x):
    sum_ = 0
    a = 0
    for n in range(0, 25):
        if n % 2 == 0:
            #print('{const}*x**{index}/{index}!'.format(const=f_even(0, n), index=n))
            sum_ += (f_even(a, n)/factorial(n)) * ((x - a)**n)
        else:
            #print('{const}*x**{index}/{index}!'.format(const=f_odd(0, n), index=n))
            sum_ += (f_odd(a, n)/factorial(n)) * ((x - a)**n)

    return sum_

 
def get_point(x, h, fx): 
    xh = x + h        
    f_xh = fx + h * derive(x)  
    x = xh

    return (x, f_xh) 
   
    
def points():
    x = 0 
    H = 0.5
    fx = 1

    points_x = []
    points_y = []
    
    while x > -6:
        x, f_xh = get_point(x, -H, fx)  
        points_x.append(x)
        points_y.append(f_xh) 

        fx = f_xh

    points_x.reverse()
    points_y.reverse()

    x = 0  
    fx = 1
    
    while x < 6:
        x, f_xh = get_point(x, H, fx)  
        points_x.append(x)
        points_y.append(f_xh) 

        fx = f_xh

    return(points_x, points_y)



def plot_graph(a, b):
    gp.c('set grid')
    gp.c(f'set xrange[{a}:{b}]')
    gp.c('set xzeroaxis')
    gp.c('set yzeroaxis')

    gp.c(f'plot "<echo 0 1" title "(0, 1)"')

    gp.s(points(), filename="arquivos.pts")

    gp.c('replot "arquivos.pts" with lp title "f(x) no intervalo [−6:6]"')
    gp.c('replot x*cos(x) + 1 title "f(x) = x*cos(x) + 1"')


def plot_graph_taylo(a, b):
    gp.c('set grid')
    gp.c(f'set xrange[{a}:{b}]')
    gp.c(f'set yrange[-10:10]')
    gp.c('set xzeroaxis')
    gp.c('set yzeroaxis')

    points_x = np.linspace(a, b, 100)
    points_y = [taylor(x) for x in points_x]
    gp.s([points_x, points_y], filename='taylor.pts')
    gp.c('plot "taylor.pts"')
    #gp.c(f'plot 1+(x**1)/{factorial(1)} + -3*x**3/{factorial(3)} + 5*x**5/{factorial(5)} + -7*x**7/{factorial(7)} title "taylor"')
    gp.c('replot x*cos(x) + 1 title "f(x) = x*cos(x) + 1"')

if __name__ == '__main__': 
    a = -6
    b = 6
    plot_graph(a, b)
    #plot_graph_taylo(a, b)
    