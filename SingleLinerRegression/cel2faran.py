import sklearn
import matplotlib.pyplot as plt
import numpy as np
import random

#y=mx+c
#F=1.8*C+32

x = list (range(0,10)) #C
y = [1.8*F+32 for F in x] #F
print(f'X: {x}')
print(f'Y: {y}')

plt.plot(x,y,'-*r')
plt.show()