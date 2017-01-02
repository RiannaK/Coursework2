"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

# Deliberately terrible code for teaching purposes
from matplotlib import pyplot as plt
from matplotlib import animation
import random


def update_boids(boids):
    formation_flying_distance = 10000
    formation_flying_strength = 0.125
    alert_distance = 100
    delta_t = 1
    move_to_middle_strength = 0.01

    xs, ys, xvs, yvs = boids
    num_boids = len(xs)

    for i in range(num_boids):
        for j in range(num_boids):
            # Fly towards the middle
            xvs[i] += (xs[j] - xs[i]) * move_to_middle_strength / num_boids
            yvs[i] += (ys[j] - ys[i]) * move_to_middle_strength / num_boids

            # Fly away from nearby boids
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < alert_distance:
                xvs[i] = xvs[i] + (xs[i] - xs[j])
                yvs[i] = yvs[i] + (ys[i] - ys[j])

    for i in range(num_boids):
        for j in range(num_boids):
            # Try to match speed with nearby boids
            if (xs[j] - xs[i]) ** 2 + (ys[j] - ys[i]) ** 2 < formation_flying_distance:
                xvs[i] += (xvs[j] - xvs[i]) * formation_flying_strength / num_boids
                yvs[i] += (yvs[j] - yvs[i]) * formation_flying_strength / num_boids

    # Move according to velocities
    for i in range(num_boids):
        xs[i] += xvs[i] * delta_t
        ys[i] += yvs[i] * delta_t


def animate(frame):
    update_boids(boids)
    scatter.set_offsets(list(zip(boids[0], boids[1])))


if __name__ == "__main__":
    num_boids = 50
    x_limits = -450, 50
    y_limits = 300, 600
    x_velocity_limits = 0,10
    y_velocity_limits = -20, 20
    axis_limits = -500, 1500

    boids_x = [random.uniform(*x_limits) for x in range(num_boids)]
    boids_y = [random.uniform(*y_limits) for x in range(num_boids)]
    boid_x_velocities = [random.uniform(*x_velocity_limits) for x in range(num_boids)]
    boid_y_velocities = [random.uniform(*y_velocity_limits) for x in range(num_boids)]
    boids = (boids_x, boids_y, boid_x_velocities, boid_y_velocities)

    figure = plt.figure()
    axes = plt.axes(xlim=axis_limits, ylim=axis_limits)
    scatter = axes.scatter(boids[0], boids[1])

    anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)
    plt.show()
