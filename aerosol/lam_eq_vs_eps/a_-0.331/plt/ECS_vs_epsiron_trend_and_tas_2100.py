import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

plt.rcParams["font.size"]=20
F_2x=3.93
xlim_min=2
xlim_max=5
plt.xlim(xlim_min,xlim_max)
ylim_min=0.
ylim_max=4
plt.ylim(ylim_min, ylim_max)
plt.axvline(x=2.5,color='green',linestyle='dashed')
plt.axvline(x=4,color='green',linestyle='dashed')
plt.axvline(x=3,color='blue',linestyle='dashed')


dd=0.05
lam_eqs=np.arange(-2.0,-0.4,dd)
epss=np.arange(0.,4.05,dd)

nx=len(lam_eqs)
ny=len(epss)
x=-F_2x/lam_eqs
y=epss
filename='../out/all/tas_trend_1981-2014.txt'
invalues=np.loadtxt(filename)
z=invalues*10
X,Y = np.meshgrid(x, y)
Z=z.reshape(nx,ny).T
plt.contourf(X, Y, Z,cmap="rainbow",levels=np.arange(0.1,0.55,0.05))
#plt.contourf(X, Y, Z,cmap="rainbow")
plt.colorbar(ticks=np.arange(0.1,0.6,0.1))
color_name='black'
obs=0.22
CS = plt.contour(X,Y,Z,levels=[obs],colors=color_name)
CS = plt.contour(X,Y,Z,levels=[0.153,0.287],colors=color_name,linestyles='dashed')

filename='../out/all/tas_2100.txt'
invalues=np.loadtxt(filename)
z=invalues
Z=z.reshape(nx,ny).T
plt.contour(X, Y, Z,levels=20)

plt.scatter(4,1,color='red',s=100)
plt.scatter(4,1.65,color='darkorange',s=100)
plt.scatter(2.95,1,color='blue',s=100)
plt.scatter(2.5,2.32,color='green',s=100)

plt.minorticks_on()
plt.grid()
filename='/home/saga-t/work/python/fig/ECS_vs_epsiron_trend_and_tas_2100'+'.png'
plt.savefig(filename, dpi=300)
plt.show()
