import matplotlib.pyplot as plt 
plt.style.use("seaborn-dark")
import numpy as np 


def draw_tube(path):
    L = np.pi/2


    xx = np.arange(0, L, 0.01)
    color = [1, 'orange',1 ,'red', 1,'blue']
    for n in [1,3,5]:
        plt.plot(xx, np.cos(xx * n)*0.95, color = color[n], label = f"n = {n}")
        plt.plot(xx, -np.cos(xx * n)*0.95, color = color[n])

    ax = plt.gca()

    xx = np.arange(-0.02, L+0.01, 0.01)

    for k in [1,-1]:
        plt.plot(xx, [k for i in xx], color = 'black', linewidth=2)

    plt.plot([xx[-1], xx[-1]], [1,-1], color = 'black', linewidth=2)
    plt.gca().get_yaxis().set_visible(False)
    plt.gca().get_xaxis().set_ticks([])

    plt.xlabel("R")
    plt.legend(ncol=3, bbox_to_anchor = (0.4, 0.98))
    plt.savefig(path)
    plt.show()

if __name__ == '__main__':
    path = ''
    draw_tube(path)