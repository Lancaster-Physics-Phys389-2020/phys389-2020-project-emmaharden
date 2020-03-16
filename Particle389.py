import math
import numpy as np
import matplotlib.pyplot as plt
import copy
import scipy.constants as sc

class Particle:

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
        return self.velocity #, self.position

    #def updateEC(self, deltaT):
    #    """Updates the position and velocity of the planet after each time step of deltaT using the Euler-Cramer Method"""
    #    self.velocity = self.velocity + self.acceleration*deltaT
    #    self.position = self.position + self.velocity*deltaT
        
    # def update_acceleration(self, other_particle):
    #     """Updates the acceleration of each planet after each time step of deltaT"""
    #     r = self.position - other_particle.position 
    #     unit_vector = r/(np.linalg.norm(r))
    #     G = 6.674e-11
    #     acceleration = (-(G*other_particle.mass)/(np.linalg.norm(r))**2)*unit_vector
    #     return acceleration

    #def kinetic_energy(self):
    #    """Calculates the kinetic energy of the planet"""
    #    KE = 0.5*self.mass*((np.linalg.norm(self.velocity))**2)
    #    return KE

class Charged_Particle(Particle):

    def __init__(self, position = np.array([0.0, 0.0, 0.0], dtype=float), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float), Name = 'Particle', mass = 1.67e-27, charge = 1.6e-19):
        Particle.__init__(self, position, velocity, acceleration, Name, mass)
        self.charge = charge

    def __repr__(self):
        return 'Particle: %10s, Charge: %.5e, Mass: %.5e, Position: %s, Velocity: %s, Acceleration:%s'%(self.Name, self.charge, self.mass,self.position, self.velocity,self.acceleration)
        
    def B_field(self):
        B = np.array([0.0, 0.0, 2.0]) 
        F = self.charge*np.cross(self.velocity, B) 
        self.acceleration = F/self.mass 
        
    def Period(self):
        "Finds the period of orbit of the charged particles"
        B = np.array([0.0, 0.0, 2.0]) 
        T = (2.0*math.pi*self.mass)/(self.charge*np.linalg.norm(B))
        return(T)

    def E_field(self, time):
        B = np.array([0.0, 0.0, 2.0]) 
        w = (self.charge*np.linalg.norm(B))/self.mass
        E = np.array([0, 0.5*math.cos(w*time), 0])
        F = self.charge*E
        self.acceleration = F/self.mass

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

    def __init__(self, no_particles, position_spread, velocity_spread):
        self.Bunch = []
        while (len(self.Bunch) < no_particles):
            particle = Charged_Particle(position = np.random.normal(loc=0.0, scale=1e-10, size=3), velocity = np.array([0.5, 0.0, 0.0], dtype=float), acceleration = np.array([0.0, 0.0, 0.0], dtype=float))
            self.Bunch.append(particle)

    def __repr__(self):
        return '{0}'%(self.Bunch)
    
    def average_xposition(self, time, deltaT):
        "Calculates the average position in the x plane of the particles in the bunch"
        x_bunch = []
        current_x = []
        for particle in self.Bunch:
            current_x.append(particle.position[0])
        av_x = sum(current_x)/len(current_x)
        x_bunch.append(av_x)
        return x_bunch

    def average_yposition(self, time, deltaT):
        "Calculates the average position in the y plane of the particles in the bunch"
        y_bunch = []
        current_y = []
        for particle in self.Bunch:
            current_y.append(particle.position[1])
        av_y = sum(current_y)/len(current_y)
        y_bunch.append(av_y)
        return y_bunch

    def average_velocity(self, time, deltaT):
        "Calculates the average velocity of the particles in the bunch"
        v_bunch = []
        current_v = []
        for particle in self.Bunch:
            current_v.append(np.linalg.norm(particle.velocity))
        av_v = sum(current_v)/len(current_v)
        v_bunch.append(av_v)
        return v_bunch
        
    def find_spread_x(self, time, deltaT):
        spread_x = []
        current_x = []
        current_y = []
        for particle in self.Bunch:
            current_x.append(particle.position[0])
            current_y.append(particle.position[1])
        range_x = max(current_x) - min(current_x)
        spread_x.append(range_x)
        return spread_x

    def find_spread(self, time, deltaT):
        "Finds the spread in the position"
        bunch_spread = []
        positions = []
        for particle in self.Bunch:
            positions.append(np.linalg.norm(particle.position))
        bunch_spread = max(positions) - min(positions)
        return bunch_spread 

    def kinetic_energy(self, time, deltaT):
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








