# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:31:35 2015

@author: capnk
"""

import numpy as np
from scipy import signal
from matplotlib import pyplot as plt

 
# Coefficients in numerator of transfer function
num = [2, 20]
# Coefficients in denominator of transfer function
# High order to low order, eg 1*s^2 + 0.1*s + 1
den = [1, 3, 2]
 
# Scan over zeta, a parameter for a second-order system
zetaRange = np.arange(0.1,1.1,0.1)
 
f1 = plt.figure()
for i in range(0,9):
    den = [1, 2*zetaRange[i], 1]
    print den
    s1 = signal.lti(num, den)
    #% Specify our own frequency range: np.arange(0.1, 5, 0.01)
    w, mag, phase = signal.bode(s1, np.arange(0.1, 5, 0.01).tolist())
    plt.semilogx (w, mag, color="blue", linewidth="1")
plt.xlabel ("Frequency")
plt.ylabel ("Magnitude")
plt.savefig ("mag.png", dpi=300, format="png")
 
plt.figure()
 
for i in range(0,9):
    den = [1, zetaRange[i], 1]
    s1 = signal.lti(num, den)
    w, mag, phase = signal.bode(s1, np.arange(0.1, 10, 0.02).tolist())
    plt.semilogx (w, phase, color="red", linewidth="1.1")
plt.xlabel ("Frequency")
plt.ylabel ("Amplitude")
plt.savefig ("phase.png", dpi=300, format="png")




plt.show()