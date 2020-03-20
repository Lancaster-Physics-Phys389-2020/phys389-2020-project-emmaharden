import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import copy
from Particle389 import Charged_Particle
from Particle389 import Particle_Bunch
import pandas as pd

"""
Here I create a bunch of 100 particles with position spread 1e-9 m and velocity spread 0(i.e.
they all have the same velocity). I also set the start time to be zero and for each time step
to be 1.0e-10 seconds, doing up to a maximum time value of 1.0e-7 seconds.
"""

Bunch = Particle_Bunch(100, 1e-9, 0)

time = 0
TIME = []
deltaT = 5.0e-11
maxT = 1.0e-5
max_radius = 0.2 
"This is the radius at which a proton in a magnetic field of 14 Tesla would reach close to the speed of light"

"""
Here I create lists ready for the data to fill. These lists can then be saved to a dataframe.
"""

x_p = []
y_p = []
x_v = []
y_v = []
v_ave = []
x_spread = []
position_spread = []
KE = []
orbits = []
radius_of_orbit = []
data = []

"""
The while loop below runs the functions written in my Particle389 Document for each 
particle in the bunch I created previously, and appends the data to the lists I had
set up. It does so until the radius of orbit reaches the maximum value of radius of
orbit set previously.

"""

while time<maxT:
    time += deltaT
    for Charticle in Bunch.Bunch:
        Charticle.update(deltaT)
        Charticle.Lorentz(time)
        Charticle.Period()
        
    item = [time, copy.deepcopy(Bunch)]
    data.append(item)
    TIME.append(time)
    x_p.append(Bunch.average_xposition(time, deltaT))
    y_p.append(Bunch.average_yposition(time, deltaT))
    v_ave.append(Bunch.average_velocity(time, deltaT))
    KE.append(Bunch.kinetic_energy(time, deltaT))
    orbits = TIME/(Charticle.Period())
    position_spread.append(Bunch.find_spread(time, deltaT))
    radius_of_orbit.append(Bunch.find_radius(time, deltaT))

    if Bunch.find_radius(time, deltaT) > max_radius:
            break


"""
Here I create a dataframe to save all of my lists to. This allows for more in depth data analysis, and it can efficiently handle
large amounts of data, allowing for a larger bunch of particles to be investigated for a longer period of time if desired.

"""

dataset = {"Time":TIME,  "AverageXPosition":x_p, "AverageYPosition":y_p, "AverageVelocity":v_ave, "AverageKE":KE, "NumberOfOrbits":orbits, "PositionSpread":position_spread, "RadiusOfOrbit":radius_of_orbit}
df = pd.DataFrame(data=dataset)
df.to_pickle(r'H:/My Documents/PHYS389/Cyclotron_Data')

print('Done')
    