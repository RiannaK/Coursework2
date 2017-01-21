"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt


class Boids:

    def __init__(self, positions, velocities):
        self.positions = positions
        self.velocities = velocities
        self.num_boids = self.get_number_of_boids()

    def get_number_of_boids(self):

        if self.positions.shape != self.velocities.shape:
            raise IndexError("matrix dimensions must match")

        return self.positions.shape[1]


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

        lower_positions = np.array([self.x_limits[0], self.y_limits[0]])
        upper_positions = np.array([self.x_limits[1], self.y_limits[1]])

        lower_velocities = np.array([self.x_velocity_limits[0], self.y_velocity_limits[0]])
        upper_velocities = np.array([self.x_velocity_limits[1], self.y_velocity_limits[1]])

        positions = self.make_random_array(lower_positions, upper_positions)
        velocities = self.make_random_array(lower_velocities, upper_velocities)

        return Boids(positions, velocities)

    def make_random_array(self, lower_limits, upper_limits):
        width = upper_limits - lower_limits
        return lower_limits[:, np.newaxis] + (np.random.rand(2, self.num_boids) * width[:, np.newaxis])

    def validate(self):
        pass


class Simulator:
    def __init__(self, boids):
        self.boids = boids
        self.scatter = None

    def update_boids(self):
        self.fly_towards_middle()
        self.fly_away_from_nearby_boids()
        self.match_speed_of_nearby_boids()
        self.update_positions()

    def fly_towards_middle(self):
        move_to_middle_strength = 0.01

        middle = np.mean(self.boids.positions, 1)
        directions_to_middle = self.boids.positions - middle[:, np.newaxis]
        self.boids.velocities -= directions_to_middle * move_to_middle_strength

    def fly_away_from_nearby_boids(self):
        alert_distance = 100

        # Broadcast positions into matrices of separations
        sep_matrix = self.boids.positions[:, np.newaxis, :] - self.boids.positions[:, :, np.newaxis]
        square_displacements = sep_matrix * sep_matrix
        square_distances = np.sum(square_displacements, 0)

        close_birds = square_distances < alert_distance
        far_birds = np.logical_not(close_birds)

        # use logical masking to ignore far away birds
        separations_if_close = np.copy(sep_matrix)
        separations_if_close[0, :, :][far_birds] = 0
        separations_if_close[1, :, :][far_birds] = 0

        self.boids.velocities += np.sum(separations_if_close, 1)

    def match_speed_of_nearby_boids(self):
        formation_flying_distance = 10000
        formation_flying_strength = 0.125

        # Broadcast positions into matrices of separations
        sep_matrix = self.boids.positions[:, np.newaxis, :] - self.boids.positions[:, :, np.newaxis]
        square_displacements = sep_matrix * sep_matrix
        square_distances = np.sum(square_displacements, 0)

        # Broadcast velocities into matrices of velocity differences
        vel_difference_matrix = self.boids.velocities[:, np.newaxis, :] - self.boids.velocities[:, :, np.newaxis]

        very_far_birds = square_distances >= formation_flying_distance

        # use logical masking to ignore far away birds
        velocity_differences_if_close = np.copy(vel_difference_matrix)
        velocity_differences_if_close[0, :, :][very_far_birds] = 0
        velocity_differences_if_close[1,:,:][very_far_birds] = 0

        self.boids.velocities += np.mean(velocity_differences_if_close, 2) * formation_flying_strength

    def update_positions(self):
        delta_t = 1
        self.boids.positions += self.boids.velocities * delta_t

    def __animate(self, frame):
        self.update_boids()
        self.scatter.set_offsets(self.boids.positions.transpose())

    def run_simulation(self):

        axis_limits = -500, 1500
        figure = plt.figure()
        axes = plt.axes(xlim=axis_limits, ylim=axis_limits)
        self.scatter = axes.scatter(self.boids.positions[0, :], self.boids.positions[1, :])

        anim = animation.FuncAnimation(figure, self.__animate, frames=50, interval=50)
        plt.show()


