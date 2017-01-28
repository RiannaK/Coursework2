import os
from copy import deepcopy
import numpy as np
import yaml
from numpy.testing import assert_array_almost_equal as array_assert

from badboids.boids import Simulator, Boids, SimulationParameters


def create_boids_data():
    boids_x = np.arange(-45.0, 5.0, 5.0)
    boids_y = np.arange(0.0, 10.0, 1.0)
    positions = np.vstack([boids_x, boids_y])

    boids_x_velocities = np.arange(0.0, 10.0, 1.0)
    boids_y_velocities = np.arange(0.0, 40.0, 4.0)
    velocities = np.vstack([boids_x_velocities, boids_y_velocities])

    boids = Boids(positions, velocities)

    return boids


def create_badboids_regression_fixtures_file():
    """Creates a fixtures file with before and after data of a single boids update iteration"""
    boids = create_boids_data()
    simulation_parameters = SimulationParameters.get_defaults()
    simulator = Simulator(boids, simulation_parameters)

    before = deepcopy(boids)
    simulator.update_boids()
    after = boids

    fixture = {"before": before, "after": after}
    fixture_file = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'regression_badboids.yaml'), "w")
    fixture_file.write(yaml.dump(fixture))
    fixture_file.close()


def test_boids():

    # Arrange
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures', 'regression_badboids.yaml')))
    boids = create_boids_data()
    boid_data_expected = regression_data["after"]
    simulation_parameters = SimulationParameters.get_defaults()
    sut = Simulator(boids, simulation_parameters)

    # Act
    sut.update_boids()

    # Assert
    array_assert(boid_data_expected.positions, boids.positions, 6)
    array_assert(boid_data_expected.velocities, boids.velocities, 6)


if __name__ == "__main__":
    create_badboids_regression_fixtures_file()
