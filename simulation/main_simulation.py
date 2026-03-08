from vpython import *

# PARAMETERS
g = vector(0,-9.81,0)     # gravity
k = 0.1                   # drag coefficient
m = 1                     # mass
dt = 0.01                 # timestep

# INITIAL CONDITIONS
initial_speed = 20
angle = 45*pi/180

velocity = vector(initial_speed*cos(angle), initial_speed*sin(angle), 0)

# CREATE OBJECTS
ground = box(pos=vector(0,-0.5,0), size=vector(50,1,10), color=color.green)

ball = sphere(pos=vector(0,0,0), radius=0.3, color=color.red, make_trail=True)

# SIMULATION LOOP
while ball.pos.y >= 0:
    
    rate(100)

    acceleration = g - (k/m)*velocity

    velocity = velocity + acceleration*dt

    ball.pos = ball.pos + velocity*dt
