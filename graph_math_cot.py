import matplotlib.pyplot as plt
import numpy as np
import math
x = np.linspace(-math.pi, math.pi, 100)
tan=[math.tan(val) for val in x]
cot=[1/math.tan(val) for val in x]
fig, ax=plt.subplots(figsize=(5.5, 3.5))
ax.plot(x, tan, color='blue', ls='-', lw=1, label='tan')
ax.plot(x, cot, color='red', ls='-', lw=1, label='cot')
ax.set_xscale('linear')
ax.set_yscale('linear')
ax.set_xlim([-math.pi/2, math.pi/2])
ax.set_ylim([-20, 20])
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc='best') 
ax.grid(ls=':')