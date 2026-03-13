from vpython import *
scene.width = 900
scene.height = 500
scene.background = color.black
scene.center = vector(20,5,0)
scene.range = 40
scene.title = "Projectile Motion Simulation"
mode = input("Choose simulation mode (2D or 3D): ")
# PARAMETERS
g = vector(0,-9.81,0)     # gravity
k = float(input("Enter drag coefficient (try 0.0 - 0.5): "))                   # drag coefficient
m = 1                     # mass
dt = 0.01                 # timestep

# INITIAL CONDITIONS
initial_speed = float(input("Enter initial speed: "))
angle = float(input("Enter launch angle (degrees): "))*pi/180

if mode == "2D":
    velocity = vector(initial_speed*cos(angle), initial_speed*sin(angle), 0)

elif mode == "3D":
    z_speed = 5
    velocity = vector(initial_speed*cos(angle), initial_speed*sin(angle), z_speed)

else:
    print("Invalid mode, defaulting to 2D")
    velocity = vector(initial_speed*cos(angle), initial_speed*sin(angle), 0)
# CREATE OBJECTS
ground = box(pos=vector(25,-0.5,0), size=vector(100,1,20), color=vector(0.2,0.8,0.2))

ball = sphere(
    pos=vector(0,0,0),
    radius=0.5,
    color=color.red,
    make_trail=True,
    trail_radius=0.1
)
info = label(
    pos=vector(10,15,0),
    text="",
    box=False,
    height=16,
    color=color.white
)
# SIMULATION LOOP
while ball.pos.y >= 0:
    
    rate(100)
    info.text = f"Position: {ball.pos}\nVelocity: {velocity}"
    
    acceleration = g - (k/m)*velocity

    velocity = velocity + acceleration*dt

    ball.pos = ball.pos + velocity*dt
