from mock import patch

from badboids.boids import BoidsParametersLoader


@patch.object(BoidsParametersLoader, 'load_parameters_from_file')
def test_boids_parameters_load_simulation_parameters(mock_load_from_file):
    """Tests Simulation Parameters loading method"""

    # Arrange
    formation_flying_distance = 10
    formation_flying_strength = 20
    alert_distance = 30
    move_to_middle_strength = 40
    delta_t = 3

    mock_load_from_file.return_value = {
        'formation_flying_distance': formation_flying_distance,
        'formation_flying_strength': formation_flying_strength,
        'alert_distance': alert_distance,
        'move_to_middle_strength': move_to_middle_strength,
        'delta_t': delta_t,
    }

    sut = BoidsParametersLoader()

    # Act
    parameters = sut.load_simulation_parameters()

    # Assert
    assert parameters.formation_flying_distance == formation_flying_distance
    assert parameters.formation_flying_strength == formation_flying_strength
    assert parameters.alert_distance == alert_distance
    assert parameters.move_to_middle_strength == move_to_middle_strength
    assert parameters.delta_t == delta_t



@patch.object(BoidsParametersLoader, 'load_parameters_from_file')
def test_boids_parameters_load_boids_setup_parameters(mock_load_from_file):
    """Tests Boids setup Parameters loading method"""

    # Arrange
    num_boids = 60
    x_limits = -420, 30
    y_limits = 100, 500
    x_velocity_limits = 1, 9
    y_velocity_limits = -23, 22

    mock_load_from_file.return_value = {
        'num_boids': num_boids,
        'x_limits': x_limits,
        'y_limits': y_limits,
        'x_velocity_limits': x_velocity_limits,
        'y_velocity_limits': y_velocity_limits,
    }

    sut = BoidsParametersLoader()

    # Act
    parameters = sut.load_boids_setup_parameters()

    # Assert
    assert parameters.num_boids == num_boids
    assert parameters.x_limits == x_limits
    assert parameters.y_limits == y_limits
    assert parameters.x_velocity_limits == x_velocity_limits
    assert parameters.y_velocity_limits == y_velocity_limits
