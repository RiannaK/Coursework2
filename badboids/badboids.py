"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

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


class BoidsBuilder:

    def __init__(self):

        self.num_boids = None
        self.x_limits = None
        self.y_limits = None
        self.x_velocity_limits = None
        self.y_velocity_limits = None

    def set_num_boids(self, num_boids):
        self.num_boids = num_boids

    def set_x_position_limits(self, x_limits):
        self.x_limits = x_limits

    def set_y_position_limits(self, y_limits):
        self.y_limits = y_limits

    def set_x_velocity_limits(self, x_velocity_limits):
        self.x_velocity_limits = x_velocity_limits

    def set_y_velocity_limits(self, y_velocity_limits):
        self.y_velocity_limits = y_velocity_limits

    def finish(self):
        self.validate()

        boids_x = np.array([random.uniform(*self.x_limits) for x in range(self.num_boids)])
        boids_y = np.array([random.uniform(*self.y_limits) for x in range(self.num_boids)])
        boid_x_velocities = np.array([random.uniform(*self.x_velocity_limits) for x in range(self.num_boids)])
        boid_y_velocities = np.array([random.uniform(*self.y_velocity_limits) for x in range(self.num_boids)])

        return Boids(boids_x, boids_y, boid_x_velocities, boid_y_velocities)

    def validate(self):
        pass


class Simulator:
    def __init__(self, boids):
        self.boids = boids
        self.scatter = None

    def update_boids(self):
        formation_flying_distance = 10000
        formation_flying_strength = 0.125
        alert_distance = 100
        move_to_middle_strength = 0.01
        delta_t = 1

        x_positions, y_positions, x_velocities, y_velocities = self.boids.x_positions, self.boids.y_positions, self.boids.x_velocities, self.boids.y_velocities
        num_boids = self.boids.num_boids

        # Fly towards the middle
        x_middle = np.mean(x_positions)
        y_middle = np.mean(y_positions)
        x_directions_to_middle = x_positions - x_middle
        y_directions_to_middle = y_positions - y_middle
        x_velocities -= x_directions_to_middle * move_to_middle_strength
        y_velocities -= y_directions_to_middle * move_to_middle_strength

        # Fly away from nearby boids
        xsep_matrix = x_positions[:, np.newaxis] - x_positions[np.newaxis, :]
        ysep_matrix = y_positions[:, np.newaxis] - y_positions[np.newaxis, :]

        square_distances = xsep_matrix * xsep_matrix + ysep_matrix * ysep_matrix
        close_birds = square_distances < alert_distance
        far_birds = np.logical_not(close_birds)
        x_separations_if_close = np.copy(xsep_matrix)
        y_separations_if_close = np.copy(ysep_matrix)
        x_separations_if_close[far_birds] = 0
        y_separations_if_close[far_birds] = 0
        x_velocities -= np.sum(x_separations_if_close, 0)
        y_velocities -= np.sum(y_separations_if_close, 0)

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

    def __animate(self, frame):
        self.update_boids()
        self.scatter.set_offsets(list(zip(boids.x_positions, boids.y_positions)))

    def run_simulation(self):

        axis_limits = -500, 1500
        figure = plt.figure()
        axes = plt.axes(xlim=axis_limits, ylim=axis_limits)
        self.scatter = axes.scatter(boids.x_positions, boids.y_positions)

        anim = animation.FuncAnimation(figure, self.__animate, frames=50, interval=50)
        plt.show()


if __name__ == "__main__":
    num_boids = 50
    x_limits = -450, 50
    y_limits = 300, 600
    x_velocity_limits = 0, 10
    y_velocity_limits = -20, 20

    builder = BoidsBuilder()
    builder.set_num_boids(num_boids)
    builder.set_x_position_limits(x_limits)
    builder.set_y_position_limits(y_limits)
    builder.set_x_velocity_limits(x_velocity_limits)
    builder.set_y_velocity_limits(y_velocity_limits)
    boids = builder.finish()

    simulator = Simulator(boids)  # todo add simulation_parameters
    simulator.run_simulation()
