# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 19:02:08 2015

@author: capnk
"""
from scipy import signal
import matplotlib.pyplot as plt

s1 = signal.lti([2, 20], [1, 3, 2])
w, mag, phase = signal.bode(s1)

plt.figure()
plt.semilogx(w, mag)
plt.xlabel (r'Frequency ($\omega$)')
plt.ylabel (r'Magnitude ($dB$)') 
plt.savefig('Magnitude.png', dpi=300)   
plt.figure()
plt.semilogx(w, phase)
plt.xlabel (r'Frequency ($\omega$)')
plt.ylabel (r'Phase ($^\circ$)') 
plt.savefig('Amplitude.png', dpi=300) 
plt.show()