import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use("seaborn-darkgrid")


path_1 = '/home/amiguel/phd/classes/time_series/project/Keplerlightcurves/KIC3656476lightcurve.txt'

path_2 = '/home/amiguel/phd/classes/time_series/project/Keplerlightcurves/KIC6603624lightcurve.txt'

names = ['KIC 3656476', 'KIC 6603624' ]

fig, axes = plt.subplots(2,1)

for index, name in enumerate([path_1, path_2]):
    with open(name) as file:
        x = []
        y = []
        for line in file:
            nn = line.split()
            x.append(float(nn[0].replace(',','.')))
            y.append(float(nn[1].replace(',','.')))

        axes[index].plot(x,y)
    axes[index].set_ylabel("Light curve [ppm]")
    axes[index].set_xlabel("Time [s]")
    axes[index].set_title(names[index])

plt.tight_layout()
fig.savefig("/home/amiguel/phd/classes/time_series/project/report/Figures/ex2_LC.png")


plt.show()