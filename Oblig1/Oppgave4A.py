import numpy as np
import matplotlib.pyplot as plt

# Definerer rutenettet
x = np.linspace(-1, 1, 100)
z = np.linspace(-1, 1, 100)
X, Z = np.meshgrid(x, z)

# Definerer ladningene
q1, q2 = 1, -1  
pos1 = np.array([0, 0.05])
pos2 = np.array([0, -0.05])
r0 = 0.025

# Beregner V
V = q1/np.sqrt((X-pos1[0])**2+(Z-pos1[1])**2+r0**2)+q2/np.sqrt((X-pos2[0])**2+(Z-pos2[1])**2+r0**2)

# Plott potensial
plt.figure(figsize=(6, 6))
plt.contour(X, Z, V, levels=np.linspace(-6,6,30), cmap="viridis")
plt.colorbar(label="Potensial V")

# Plott ladningene
plt.scatter([pos1[0], pos2[0]], [pos1[1], pos2[1]], color=["red", "blue"])
plt.xlabel("x")
plt.ylabel("z")
plt.title("Ekvipotensialflate for en dipol")
plt.grid()
plt.show()