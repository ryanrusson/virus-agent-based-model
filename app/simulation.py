import numpy as np
from agents import People
from random import randint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

xmin, xmax = (0, 200)
ymin, ymax = (0, 200)
frames = 1000
agentnum = 100
infected_agent = randint(0, agentnum)
socdistance = 6.0
step = 2

people = []
points = []

# Set up the first plot
fig, ax = plt.subplots()
ax.set_axis_off()

random_step = False


# Define the plot initializer
def init():
    global points, people, infected

    # Initialize the agents
    for idx in range(agentnum):
        xinit = randint(xmin, xmax)
        yinit = randint(ymin, ymax)

        # Set up a "temp" person
        temp = People(
            xinit,
            yinit,
            idx,
            socdistance,
            xlim=(xmin, xmax),
            ylim=(ymin, ymax),
            step=step,
        )

        # Set the infected person
        if idx == infected_agent:
            temp.contracted(1)

        # Update the list of people and plot points
        people.append(temp)
        points.append(ax.plot(temp.x, temp.y, color=temp.color, marker=temp.marker))

    # Set up the plot
    ax.set_ylim(ymin, ymax)
    ax.set_xlim(xmin, xmax)
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    return points


# Define the run function to update the simulation
def run(i):
    global points, people, distance

    # Gather up everyone's current position
    curpos = [(p.x, p.y) for p in people]

    for idx, point in enumerate(points):

        # Have the person take a step
        if random_step:
            dist = people[idx].random_step(curpos)
        else:
            dist = people[idx].avoidance_step(curpos)

        # Determine if that person infects someone
        if people[idx].infected == 1:

            for d in dist:
                if d[1] < socdistance and d[0] != idx:
                    people[d[0]].contracted(1)

        # Update the person's marker
        point[0].set_data(people[idx].x, people[idx].y)
        point[0].set_marker(people[idx].marker)
        point[0].set_color(people[idx].color)


ani = FuncAnimation(fig, run, blit=False, frames=frames, init_func=init, repeat=False)
plt.show()
