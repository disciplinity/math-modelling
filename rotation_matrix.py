import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button


canvas_rect = plt.axes([0.25, 0.2, 0.65, 0.65])
slider_rect = plt.axes([0.25, 0.05, 0.65, 0.03])
slider = Slider(slider_rect, 'Theta', 1, 360, valinit=1, valfmt="%i")
txt_on_line="eVal="

eigenvector_1 = 1 + 1j
eigenvector_2 = 1 - 1j

def slider_callback(self):
    plt.sca(canvas_rect)
    plt.cla()
    plt.xlim((-2, 2))
    plt.ylim((-2, 2))
    plt.ylabel('Imaginary')
    plt.xlabel('Real')

    theta = slider.val
    eigenvalue_1 = np.cos(theta) + (np.sin(theta) * 1j)
    eigenvalue_2 = np.cos(theta) - (np.sin(theta) * 1j)

    eigenvector1_multiplied_by_eigenvalue1  = eigenvector_1 * eigenvalue_1
    eigenvector1_multiplied_by_eigenvalue2  = eigenvector_1 * eigenvalue_2
    eigenvector2_multiplied_by_eigenvalue1  = eigenvector_2 * eigenvalue_1
    eigenvector2_multiplied_by_eigenvalue2  = eigenvector_2 * eigenvalue_2

    plt_text(eigenvector1_multiplied_by_eigenvalue1, eigenvalue_1)
    plt_text(eigenvector1_multiplied_by_eigenvalue2, eigenvalue_2)
    plt_text(eigenvector2_multiplied_by_eigenvalue1, eigenvalue_1)
    plt_text(eigenvector2_multiplied_by_eigenvalue2, eigenvalue_2)

    plt_plot(eigenvector1_multiplied_by_eigenvalue1, 'ro-')
    plt_plot(eigenvector2_multiplied_by_eigenvalue1, 'ro-')
    plt_plot(eigenvector1_multiplied_by_eigenvalue2, 'bo-')
    plt_plot(eigenvector2_multiplied_by_eigenvalue2, 'bo-')

def plt_text(eigvec, eigval):
    plt.text(eigvec.real, eigvec.imag, txt_on_line + str(round(eigval.real, 2) + round(eigval.imag,2) * 1j))

def plt_plot(eigvec, color):
    plt.plot([0,eigvec.real],[0,eigvec.imag],color,label='python')


slider.on_changed(slider_callback)
plt.show()