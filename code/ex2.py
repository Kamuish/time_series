import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use("seaborn-darkgrid")
from matplotlib.lines import Line2D
from find_peaks import peak_finder 

def calculate_speed_sound(R, R_err, spacing, spacing_err):
    R *= 696340  # pass from Sun radius to to km
    R_err *= 696340 
    spacing /= 1000000 # pass from uHz to Hz
    spacing_err /= 1000000 

    speed = 2*R*spacing
    err_speed = speed * np.sqrt((R_err/(2*R))**2 + (spacing_err/spacing)**2)

    return speed, err_speed

def overtone_numb_calc(radius_star, speed_sound, peaks):
    radius_star *= 696340 # pass to km
    return [int(round(0.5*((peak/1000000)*4*radius_star/speed_sound - 1))) for peak in peaks]


path_1 = '/home/amiguel/phd/classes/time_series/project/Keplerlightcurves/KIC3656476lightcurve.fou'
data_1 = np.loadtxt(path_1)

path_2 = '/home/amiguel/phd/classes/time_series/project/Keplerlightcurves/KIC6603624lightcurve.fou'
data_2 = np.loadtxt(path_2)
names = ['KIC 3656476', 'KIC 6603624' ]


fig, axes = plt.subplots(2,1, figsize = (13,5))
fig_1, axes_1 = plt.subplots(2,1)


for index, data in enumerate([data_1, data_2]):
    ax = axes[index]
    ax.plot(data[:,0]*1000000, data[:,1]**2)

    ax.set_xlabel(r"Frequency [$\mu$ Hz]")
    ax.set_ylabel("Power")
    ax.set_title(names[index])

    if index == 0:
        ax.set_xlim([1600,2200])
        ax.arrow(1865,35, 80 ,0, head_width=8.5, head_length=5, fc='k', ec='k',length_includes_head=True)
        ax.arrow(1940,35, -80 ,0, head_width=8.5, head_length=5, fc='k', ec='k',length_includes_head=True)
        ax.annotate(s = r"$\Delta$ v",xy=(1900, 37))

        ax.arrow(1808,30, 5 ,0, head_width=2, head_length=1, fc='k', ec='k',length_includes_head=True)
        ax.arrow(1813,30, -5 ,0, head_width=2, head_length=1, fc='k', ec='k',length_includes_head=True)
        ax.annotate(s = r"$\Delta v_{nr}$",xy=(1810, 33))

        ax.annotate(s = r"A",xy=(1672, 20))
        ax.annotate(s = r"B",xy=(1765, 40))
        ax.annotate(s = r"C",xy=(1856, 78))
        ax.annotate(s = r"D",xy=(1950, 40))
        ax.annotate(s = r"E",xy=(2044, 36))
        ax.annotate(s = r"F",xy=(2137, 20))

        ax.annotate(s = r"a",xy=(1723, 18))
        ax.annotate(s = r"b",xy=(1815, 18))
        ax.annotate(s = r"c",xy=(1908, 18))
        ax.annotate(s = r"d",xy=(2001, 20))
        ax.annotate(s = r"e",xy=(2094, 20))
        peaks = []
        limts = [[1660, 1680], [1753, 1766], [1849, 1861],[1938,1952],[2036, 2050],[2132,2180]] # window that contains only one peak

    else:
        ax.set_xlim([2100, 2700])
        ax.annotate(s = r"I",xy=(2201, 11))
        ax.annotate(s = r"II",xy=(2312, 35))
        ax.annotate(s = r"III",xy=(2422, 16))
        ax.annotate(s = r"IV",xy=(2533, 18))
        ax.annotate(s = r"V",xy=(2644, 18))

        ax.annotate(s = r"i",xy=(2260, 10))
        ax.annotate(s = r"ii",xy=(2370, 15))
        ax.annotate(s = r"iii",xy=(2480, 10))
        ax.annotate(s = r"iv",xy=(2590, 8))
        limts = [[2190, 2202], [2304, 2330], [2411, 2430],[2519,2560],[2630, 2700]]


    peaks = []
    xx = data[:,0]*1000000
    yy = data[:,1]**2 

    peaks = peak_finder(xx,yy, limts)


    axx = axes_1[index]
    XX = [n for n in range(len(peaks) )]
    YY = peaks
    axx.set_title(names[index])
    axx.set_xticks(XX)
    axx.set_yticks(YY)
    axx.set_ylabel(r"Frequency [$\mu$ Hz]")
    axx.set_xlabel("Relative overtone number")
 
    p, V = np.polyfit(y = YY, x = XX, deg = 1, cov=True)
    overtone_spacing = p[0]
    overtone_error = np.sqrt(V[0][0])

    mean_density = (overtone_spacing/135)**2
    mean_density_err = 2*overtone_spacing*overtone_error/135**2

    radius_star = (1.05/mean_density)**(1/3)
    radius_star_err = radius_star*mean_density_err/(3*mean_density)

    speed_sound, speed_sound_err = calculate_speed_sound(radius_star, radius_star_err, overtone_spacing, overtone_error)

    overtone_numbers = overtone_numb_calc(radius_star, speed_sound, peaks)
        

    print("=================//================")
    print(f"Starting analysis for : {names[index]}")
    print(f"\t\tPeaks: {peaks}")
    print(f"\t\tDelta v {np.diff(peaks)}")
    print(f"\t\tOvertone numbers: {overtone_numbers}")

    print(f"\t\tFit params", p, np.sqrt(V[0][0]),  np.sqrt(V[1][1]))
    print(f"\t\tMean density [<d>_Sun]: {mean_density:.4f} {mean_density_err:.4f}")
    print(f"\t\tRadius [R_Sun]: {radius_star:.3f} {radius_star_err:.3f}")
    print(f"\t\tSpeed Sound [Km/s]: {speed_sound:.1f} {speed_sound_err:.1f}")
    


    axx.plot(XX, np.multiply(p[0],XX)+p[1], color = 'red', linestyle = '-.')
    axx.scatter(XX, YY, color = 'black')


fig.tight_layout()
fig_1.tight_layout()

colors = ['black', 'red']
lines = [Line2D([0], [0], linewidth=0, marker='o', color='black'), Line2D([0], [0], linewidth=3, linestyle='--', color='red')]
labels = ['Peak wavelength', 'fit']
axes_1[0].legend(lines, labels, ncol=2, bbox_to_anchor=(0.43, 1.05))
axes_1[1].legend(lines, labels, ncol=2, bbox_to_anchor=(0.43, 1.05))


fig.savefig("/home/amiguel/phd/classes/time_series/project/report/Figures/ex2_freq-power.png")
fig_1.savefig("/home/amiguel/phd/classes/time_series/project/report/Figures/ex2_overtone_freqs.png")

plt.show()