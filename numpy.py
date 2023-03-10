# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:07:29 2023

@author: user
"""


import numpy as np
import matplotlib.pyplot as plt

x  = np.linspace(0,2*np.pi,100)
y = np.sin(x)
print(y)
plt.plot(x,y)


