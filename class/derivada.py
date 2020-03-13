from math import cos

def f(x):
    return x * cos(x)

lim = lambda x, h: (f(x + h) - f(x))/h

derive = lambda f, x, h: (f(x + h) - f(x))/h
tang = [derive(f, 1, i) for i in [10**x for x in range(0, -12, -1)]]

for h in [0.1, 0.05, 0.01, 0.005, 0.0001, 0.00005]:
    print(f"h: {h} -> {lim(1, h)}")

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