import numpy as np 

def peak_finder(xx, yy, limts):
    peaks = []
    for lims in limts:
        inds = np.where(np.logical_and(xx >= lims[0], xx <= lims[1]))
        xx_l = xx[inds]
        yy_l = yy[inds]
        max_ind = np.argmax(yy_l)
        peaks.append(xx_l[max_ind])

    return peaks