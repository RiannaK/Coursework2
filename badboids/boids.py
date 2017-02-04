"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

import numpy as np
import yaml
import os
from matplotlib import animation
from matplotlib import pyplot as plt


class SimulationParameters:
    def __init__(self, formation_flying_distance, formation_flying_strength, alert_distance, move_to_middle_strength,
                 delta_t):
        self.delta_t = delta_t
        self.move_to_middle_strength = move_to_middle_strength
        self.alert_distance = alert_distance
        self.formation_flying_strength = formation_flying_strength
        self.formation_flying_distance = formation_flying_distance

    @staticmethod
    def get_defaults():
        delta_t = 1
        move_to_middle_strength = 0.01
        alert_distance = 100
        formation_flying_strength = 0.125
        formation_flying_distance = 10000

        return SimulationParameters(formation_flying_distance, formation_flying_strength, alert_distance,
                                    move_to_middle_strength, delta_t)


class SimulationParametersLoader:

    def load_parameters(self):
        raw_parameters = self.load_parameters_from_file()

        formation_flying_distance = raw_parameters.pop('formation_flying_distance')
        formation_flying_strength = raw_parameters.pop('formation_flying_strength')
        alert_distance = raw_parameters.pop('alert_distance')
        move_to_middle_strength = raw_parameters.pop('move_to_middle_strength')
        delta_t = raw_parameters.pop('delta_t')

        return SimulationParameters(formation_flying_distance, formation_flying_strength, alert_distance,
                                    move_to_middle_strength, delta_t)

    def load_parameters_from_file(self):  # pragma: no cover
        with open(os.path.join(os.path.dirname(__file__), 'config.yaml')) as parameters_file:
            return yaml.load(parameters_file)['defaults'][0]


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
    def __init__(self, boids, simulation_parameters):
        self.boids = boids
        self.scatter = None
        self.parameters = simulation_parameters

    def update_boids(self):
        self.fly_towards_middle()
        self.fly_away_from_nearby_boids()
        self.match_speed_of_nearby_boids()
        self.update_positions()

    def fly_towards_middle(self):
        middle = np.mean(self.boids.positions, 1)
        directions_to_middle = self.boids.positions - middle[:, np.newaxis]
        self.boids.velocities -= directions_to_middle * self.parameters.move_to_middle_strength

    def fly_away_from_nearby_boids(self):
        # Broadcast positions into matrices of separations
        sep_matrix = self.boids.positions[:, np.newaxis, :] - self.boids.positions[:, :, np.newaxis]
        square_displacements = sep_matrix * sep_matrix
        square_distances = np.sum(square_displacements, 0)

        close_birds = square_distances < self.parameters.alert_distance
        far_birds = np.logical_not(close_birds)

        # use logical masking to ignore far away birds
        separations_if_close = np.copy(sep_matrix)
        separations_if_close[0, :, :][far_birds] = 0
        separations_if_close[1, :, :][far_birds] = 0

        self.boids.velocities += np.sum(separations_if_close, 1)

    def match_speed_of_nearby_boids(self):
        # Broadcast positions into matrices of separations
        sep_matrix = self.boids.positions[:, np.newaxis, :] - self.boids.positions[:, :, np.newaxis]
        square_displacements = sep_matrix * sep_matrix
        square_distances = np.sum(square_displacements, 0)

        # Broadcast velocities into matrices of velocity differences
        vel_difference_matrix = self.boids.velocities[:, np.newaxis, :] - self.boids.velocities[:, :, np.newaxis]

        very_far_birds = square_distances >= self.parameters.formation_flying_distance

        # use logical masking to ignore far away birds
        velocity_differences_if_close = np.copy(vel_difference_matrix)
        velocity_differences_if_close[0, :, :][very_far_birds] = 0
        velocity_differences_if_close[1, :, :][very_far_birds] = 0

        self.boids.velocities += np.mean(velocity_differences_if_close, 2) * self.parameters.formation_flying_strength

    def update_positions(self):
        self.boids.positions += self.boids.velocities * self.parameters.delta_t


class BoidsController:
    def __init__(self, boids_model, boids_view):
        self.boids_model = boids_model
        self.boids_view = boids_view

    def run_simulation(self):
        anim = animation.FuncAnimation(self.boids_view.figure, self.__animate, frames=50, interval=50)
        self.boids_view.initialise_view(self.boids_model.boids.positions)

    def __animate(self, frame):
        self.boids_model.update_boids()
        self.boids_view.update_view(self.boids_model.boids.positions)


class BoidsView:
    def __init__(self):
        self.scatter = None
        self.figure = plt.figure()

    def initialise_view(self, positions):
        axis_limits = -500, 1500
        axes = plt.axes(xlim=axis_limits, ylim=axis_limits)
        self.scatter = axes.scatter(positions[0, :], positions[1, :])
        plt.show()

    def update_view(self, positions):
        self.scatter.set_offsets(positions.transpose())
