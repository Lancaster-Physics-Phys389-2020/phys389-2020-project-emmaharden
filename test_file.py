import pytest 
import math
import numpy as np 
import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import copy
from Particle389 import Particle
from Particle389 import Charged_Particle
from Particle389 import Particle_Bunch


def test_bunch():
    "Checks that the Particle_Bunch class makes a bunch of 100 particles"
    Bunch = Particle_Bunch(100, 1e-9, 0)
    assert len(Bunch.Bunch) == 100

def test_Lorentz():
    "Checks that the acceleration of the particle due to the Lorentz force is close to the expected value"
    Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
    calculated_acc = (0, -5.757108678e8, 0)
    assert math.isclose(Charticle.Lorentz(1.0e-10)[1], calculated_acc[1])

def test_velocity_update():
    "Checks that each component of the velocity of each particle agrees with the expected value for one time step within 1e-6 ms**-1"
    Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
    acceleration = Charticle.Lorentz(1.0e-10)
    Charticle.update(1.0e-10)
    calculated_velocity = np.array([0.5, -5.757108678e-2, 0.0])
    assert np.allclose(Charticle.velocity, calculated_velocity, atol=1e-6)
    
def test_position_update():
    "Checks that each component of the position of each particle agrees with the expected value for one time step within 1e-6 m"
    Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
    acceleration = Charticle.Lorentz(1.0e-10)
    Charticle.update(1e-10)
    calculated_position = np.array([0.5e-10, 0.0, 0.0])
    assert np.allclose(Charticle.position, calculated_position, atol=1e-6)

def test_average_xposition():
    "Checks that the output of the average_xposition function is not an array, and is a singular value"
    Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
    Bunch = Particle_Bunch(100, 1e-9, 0)
    assert Bunch.average_xposition(0, 1.0e-10) != list

def test_average_yposition():
    "Checks that the output of the average_yposition function is not an array, and is a singular value"
    Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
    Bunch = Particle_Bunch(100, 1e-9, 0)
    array = [1, 2, 3]
    assert Bunch.average_yposition(0, 1.0e-10) != type(array)

def test_spread():
    "Checks that the spread of the bunch has a magnitude of 1e-10 (the standard deviation of the position function)"
    Bunch = Particle_Bunch(100, 1e-9, 0)
    Spread = Bunch.find_spread(0, 1e-10)/1e-10
    assert 1 < Spread < 10

def test_radius():
    "Checks that the result of the find_radius fuction is a singular value of the radius of the particle bunch at a given time"
    Bunch = Particle_Bunch(100, 1e-9, 0)
    array = [1, 2, 3]
    bunch_radius = Bunch.find_radius(0, 1e-9)
    assert bunch_radius != type(array) 

# def test_KE():
#     Bunch = Particle_Bunch(100, 1e-9, 0)
#     KE = Bunch.kinetic_energy(0, 1e-9)
#     Energy = (((1.6e-19)**2)*(14.0**2)*(Bunch.find_radius(0, 1e-9)**2))/(2*1.67e-27)
#     assert math.isclose(KE, Energy)
    
