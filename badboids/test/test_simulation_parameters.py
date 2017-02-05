from numpy.testing import assert_array_almost_equal as array_assert

from badboids.boids import SimulationParameters


def test_simulation_parameters_init():
    """Tests Simulation Parameters constructor"""

    # Arrange
    formation_flying_distance = 800
    formation_flying_strength = 0.10
    alert_distance = 8
    move_to_middle_strength = 0.2
    delta_t = 1.5

    # Act
    sut = SimulationParameters(formation_flying_distance, formation_flying_strength, alert_distance,
                               move_to_middle_strength, delta_t)

    # Assert
    array_assert(sut.formation_flying_distance, formation_flying_distance)
    array_assert(sut.formation_flying_strength, formation_flying_strength)
    array_assert(sut.alert_distance, alert_distance)
    array_assert(sut.move_to_middle_strength, move_to_middle_strength)
    array_assert(sut.delta_t, delta_t)


def test_get_defaults():
    """Tests Simulation Parameters get defaults method"""

    # Arrange
    expected_formation_flying_distance = 10000
    expected_formation_flying_strength = 0.125
    expected_alert_distance = 100
    expected_move_to_middle_strength = 0.01
    expected_delta_t = 1.0

    # Act
    parameters = SimulationParameters.get_defaults()

    # Assert
    assert parameters.formation_flying_distance == expected_formation_flying_distance
    assert parameters.formation_flying_strength == expected_formation_flying_strength
    assert parameters.alert_distance == expected_alert_distance
    assert parameters.move_to_middle_strength == expected_move_to_middle_strength
    assert parameters.delta_t == expected_delta_t

