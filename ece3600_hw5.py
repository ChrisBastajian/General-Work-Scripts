import numpy as np

#Problem 6.23 Part b):
R1 = 0.0384
X1 = 0.182
R2 = 0.0845
X2 = 0.0780
Xm = 32.7

s = 0.0235

V_line = 2400.0
Vph = V_line / np.sqrt(3) #this is V1
P_core = 15820 #from part a

def compute_Vrc(Rc):
    Z1 = R1 + 1j*X1 #stator branch
    Z2 = R2/s + 1j*X2 #rotor branhc
    Zxm = 1j*Xm

    #Xm // Rc
    Zxm_rc = 1 / (1/Zxm + 1/Rc)

    #Rotor // (Xm//Rc)
    Zpar = 1 / (1/Z2 + 1/Zxm_rc)

    # Total input impedance
    Zin = Z1 + Zpar
    I1 = Vph / Zin #stator current
    Vrc = (Zpar/Zpar+Z1)*Vph #voltage divider

    return Vrc, I1, Zin, Zpar, Zxm_rc

# Rc = 3 * |Vrc|^2 / P_core
Rc = 3 * Vph**2 / P_core #this is an initial guess assuming Vph=Vrc
alpha = 0.3
tol = 1e-12

for n in range(200):
    Vrc, I1, Zin, Zpar, Zxm_rc = compute_Vrc(Rc)
    Rc_new = 3 * abs(Vrc)**2 / P_core

    if abs(Rc_new - Rc) < tol:
        Rc = Rc_new
        break
    Rc = alpha*Rc_new + (1 - alpha)*Rc

print("Converged Rc =", Rc)
print("Voltage Vrc =", Vrc)
print("Magnitude |Vrc| =", abs(Vrc))
print("Stator current I1 =", I1)
print("Total input impedance Zin =", Zin)