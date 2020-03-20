import math
import numpy as np
import matplotlib.pyplot as plt
import copy
import scipy.constants as sc

class Particle:
    """
    This class creates a massive particle with mass = proton mass, and gives it an initial position, velocity and acceleration in 3D.
    It also uses the Euler method to update the position and velocity of the particle for each time step, delta T.

    """
    def __init__(self, position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.0, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27):
        self.position = np.array(position, dtype=float)
        self.velocity = np.array(velocity)
        self.acceleration = np.array(acceleration)
        self.Name = Name
        self.mass = mass

    def __repr__(self):
        return 'Particle: %10s, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(self.Name, self.mass,self.position, self.velocity,self.acceleration)

    def update(self, deltaT):
        """Updates the position and velocity of the particle after each time step of deltaT using Euler's Method"""
        self.velocity = self.velocity + self.acceleration*deltaT
        self.position = self.position + self.velocity*deltaT
        return self.velocity, self.position

class Charged_Particle(Particle):
    """
    This class inherits from the Particle class and adds a charge to the particle, in order to make a proton.
    It also creates a constant magnetic field and a time varying electric field with frequency equal to the frequency of orbit of the proton.
    These fields are then used to clculate the Lorentz force on the particle, and the acceleration due to the Lorentz force. 

    """
    def __init__(self, position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19):
        Particle.__init__(self, position, velocity, acceleration, Name, mass)
        self.charge = charge

    def __repr__(self):
        return 'Particle: %10s, Charge: %.5e, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(self.Name, self.charge, self.mass,self.position, self.velocity,self.acceleration)
          
    def Period(self):
        "Finds the period of orbit of the charged particles"
        B = np.array([0.0, 0.0, 14.0]) 
        T = (2.0*math.pi*self.mass)/(self.charge*np.linalg.norm(B))
        return(T)

    def Lorentz(self, time):
        "Calculates the acceleration on each particle due to the magnetic and electric fields"
        B = np.array([0.0, 0.0, 14.0]) 
        F_B = self.charge*np.cross(self.velocity, B)
        w = (self.charge*np.linalg.norm(B))/self.mass
        E = np.array([0, math.cos(w*time), 0])
        F_E = self.charge*E
        F_tot = F_B + F_E
        self.acceleration = F_tot/self.mass
        return self.acceleration

class Particle_Bunch:
    """
    This class creates a bunch of charged particles using the Charged_Particle class created previously.
    Each particle has the same mass, charge, initial velocity and acceleration, but they all have random positions drawn from a normal 
    distribution with standard deviation 1e-10 m.

    """

    def __init__(self, no_particles, position_spread, velocity_spread):
        "Creating a bunch of charged particles by using the Charged_Particle class to make a list of particles with random positions"
        self.Bunch = []
        while (len(self.Bunch) < no_particles):
            particle = Charged_Particle(position = np.random.normal(loc=0.0, scale=1e-10, size=3), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float))
            self.Bunch.append(particle)

    def __repr__(self):
        return '{0}'%(self.Bunch)
    
    def average_xposition(self, time, deltaT):
        "Calculates the average position of the particles in the bunch in the x plane"
        current_x = []
        for particle in self.Bunch:
            current_x.append(particle.position[0])
        av_x = sum(current_x)/len(current_x)
        return av_x

    def average_yposition(self, time, deltaT):
        "Calculates the average position of the particles in the bunch in the y plane"
        current_y = []
        for particle in self.Bunch:
            current_y.append(particle.position[1])
        av_y = sum(current_y)/len(current_y)
        return av_y

    def average_velocity(self, time, deltaT):
        """
        Calculates the average velocity of the particles in the bunch. 
        Returns a singular value, which is the average velocity for one time step in ms**-1.

        """
        current_v = []
        for particle in self.Bunch:
            current_v.append(np.linalg.norm(particle.velocity))
        av_v = sum(current_v)/len(current_v)
        return av_v
        
    def find_spread(self, time, deltaT):
        """
        Finds the spread in the position of the particles in the bunch.
        Returns a singular value, the spread in magnitude of the positions in m.

        """
        bunch_spread = []
        positions = []
        for particle in self.Bunch:
            positions.append(np.linalg.norm(particle.position))
        bunch_spread = max(positions) - min(positions)
        return bunch_spread 

    def kinetic_energy(self, time, deltaT):
        """
        Calcuates the average kinetic energy of the bunch of particles.
        Takes into account relativistic effects (when gamma < 1) to allow plotting at high velocities.
        
        """
        energies = []
        for particle in self.Bunch:
            v = np.linalg.norm(particle.velocity)
            beta = v/sc.c
            gamma = (1 - beta**2)**0.5
            if gamma < 1:
                relativistic = particle.mass*((sc.c)**2)*((1/gamma)-1)
                energies.append(relativistic)
            else:
                energies.append(0.5*(sc.m_e)*(v**2))
        return sum(energies)

    def find_radius(self, time, deltaT):
        """
        Calculates the average radius of orbit of the bunch of particles.
        Returns a singular value, the magnitude of the radius in m.

        """
        radii = []
        for particle in self.Bunch:
            radius = np.linalg.norm(particle.position)
            radii.append(radius)
        av_radius = sum(radii)/len(radii)
        return av_radius