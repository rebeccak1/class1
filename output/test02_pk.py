import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/n/home12/rebecca.krall/class1/output/test02_pk.dat', '/n/home12/rebecca.krall/class1/output/mp_lcdm01_pk.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['test02_pk', 'mp_lcdm01_pk']

fig, ax = plt.subplots()
y_axis = [u'P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()