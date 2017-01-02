from copy import deepcopy
import os
import numpy as np
import yaml
from numpy.testing import assert_array_almost_equal as array_assert
from badboids.badboids import update_boids


def create_boids_data():
    boids_x = np.arange(-450.0, 50.0, 50.0)
    boids_y = np.arange(-450.0, 50.0, 50.0)
    boids_x_velocities = np.arange(0.0, 10.0, 1.0)
    boids_y_velocities = np.arange(0.0, 40.0, 4.0)
    boids = (boids_x, boids_y, boids_x_velocities, boids_y_velocities)

    return boids


def create_badboids_regression_fixtures_file():
    '''add information'''
    boids = create_boids_data()

    before = deepcopy(boids)
    update_boids(boids)
    after = boids

    fixture = {"before": before, "after": after}
    fixture_file = open(os.path.join(os.path.dirname(__file__), 'fixtures', 'regression_badboids.yaml'), "w")
    fixture_file.write(yaml.dump(fixture))
    fixture_file.close()


def test_boids():

    # Arrange
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixtures', 'regression_badboids.yaml')))
    boid_data = regression_data["before"]
    boid_data_expected = regression_data["after"]

    # Act
    update_boids(boid_data)

    # Assert
    array_assert(boid_data_expected[0], boid_data[0], 6)
    array_assert(boid_data_expected[1], boid_data[1], 6)
    array_assert(boid_data_expected[2], boid_data[2], 6)
    array_assert(boid_data_expected[3], boid_data[3], 6)


if __name__ == "__main__":
    create_badboids_regression_fixtures_file()