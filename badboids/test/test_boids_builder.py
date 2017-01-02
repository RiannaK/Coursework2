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
    # todo COME BACK TO THIS
    pass