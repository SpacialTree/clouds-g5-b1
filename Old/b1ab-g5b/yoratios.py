import matplotlib
import matplotlib.pyplot as plt
import numpy as np

tau = np.arange(0.0001,30.0,0.25)
r1213 = (1 - np.e**(-tau)) / (1 - np.e**(-tau / 30.0))
r1218 = (1 - np.e**(-tau)) / (1 - np.e**(-tau / 200.0))

fig, ax = plt.subplots()
ax.plot(tau, r1213)
ax.plot(tau, r1218)

ax.set(xlabel='Opacity tau', ylabel='Ratio R', title='Radiative Transfer Ratios')
ax.grid()


plt.show()


