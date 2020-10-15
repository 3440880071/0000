import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2*np.pi,0.01)
y=np.cos(x)


plt.plot(x,y)
plt.xlabel('t')
plt.ylabel('X(t)')
plt.title('x(t)=Acos(ωt+ψ)')

plt.show()