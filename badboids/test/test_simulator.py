import numpy as np
import yaml
import os
from numpy.testing import assert_array_almost_equal as array_assert

from badboids.boids import Boids, Simulator


def test_simulator_fly_towards_middle():
    """Tests Simulator 'fly towards middle' method"""

    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_simulator_fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_simulator_fly_towards_middle']

    for fixture in fixtures:
        # Arrange
        positions = np.array(fixture.pop('positions'))
        velocities = np.array(fixture.pop('velocities'))

        expected_positions = np.array(fixture.pop('expected_positions'))
        expected_velocities = np.array(fixture.pop('expected_velocities'))

        boids = Boids(positions, velocities)
        sut = Simulator(boids)

        # Act
        sut.fly_towards_middle()

        # Assert
        array_assert(sut.boids.positions, expected_positions, 6)
        array_assert(sut.boids.velocities, expected_velocities, 6)



def test_simulator_fly_away_from_nearby_boids():
    """Tests Simulator 'fly_away_from_nearby_boids' method"""
    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_simulator_fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_simulator_fly_away_from_nearby_boids']

    for fixture in fixtures:
        # Arrange
        positions = np.array(fixture.pop('positions'))
        velocities = np.array(fixture.pop('velocities'))

        expected_positions = np.array(fixture.pop('expected_positions'))
        expected_velocities = np.array(fixture.pop('expected_velocities'))

        boids = Boids(positions, velocities)
        sut = Simulator(boids)

        # Act
        sut.fly_away_from_nearby_boids()

        # Assert
        array_assert(sut.boids.positions, expected_positions, 6)
        array_assert(sut.boids.velocities, expected_velocities, 6)

def test_simulator_match_speed_of_nearby_boids():
    """Tests Simulator 'match_speed_of_nearby_boids' method"""

    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_simulator_fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_simulator_match_speed_of_nearby_boids']

    for fixture in fixtures:
        # Arrange
        positions = np.array(fixture.pop('positions'))
        velocities = np.array(fixture.pop('velocities'))

        expected_positions = np.array(fixture.pop('expected_positions'))
        expected_velocities = np.array(fixture.pop('expected_velocities'))

        boids = Boids(positions, velocities)
        sut = Simulator(boids)

        # Act
        sut.match_speed_of_nearby_boids()

        # Assert
        array_assert(sut.boids.positions, expected_positions, 6)
        array_assert(sut.boids.velocities, expected_velocities, 6)


def test_simulator_update_velocities():
    """Tests Simulator 'fly_away_from_nearby_boids' method"""

    with open(os.path.join(os.path.dirname(__file__), 'fixtures', 'test_simulator_fixtures.yaml')) as fixtures_file:
        fixtures = yaml.load(fixtures_file)['test_simulator_update_velocities']

    for fixture in fixtures:
        # Arrange
        positions = np.array(fixture.pop('positions'))
        velocities = np.array(fixture.pop('velocities'))

        expected_positions = np.array(fixture.pop('expected_positions'))
        expected_velocities = np.array(fixture.pop('expected_velocities'))

        boids = Boids(positions, velocities)
        sut = Simulator(boids)

        # Act
        sut.update_positions()

        # Assert
        array_assert(sut.boids.positions, expected_positions, 6)
        array_assert(sut.boids.velocities, expected_velocities, 6)
