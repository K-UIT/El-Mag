# Oppgave 4B
import numpy as np
import matplotlib.pyplot as plt

# Definerer rutenettet
x = np.linspace(-1, 1, 500)
z = np.linspace(-1, 1, 500)
X, Z = np.meshgrid(x, z)

# Definerer ladningene
qO, qH = -2, 1  
pos1 = np.array([0, 0.005])
l = (pos1[1]+0.05)*np.tan(np.radians(105/2))
pos2 = np.array([l, -0.05])
pos3 = np.array([-l, -0.05])
r0 = 0.025

# Beregner V
V = qO/np.sqrt((X-pos1[0])**2+(Z-pos1[1])**2+r0**2)+qH/np.sqrt((X-pos2[0])**2+(Z-pos2[1])**2+r0**2)+qH/np.sqrt((X-pos3[0])**2+(Z-pos3[1])**2+r0**2)

# Plott potensial
plt.figure(figsize=(6, 6))
plt.contour(X, Z, V, levels=np.linspace(-6,6,30), cmap="viridis")
plt.colorbar(label="Potensial V")

# Plott ladningene
plt.scatter([pos1[0], pos2[0], pos3[0]], [pos1[1], pos2[1], pos3[1]], color=["blue", "red", "red"])
plt.xlabel("x")
plt.ylabel("z")
plt.title("Ekvipotensialflate for vannmolekyl")
plt.grid()
plt.show()