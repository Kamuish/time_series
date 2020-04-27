
import matplotlib.pyplot as plt 
plt.style.use("seaborn-dark")
import numpy as np 



def plot_kernel(path_raw, path_dan):
    data_raw = np.loadtxt(path_raw, delimiter=',', usecols=[1,2], skiprows=1)

    fig, axes = plt.subplots(2,1, figsize=(8,8))

    ax = axes[0]
    ax.plot(data_raw[:,0], data_raw[:,1])

    thresh_raw = 31000
    all_indexes_raw = np.where(data_raw[:,1] > thresh_raw)

    indexes_raw = [i for i in all_indexes_raw[0] if i not in [20]]


    print(f"{data_raw[:,1][indexes_raw]}")
    print(data_raw[:,0][indexes_raw])
    print(1/data_raw[:,0][indexes_raw])
    ax.scatter(data_raw[:,0][indexes_raw], data_raw[:,1][indexes_raw], color = 'red', marker='x')
    ax.set_xlabel("Frequency (cycles/year)")
    ax.set_ylabel("Spectrum")
    ax.set_title("Raw Periodogram")

    ax.set_xticks([0.1*i for i in range(11)])

    ax_smooth = axes[1]

    data_smooth = np.loadtxt(path_dan, delimiter=',', usecols=[1,2], skiprows=1)
    ax_smooth.plot(data_smooth[:,0], data_smooth[:,1])

    thresh_smooth = 3.1e+3
    all_indexes_smooth = np.where(data_smooth[:,1] >= max(data_smooth[:,1]))
    print(f"Smooth: {all_indexes_smooth}")
    indexes_smooth = [i for i in all_indexes_smooth[0] if i not in []]


    print(f"{data_smooth[:,1][indexes_smooth]}")
    print(data_smooth[:,0][indexes_smooth])
    print(1/data_smooth[:,0][indexes_smooth])
    ax_smooth.scatter(data_smooth[:,0][indexes_smooth], data_smooth[:,1][indexes_smooth], color = 'red', marker='x')
    ax_smooth.set_xlabel("Frequency (cycles/year)")
    ax_smooth.set_ylabel("Spectrum")
    ax_smooth.set_title("Smooth Periodogram (Daniell)")

    ax_smooth.set_xticks([0.1*i for i in range(11)])
    plt.tight_layout()
    plt.savefig("/home/amiguel/phd/classes/time_series/project/report/Figures/ex1_periodograms.png")
  
    plt.show()  

if __name__ == '__main__':
    plot_kernel("/home/amiguel/phd/classes/time_series/project/data_kernels/kernel_raw",
            "/home/amiguel/phd/classes/time_series/project/data_kernels/kernel_dan")

