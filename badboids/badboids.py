"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

# Deliberately terrible code for teaching purposes
from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np


class Boids:

    def __init__(self, x_positions, y_positions, x_velocities, y_velocities):
        self.x_positions = x_positions
        self.y_positions = y_positions
        self.x_velocities = x_velocities
        self.y_velocities = y_velocities
        self.num_boids = self.get_number_of_boids()

    def get_number_of_boids(self):
        num_x_pos = len(self.x_positions)
        num_y_pos = len(self.y_positions)
        num_x_vel = len(self.x_velocities)
        num_y_vel = len(self.y_velocities)

        numbers = [num_x_pos, num_y_pos, num_x_vel, num_y_vel]

        if any(num != num_x_pos for num in numbers):
            raise IndexError("length of arrays must match")
        return len(self.x_positions)


def update_boids(boids):
    formation_flying_distance = 10000
    formation_flying_strength = 0.125
    alert_distance = 100
    move_to_middle_strength = 0.01
    delta_t = 1

    x_positions, y_positions, x_velocities, y_velocities = boids.x_positions, boids.y_positions, boids.x_velocities, boids.y_velocities
    num_boids = boids.num_boids

    for i in range(num_boids):
        for j in range(num_boids):
            # Fly towards the middle
            x_position_difference = x_positions[j] - x_positions[i]
            y_position_difference = y_positions[j] - y_positions[i]

            x_velocities[i] += x_position_difference * move_to_middle_strength / num_boids
            y_velocities[i] += y_position_difference * move_to_middle_strength / num_boids

            # Fly away from nearby boids
            if x_position_difference ** 2 + y_position_difference ** 2 < alert_distance:
                x_velocities[i] -= x_position_difference
                y_velocities[i] -= y_position_difference

    for i in range(num_boids):
        for j in range(num_boids):
            # Try to match speed with nearby boids
            x_position_difference = x_positions[j] - x_positions[i]
            y_position_difference = y_positions[j] - y_positions[i]
            x_velocity_difference = x_velocities[j] - x_velocities[i]
            y_velocity_difference = y_velocities[j] - y_velocities[i]

            if x_position_difference ** 2 + y_position_difference ** 2 < formation_flying_distance:
                x_velocities[i] += x_velocity_difference * formation_flying_strength / num_boids
                y_velocities[i] += y_velocity_difference * formation_flying_strength / num_boids

    # Move according to velocities
    x_positions += x_velocities * delta_t
    y_positions += y_velocities * delta_t


def animate(frame):
    update_boids(boids)
    scatter.set_offsets(list(zip(boids.x_positions, boids.y_positions)))


if __name__ == "__main__":
    num_boids = 50
    x_limits = -450, 50
    y_limits = 300, 600
    x_velocity_limits = 0, 10
    y_velocity_limits = -20, 20
    axis_limits = -500, 1500

    boids_x = np.array([random.uniform(*x_limits) for x in range(num_boids)])
    boids_y = np.array([random.uniform(*y_limits) for x in range(num_boids)])
    boid_x_velocities = np.array([random.uniform(*x_velocity_limits) for x in range(num_boids)])
    boid_y_velocities = np.array([random.uniform(*y_velocity_limits) for x in range(num_boids)])
    boids = Boids(boids_x, boids_y, boid_x_velocities, boid_y_velocities)

    figure = plt.figure()
    axes = plt.axes(xlim=axis_limits, ylim=axis_limits)
    scatter = axes.scatter(boids.x_positions, boids.y_positions)

    anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)
    plt.show()
