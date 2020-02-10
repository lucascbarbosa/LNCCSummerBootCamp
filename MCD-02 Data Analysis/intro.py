import matplotlib.pyplot as plt

hh = [1.65,1.7,1.8,1.9]
w = [(h**2)*22.5 for h in hh]

plt.plot(hh,w)