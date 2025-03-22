import numpy as np
import matplotlib.pyplot as plt
def calc(vf,tm):
    # Definerer konstanter
    V0 = 1 #V
    C = 100E-9 # F
    R = 1E3 # ohm
    tmax = tm # sekunder
    vinkelfrekvens = vf# rad/s
    dt = 1e-6 # tidssteg
    
    V_Ss = [0] # V_S for alle tidssteg
    V_Cs = [0] # V_C for alle tidssteg
    ts = [0] # t for alle tidssteg
    while ts[-1] < tmax:
        V_Cs.append( V_Cs[-1]+(V_Ss[-1]-V_Cs[-1])/(R*C)*dt )
        ts.append( ts[-1] + dt )
        V_Ss.append( V0* np.sin(vinkelfrekvens* ts[-1]) )
    return V_Ss, V_Cs,np.array(ts)* 1000

VS1, VC1, t1 = calc(1e3, 3e-3)
VS2, VC2, t2 = calc(1e4, 0.5e-3)
VS3, VC3, t3 = calc(1e5, 0.5e-4)



fig, ax = plt.subplots(1,3, dpi = 200, figsize =(12,4))

ax[0].plot(t1, VS1, label = "$V_S$", color = [0,0,0], lw = 0.3)
ax[0].plot(t1, VC1, label = "$V_C$", color = [0,0.5,1])
ax[0].legend()
ax[0].set_ylabel("Spenning [V]")
ax[0].set_xlabel("Tid [ms]")
ax[0].set_title("Vinkelfrekvens $\omega$ = 1k")


ax[1].plot(t2, VS2, label = "$V_S$", color = [0,0,0], lw = 0.3)
ax[1].plot(t2, VC2, label = "$V_C$", color = [0,0.5,1])
ax[1].legend()
ax[1].set_xlabel("Tid [ms]")
ax[1].set_title("Vinkelfrekvens $\omega$ = 10k")


ax[2].plot(t3, VS3, label = "$V_S$", color = [0,0,0], lw = 0.3)
ax[2].plot(t3, VC3, label = "$V_C$", color = [0,0.5,1])
ax[2].legend()
ax[2].set_xlabel("Tid [ms]")
ax[2].set_title("Vinkelfrekvens $\omega$ = 100k")
fig.show()