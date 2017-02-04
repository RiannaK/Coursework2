from mock import patch

from badboids.boids import SimulationParametersLoader


@patch.object(SimulationParametersLoader, 'load_parameters_from_file')
def test_simulation_parameters_load_parameters(mock_load_from_file):
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

    sut = SimulationParametersLoader()

    # Act
    parameters = sut.load_parameters()

    # Assert
    assert parameters.formation_flying_distance == formation_flying_distance
    assert parameters.formation_flying_strength == formation_flying_strength
    assert parameters.alert_distance == alert_distance
    assert parameters.move_to_middle_strength == move_to_middle_strength
    assert parameters.delta_t == delta_t
