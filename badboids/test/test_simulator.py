import pytest
import numpy as np

from badboids.badboids import Boids, Simulator
from numpy.testing import assert_array_almost_equal as array_assert

def test_simulator_fly_towards_middle():
    """Tests Simulator 'fly towards middle' method"""

    # Arrange
    x_positions = np.array([1., 2., 3.])
    y_positions = np.array([3., 5., 7.])
    x_velocities = np.array([10., 11., 12.])
    y_velocities = np.array([13., 14., 15.])

    expected_x_positions = np.array([1., 2., 3.])
    expected_y_positions = np.array([3., 5., 7.])
    expected_x_velocities = np.array([10.01, 11., 11.99])
    expected_y_velocities = np.array([13.02, 14., 14.98]) # todo add to fixtures file

    boids = Boids(x_positions, y_positions, x_velocities, y_velocities)
    sut = Simulator(boids)


    # Act
    sut.fly_towards_middle()

    # Assert
    array_assert(sut.boids.x_positions, expected_x_positions, 6)
    array_assert(sut.boids.y_positions, expected_y_positions, 6)
    array_assert(sut.boids.x_velocities, expected_x_velocities, 6)
    array_assert(sut.boids.y_velocities, expected_y_velocities, 6)

