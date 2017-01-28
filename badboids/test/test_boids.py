import numpy as np
import pytest
from numpy.testing import assert_array_almost_equal as array_assert

from badboids.boids import Boids


def test_boids_init():
    """Tests Boids constructor"""

    # Arrange
    positions = np.array([[1., 2., 3.], [3., 5., 7.]])
    velocities = np.array([[10., 11., 12.], [13., 14., 15.]])

    # Act
    sut = Boids(positions, velocities)

    # Assert
    array_assert(sut.positions, positions)
    array_assert(sut.velocities, velocities)


def test_boids_init_with_incorrect_array_length():
    """Tests Boids constructor with incorrect array lengths"""

    # Arrange
    positions = np.array([[1., 2., 3., 4.], [3., 5., 7.,5.]])
    velocities = np.array([[10., 11., 12.], [13., 14., 15.]])

    # Act + Assert
    with pytest.raises(IndexError):
        Boids(positions, velocities)

