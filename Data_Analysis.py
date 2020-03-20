import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy
from Particle389 import Charged_Particle
from Particle389 import Particle_Bunch
import pandas as pd

Cyclotron = pd.read_pickle(r'H:/My Documents/PHYS389/Cyclotron_Data')

plt.plot(Cyclotron.AverageXPosition, Cyclotron.AverageYPosition, 'r-', label='Particle Bunch Position in B Field')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.show()
    
plt.plot(Cyclotron.Time, Cyclotron.AverageVelocity, 'r-', label='Average Particle Bunch Velocity in B Field')
plt.xlabel('Time')
plt.ylabel('Average velocity of the bunch')
plt.show()

plt.plot(Cyclotron.Time, Cyclotron.AverageKE, 'r-', label='Kinetic Energy of the Particle Bunch over Time')
plt.xlabel('Time')
plt.ylabel('Kinetic Energy')
plt.show()

plt.plot(Cyclotron.Time, Cyclotron.PositionSpread, 'r-', label='Spread of Particle Bunch in B Field')
plt.xlabel('Time')
plt.ylabel('Spread of the bunch')
plt.show()

plt.plot(Cyclotron.NumberOfOrbits, Cyclotron.PositionSpread, 'r-', label='Spread of Particle Bunch in B Field as a Function of the Number of Orbits')
plt.xlabel('Number of Orbits')
plt.ylabel('Spread of the bunch')
plt.show()

plt.plot(Cyclotron.Time, Cyclotron.RadiusOfOrbit, 'r-', label='Average Radius of Orbit of Particle Bunch in B Field')
plt.xlabel('Time')
plt.ylabel('Radius of orbit of the bunch')
plt.show()