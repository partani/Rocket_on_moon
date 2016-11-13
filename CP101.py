import numpy as np
import matplotlib.pyplot as plt
import time

print'Some Assumptions'
print'1. The moon has no Atmosphere, hence there is no drag force'
print'2. Dynamic values of dt is used to make the simulation faster'

print'The escape velocity at surface of moon is 2.38 km/s'

M0 = input("Enter the mass of rocket in kg, ")
mass = M0
c = input("Enter the velocity of exhaust gas in m/s, ")
A = input("Enter the mass flow rate of exhaust gas in kg/s, ")
dt1 = 0.1

t = 0
global vpre
vpre = 0

e =0
R = 1737000
i = 0
velk = 0
g = 1.62519
dr = 0
E = -10
timeout = time.time() + 10

while (E  < 0):
    t = t + dt1
    mass = mass - A*dt1
    e = R/(R+dr)
    velk = -g*e*e*dt1 +  dt1*c*A/mass  + velk
    if(velk < 0):
        velk = 0
    dr = velk*dt1 +dr
    E = mass*(velk*velk/2 - 4903893739360/(R+dr)) 
    if(time.time() > timeout):
        print 'Such Rocket cannot be launched'
        quit()

print 'Velocity at escape' 
print velk
print 'Distance at which the Escape condition meet'
print dr

print "The taken to escape is"
print t

dt = t / 1000000
print 'dt for this simulation is '
print dt
print 'The Fuel needed for the launch is'
print M0 - mass 


tim = np.zeros((t/dt+1,1))
vel = np.zeros((t/dt + 1,1))
dis = np.zeros((t/dt +1,1))

j = M0
i = 0
for i in range (0, int(t/dt)):
    tim[i+1] = tim[i] +dt
    mass = M0- A*tim[i+1]
    e = R/(R+dis[i])
    vel[i+1] = vel[i] - g*e*e*dt + dt*c*A/mass
    if(vel[i+1] <= 0 ):
        vel[i+1] = 0
        j = mass
    dis[i+1] = dis[i] + vel[i+1]*dt
    
print 'For the given velocity of exhaust gas and mass flow rate'
print 'The Shuttle which can be launched should have mass'
print mass
print 'and mass of fuel'
print j-mass
print 'Giving total mass'
print  j

    

plt.figure(1)
plt.subplot(211)
plt.plot(tim, vel)
plt.xlabel('Time in s')
plt.ylabel('Velocity in m/s')
plt.title('Simulation of Rocket')



plt.subplot(212)
plt.plot(tim,dis)
plt.xlabel('Time in s')
plt.ylabel('Distance in m')
plt.show()
