import matplotlib
import numpy as np
from mock import patch, Mock

from badboids.boids import BoidsView


@patch.object(matplotlib.pyplot, 'figure')
@patch.object(matplotlib.pyplot, 'show')
def test_boids_voids_initialise_view(mock_show, mock_figure):
    """Tests Boids View initialise view method """

    # Arrange
    sut = BoidsView()
    positions = np.array([[1, 2, 3], [4, 5, 6]])

    # Act
    sut.initialise_view(positions)

    # Assert
    mock_figure.assert_called()
    mock_show.assert_called()


@patch.object(matplotlib.pyplot, 'figure')
def test_boids_voids_update_view(mock_figure):
    """Tests Boids View update view method """


    # Arrange
    sut = BoidsView()
    sut.scatter = Mock()
    positions = np.array([[1, 2, 3], [4, 5, 6]])

    # Act
    sut.update_view(positions)

    # Assert
    mock_figure.assert_called()

