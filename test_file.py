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
    Bunch = Particle_Bunch(100, 1e-9, 0)
    assert len(Bunch.Bunch) == 100

def test_Lorentz():
    Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
    calculated_acc = (0, -5.757108678e8, 0)
    assert math.isclose(Charticle.Lorentz(1.0e-10)[1], calculated_acc[1])

# def test_velocity_update():
#     Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
#     acceleration = Charticle.Lorentz(1.0e-10)
#     v, p = Charticle.update(1.0e-10)
#     calculated_v = np.array([0.5, -5.757108678e-2, 0.0])
#     assert np.allclose(v, calculated_v, atol=1e-6)

def test_velocity_update():
        Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
        acceleration = Charticle.Lorentz(1.0e-10)
        Charticle.update(1.0e-10)
        calculated_velocity = np.array([0.5, -5.757108678e-2, 0.0])
        assert np.allclose(Charticle.velocity, calculated_velocity, atol=1e-6)
    
# def test_position_update():
#     Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
#     acceleration = Charticle.Lorentz(1.0e-10)
#     velocity, p = Charticle.update(1.0e-10)
#     calculated_position = np.array[(0.5e-10, 0.0, 0.0)]
#     assert np.allclose(p, calculated_position, atol=1e-6)
    
def test_position_update():
    Charticle = Charged_Particle(position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19)
    acceleration = Charticle.Lorentz(1.0e-10)
    Charticle.update(1e-10)
    calculated_position = np.array[(0.5e-10, 0.0, 0.0)]
    assert math.isclose(Charticle.position, calculated_position, atol=1e-6)

# def test_KE():


