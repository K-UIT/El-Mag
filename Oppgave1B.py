import numpy as np
import matplotlib.pyplot as plt

# Konstanter
k = 1 # Konstanter
m = 1 # Masse
r = 1 # Radius
z0 = 1 # Starts posisjon
v0 = 0  # Starts hastighet
dt = 1e-2  # Tidssteg


# Starts variabler
z = z0; v = v0; t = 0
# Lager lister
t_vals = []; z_vals = []
# Flip logikk
flip = False

while t < 10:
    t += dt
    F = -k/np.sqrt(r**2+z**2)
    a = F/m
    v += a*dt
    z += v*dt
    t_vals.append(t)
    z_vals.append(z)
    # Endrer kraftens retning
    if z<0 and not flip:
        k= k*-1
        flip = True
    elif z>0 and flip:
        k = k*-1
        flip = False
    
    
t_vals = np.array(t_vals)
z_vals = np.array(z_vals)

# Plotter
plt.plot(t_vals, z_vals)
plt.axhline(y=0, color="black", linestyle="-")
plt.xlabel("Tid (s)")
plt.ylabel("Posisjon (z)")
plt.title(f"Partikelens bevegelse når r={r} og z0={z0}")
plt.show()

# Deriverer to ganger
z_dotdot = np.gradient(np.gradient(z_vals, dt), dt)

# Sammenligner negativ posisjon og akselerasjon
plt.plot(t_vals, z_dotdot, label="Akselerasjon")
plt.plot(t_vals, -z_vals, label="-Posisjon")
plt.axhline(y=0, color="Black", linestyle="-")
plt.legend()
plt.xlabel("Tid (s)")
plt.ylabel("Verdi")
plt.title("Akselerasjon mot posisjon")
plt.show()
