import pytest

from badboids.boids import BoidsBuilder


def test_boids_builder_set_num_boids():
    """Tests BuilderBoids set_num_boids method"""

    # Arrange
    num_boids = 40
    sut = BoidsBuilder()

    # Act
    sut.set_num_boids(num_boids)

    # Assert
    assert sut.num_boids == num_boids


def test_boids_builder_set_x_position_limits():
    """Tests BuilderBoids set_x_position_limits method"""

    # Arrange
    x_limits = -20, 220
    sut = BoidsBuilder()

    # Act
    sut.set_x_position_limits(x_limits)

    # Assert
    assert sut.x_limits == x_limits


def test_boids_builder_set_y_position_limits():
    """Tests BuilderBoids set_y_position_limits method"""

    # Arrange
    y_limits = -180, 60
    sut = BoidsBuilder()

    # Act
    sut.set_y_position_limits(y_limits)

    # Assert
    assert sut.y_limits == y_limits


def test_boids_builder_set_x_velocity_limits():
    """Tests BuilderBoids set_x_velocity_limits method"""

    # Arrange
    x_velocity_limits = -15, 45
    sut = BoidsBuilder()

    # Act
    sut.set_x_velocity_limits(x_velocity_limits)

    # Assert
    assert sut.x_velocity_limits == x_velocity_limits


def test_boids_builder_set_y_velocity_limits():
    """Tests BuilderBoids set_y_velocity_limits method"""

    # Arrange
    y_velocity_limits = 0, 60
    sut = BoidsBuilder()

    # Act
    sut.set_y_velocity_limits(y_velocity_limits)

    # Assert
    assert sut.y_velocity_limits == y_velocity_limits


def test_boids_builder_finish():
    """Tests BuilderBoids finish method"""

    # Arrange
    num_boids = 50
    x_limits = -20, 220
    y_limits = -180, 60
    x_velocity_limits = -15, 45
    y_velocity_limits = 0, 60

    sut = BoidsBuilder()
    sut.set_num_boids(num_boids)
    sut.set_x_position_limits(x_limits)
    sut.set_y_position_limits(y_limits)
    sut.set_x_velocity_limits(x_velocity_limits)
    sut.set_y_velocity_limits(y_velocity_limits)

    # Act
    boids = sut.finish()

    # Assert
    assert boids.positions.shape == (2, 50)
    assert boids.velocities.shape == (2, 50)


def test_boids_builder_finish_with_missing_parameters_throws():
    """Tests BuilderBoids finish method with missing parameters"""

    # Arrange
    num_boids = 50
    x_limits = -20, 220
    y_limits = -180, 60
    x_velocity_limits = -15, 45
    y_velocity_limits = 0, 60

    for missing_case in range(5):
        sut = BoidsBuilder()

        if missing_case != 0:
            sut.set_num_boids(num_boids)
        if missing_case != 1:
            sut.set_x_position_limits(x_limits)
        if missing_case != 2:
            sut.set_y_position_limits(y_limits)
        if missing_case != 3:
            sut.set_x_velocity_limits(x_velocity_limits)
        if missing_case != 4:
            sut.set_y_velocity_limits(y_velocity_limits)

        # Act + Assert
        with pytest.raises(AssertionError):
            sut.finish()
