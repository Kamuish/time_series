
import matplotlib.pyplot as plt 
plt.style.use("seaborn-dark")
import numpy as np 


def plot_spots(path):
    """
    Plot the number of sun spots, for each year
    """
    data  = []

    with open(path) as file:
        for line in file:
            try:
                data.append(float(line.split(",")[1].split("\n")[0]))
            except:
                pass

    x_axis = np.arange(1749.5,1979, 0.5)
    plt.plot(x_axis, data)
    plt.xlabel("Year")
    plt.ylabel("Number of sun spots")

    plt.savefig("/home/amiguel/phd/classes/time_series/project/report/Figures/ex1_year_sunspot.png")

    plt.show()

plot_spots('/home/amiguel/phd/classes/time_series/project/sunspotz.csv')