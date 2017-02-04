import numpy as np
import pytest
from numpy.testing import assert_array_almost_equal as array_assert

from badboids.boids import SimulationParameters, BoidsSetupParameters


def test_boids_setup_parameters_init():
    """Tests Boids Setup Parameters Parameters constructor"""

    # Arrange
    num_boids = 50
    x_limits = -450, 50
    y_limits = 300, 600
    x_velocity_limits = 0, 10
    y_velocity_limits = -20, 20

    # Act
    sut = BoidsSetupParameters(num_boids, x_limits, y_limits, x_velocity_limits, y_velocity_limits)

    # Assert
    array_assert(sut.num_boids, num_boids)
    array_assert(sut.x_limits, x_limits)
    array_assert(sut.y_limits, y_limits)
    array_assert(sut.x_velocity_limits, x_velocity_limits)
    array_assert(sut.y_velocity_limits, y_velocity_limits)


def test_get_defaults():
    """Tests Boids Setup Parameters get defaults method"""

    # Arrange
    num_boids = 50
    x_limits = -450, 50
    y_limits = 300, 600
    x_velocity_limits = 0, 10
    y_velocity_limits = -20, 20

    # Act
    parameters = BoidsSetupParameters.get_defaults()

    # Assert
    assert parameters.num_boids == num_boids
    assert parameters.x_limits == x_limits
    assert parameters.y_limits == y_limits
    assert parameters.x_velocity_limits == x_velocity_limits
    assert parameters.y_velocity_limits == y_velocity_limits
