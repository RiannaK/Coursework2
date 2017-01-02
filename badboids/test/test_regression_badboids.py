import os
from copy import deepcopy
import numpy as np
import yaml
from numpy.testing import assert_array_almost_equal as array_assert

from badboids.badboids import Simulator, Boids


def create_boids_data():
    boids_x = np.arange(-45.0, 5.0, 5.0)
    boids_y = np.arange(0.0, 10.0, 1.0)
    boids_x_velocities = np.arange(0.0, 10.0, 1.0)
    boids_y_velocities = np.arange(0.0, 40.0, 4.0)
    boids = Boids(boids_x, boids_y, boids_x_velocities, boids_y_velocities)

    return boids


def create_badboids_regression_fixtures_file():
    """Creates a fixtures file with before and after data of a single boids update iteration"""
    boids = create_boids_data()
    simulator = Simulator(boids)

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
    boids = regression_data["before"]
    boid_data_expected = regression_data["after"]
    sut = Simulator(boids)

    # Act
    sut.update_boids()

    # Assert
    array_assert(boid_data_expected.x_positions, boids.x_positions, 6)
    array_assert(boid_data_expected.y_positions, boids.y_positions, 6)
    array_assert(boid_data_expected.x_velocities, boids.x_velocities, 6)
    array_assert(boid_data_expected.y_velocities, boids.y_velocities, 6)


if __name__ == "__main__":
    create_badboids_regression_fixtures_file()
