import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy
from Particle389 import Charged_Particle
from Particle389 import Particle_Bunch

Bunch = Particle_Bunch(100, 1e-9, 0)
#Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0]), velocity = np.array([1.0, 0.0, 0.0]), acceleration = np.array([0.0, 0.0, 0.0]), Name = 'Charticle')

time = 0
TIME = []
deltaT = 1.0e-10
maxT = 1.0e-7

x_p = []
y_p = []
x_v = []
y_v = []
v_ave = []
x_spread = []
position_spread = []
KE = []
data = []

while time<maxT:
    time += deltaT

    for Charticle in Bunch.Bunch:
        Charticle.update(deltaT)
        Charticle.Lorentz(time)

    item = [time, copy.deepcopy(Bunch)]
    data.append(item)
    TIME.append(time)
    # x_p.append(Charticle.position[0])
    # y_p.append(Charticle.position[1])
    x_p.append(Bunch.average_xposition(time, deltaT))
    y_p.append(Bunch.average_yposition(time, deltaT))
    v_ave.append(Bunch.average_velocity(time, deltaT))
    KE.append(Bunch.kinetic_energy(time, deltaT))
    position_spread.append(Bunch.find_spread(time, deltaT))
    #x_spread.append(Bunch.find_spread_x(time, deltaT))
    
#print(KE)
    
plt.plot(x_p, y_p, 'r-', label='Particle Bunch Position in B Field')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()
    
plt.plot(TIME, v_ave, 'r-', label='Average Particle Bunch Velocity in B Field')
plt.xlabel('Time')
plt.ylabel('Average velocity of the bunch')
plt.show()

plt.plot(TIME, KE, 'r-', label='Kinetic Energy of the Particle Bunch over Time')
plt.xlabel('Time')
plt.ylabel('Kinetic Energy')
plt.show()

plt.plot(TIME, position_spread, 'r-', label='Spread of Particle Bunch in B Field')
plt.xlabel('Time')
plt.ylabel('Spread of the bunch')
plt.show()

# plt.plot(TIME, x_spread, 'r-', label='Spread of Particle Bunch in B Field')
# plt.xlabel('Time')
# plt.ylabel('Spread of the bunch in the x direction')
# plt.show()

# plt.plot(a_ave, TIME, 'r-', label='Particle Position in B Field')
# plt.xlabel('Average acceleration of the bunch')
# plt.ylabel('Time')
# plt.show()

# plt.plot(TIME, y_v, 'r-',label='Particle Y Velocity against Time in B Field')
# plt.xlabel('Time')
# plt.ylabel('Velocity in Y')
# plt.show()

# fig = plt.axes(projection = '3d', xlabel = 'time', ylabel = 'y position', zlabel = 'x position')
# fig.plot3D(TIME, y_p, x_p)
# plt.show()

# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# Axes3D.plot(x_p, y_p, TIME, 'r-',label='Particle Position in B Field over time')
# Axes3D.show()
