import numpy as np
import pytest
from numpy.testing import assert_array_almost_equal as array_assert
from badboids.badboids import Boids


def test_boids_init():
    """Tests Boids constructor"""

    # Arrange
    x_positions = np.array([1., 2., 3.])
    y_positions = np.array([3., 5., 7.])
    positions = np.vstack([x_positions, y_positions])

    x_velocities = np.array([10., 11., 12.])
    y_velocities = np.array([13., 14., 15.])
    velocities = np.vstack([x_velocities, y_velocities])

    # Act
    sut = Boids(positions, velocities)

    # Assert
    array_assert(sut.positions, positions)
    array_assert(sut.velocities, velocities)


def test_boids_init_with_incorrect_array_length():
    """Tests Boids constructor with incorrect array lengths"""
    # todo add this to a fixtures file
    # Arrange
    x_positions = np.array([1., 2., 3., 4.])
    y_positions = np.array([3., 5., 7.,5.])
    positions = np.vstack([x_positions, y_positions])

    x_velocities = np.array([10., 11., 12.])
    y_velocities = np.array([13., 14., 15.])
    velocities = np.vstack([x_velocities, y_velocities])

    # Act + Assert
    with pytest.raises(IndexError):
        Boids(positions, velocities)

