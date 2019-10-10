import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button
from scipy.optimize import fsolve

def f1(x):
    return x**3

x = np.linspace(-10, 10, 30)
y = f1(x)

fig = plt.figure()
ax = fig.add_subplot(111)

last_point = None
last_clicked = None
def onclick_graph(event):
    global last_point
    global last_clicked

    if event.inaxes == ax:
        if last_point is not None:
            last_point.remove()

        last_point = ax.scatter(event.xdata, 0)
        last_clicked = event.xdata
        fig.canvas.draw()

h = 0.1
#f'(x) = lim(h->0)  (f(x+h) - f(x)) / h
def derrivative(f, c):
    return (f(c + 0.1) - f(c)) / 0.1


def tan_func(f, fp, c, a):
    return f(c) + fp*(a-c)



def button_on_click(event):
    global last_clicked
    fprime = derrivative(f1, last_clicked)
    tangent = [tan_func(f1, fprime, last_clicked, a) for a in x]

    ax.plot(last_clicked, f1(last_clicked), 'om', x, tangent, '--r')

    t = lambda x : f1(last_clicked) + fprime*(x-last_clicked)
    last_clicked = fsolve(t, 0)
    plt.show()



fig.canvas.mpl_connect('button_press_event', onclick_graph)
plt.plot(x, y)

button_ax = plt.axes([0.9, 0.0, 0.1, 0.05])
btn = Button(button_ax, "Newton")
btn.on_clicked(button_on_click)
plt.show()