import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#Problem 7.7:
Vt = 250 #V
slope = 150
Ra = 95 * 1e-3
n_rated = 1500 #rpm
V_rated = 250
P_rated = 35000 #W
I_f = 1.67

P_shaft = np.linspace(0, P_rated, 1000)
Ia = P_shaft/Vt

w_rated = 2*np.pi*n_rated/60 #rad/s
print(V_rated/w_rated)

omega = (Vt - Ia*Ra)/(V_rated/w_rated)
n=omega*60/(2*np.pi)

plt.figure()
plt.plot(P_shaft/1000, n)
plt.xlabel('Shaft Power (kW)', fontsize=14, font='Times New Roman')
plt.ylabel('Motor speed (rpm)', fontsize=14, font='Times New Roman')

plt.title(f"Plot For Part a", fontsize=16, font='Times New Roman')
plt.grid()
plt.show()

#Part b:
Ia = P_shaft/Vt
E = Vt - Ia*Ra
If_arr = E/slope

plt.figure()
plt.plot(P_shaft/1000, If_arr)
plt.xlabel('Shaft Power (kW)', fontsize=14, font='Times New Roman')
plt.ylabel('Field Current (A)', fontsize=14, font='Times New Roman')
plt.grid()
plt.title(f"Plot for Part b", fontsize=16, font='Times New Roman')
plt.show()

#Problem 7.15:
Va = 250 #V
P_rated = 75000 #W
#this is a separately excited DC motor
n_range = np.linspace(0, 2400, 10000)

#First condition with if constant:
n1_range = np.linspace(0, 1450, 5000)
Va1_range = np.linspace(0, 250)

#Second condition with Va constant:
Va2 = 250
n2_range = np.linspace(1450, 2400, 5000) #If decreases here

#Part a : find i_f, i_t, and torque for n=2400rpm, Va = 250, P=75kW
Ka_L = (Va*60)/(2*np.pi*2400*4.5)
Ia_a = 316.9 #found by hand
If_a = 4.261 #found by hand

torque_a = 75000/(2*np.pi*2400/60)
print(f"torque in part a: {torque_a}")

#Part b: find If, and Ia, if Va=250V, n=1450rpm
P_b = (1450/2400)*75000
print(f"Power in part b: {P_b}")
Ia_b = 187.133 #found by hand
If_b = 7.216 #found by hand
If_b = (Va * 60) / (2 * np.pi * 1450 * Ka_L)
print(f"If for part b (code based): {If_b}")
#Part c:
If_1 = np.linspace(If_b, If_b, 5000) #constant until n=1450
If_2 = (Va2*60)/(2*np.pi*n2_range*Ka_L)

Va_1 = np.linspace(0,250, 5000) #n goes from 0 to 1450
Va_2 = np.linspace(Va, Va, 5000) #Va=Va2... constant

Ia_1 = np.linspace(Ia_b, Ia_b, 5000) #constant and will increase for n2_range
Ia_2 = np.linspace(Ia_b, Ia_a, 5000) #reaches the highest point at n=2400rpm

#combining both ranges:
n_full = np.concatenate([n1_range, n2_range])
Va_full = np.concatenate([Va_1, Va_2])
Ia_full = np.concatenate([Ia_1, Ia_2])
If_full = np.concatenate([If_1, If_2])

#Ia vs speed
plt.subplot(3, 1, 1)
plt.plot(n_full, Ia_full, label='I_a (A)')
plt.title('Problem 7.15 part c')
plt.ylabel('Armature Current (A)')
plt.grid(True)
plt.legend()

#field current vs speed
plt.subplot(3, 1, 2)
plt.plot(n_full, If_full, label='I_f (A)')
plt.ylabel('Field Current (A)')
plt.grid(True)
plt.legend()

#Va vs speed
plt.subplot(3, 1, 3)
plt.plot(n_full, Va_full, label='V_a (V)')
plt.xlabel('Speed (rpm)')
plt.ylabel('Armature Voltage (V)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()