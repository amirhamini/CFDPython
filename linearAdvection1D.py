import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# To solve equation u_t + c u_x = 0 with
# Spatial mesh
L = 2
nx = 40
x = np.linspace(0, L, nx + 1)
dx = x[1] - x[0]

# Wave speed of equation u_t + c u_x = 0
c = 1

# Temporal mesh
# CFL = cdt/dx
CFL = 0.5
dt = CFL*dx/c
nt = 800

# IC
u = np.ones(nx + 1)
u[.5/dx: 1/dx+1] = 2

fig01 = plt.figure(1, figsize=(10, 5), dpi=90)
ax = fig01.add_subplot(111)
ax.plot(x, u)
ax.set_ylim([0, 3])
ax.set_title("Initial Condtion", fontsize=20, y=1)
plt.show()

# Solving the equation u_t + c u_x = 0
# using the Forward Difference scheme for the time derivative and
# the Backward Difference scheme for the space derivative.
u_sol = []
for n in range(nt):
    un = u.copy()
    u_sol.append(un)
    for i in range(nx + 1):
        u[i] = un[i]-c*dt/dx*(un[i]-un[i-1])

# Plotting the result in animation form
# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure(1, figsize=(10, 5), dpi=90)
ax = plt.axes(xlim=(0, 2), ylim=(0, 3))
ax.set_title("Results", fontsize=20, y=1)
line, = ax.plot([], [], lw=2)


# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,


# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, L, nx + 1)
    y = u_sol[i]
    line.set_data(x, y)
    return line,

# Calling the animator
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=nt, interval=nt/10.0, blit=False)

plt.show()
