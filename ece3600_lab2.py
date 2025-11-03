import numpy as np
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

#The following covers the plot for part 2 of the lab:
sep_excited = {
    "Il": [0,0.19, 0.38, 0.64, 0.89, 1.32, 1.61],
    "Ea": [104, 101.7, 99.7, 97.1, 94.7, 90.5, 87.1]
}

self_excited = {
    "Il": [0, 0.24, 0.48, 0.83, 1.18, 1.74, 2.07],
    "Ea": [125, 125, 125, 125, 125, 118.9, 112.6]
}

plt.Figure()
plt.grid()
plt.scatter(sep_excited['Il'], sep_excited['Ea'])
plt.scatter(self_excited['Il'], self_excited['Ea'])
plt.legend(['Separately-Excited', 'Self-Excited'], loc='right')

plt.xlabel('Load Current (A)', fontsize=14, font='Times New Roman')
plt.ylabel('Terminal Voltage (V)', fontsize=14, font='Times New Roman')

plt.show()
