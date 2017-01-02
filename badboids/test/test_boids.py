import pytest

from badboids.badboids import Boids


def test_boids_init():
    """Tests Boids constructor"""

    # Arrange
    x_positions = [1, 2, 3]
    y_positions = [4, 5, 6]
    x_velocities = [10, 11, 12]
    y_velocities = [13, 14, 15]

    # Act
    sut = Boids(x_positions, y_positions, x_velocities, y_velocities)

    # Assert
    assert sut.x_positions == x_positions
    assert sut.y_positions == y_positions
    assert sut.x_velocities == x_velocities
    assert sut.y_velocities == y_velocities


def test_boids_init_with_incorrect_array_length():
    """Tests Boids constructor with incorrect array lengths"""
    # todo add this to a fixtures file
    # Arrange
    x_positions = [1, 2, 3, 4]
    y_positions = [4, 5, 6]
    x_velocities = [10, 11, 12]
    y_velocities = [13, 14, 15]

    # Act + Assert
    with pytest.raises(IndexError):
        Boids(x_positions, y_positions, x_velocities, y_velocities)

