import matplotlib
from matplotlib import animation
from mock import MagicMock
from mock import patch

from badboids.boids import BoidsController, BoidsView


@patch.object(matplotlib.animation, 'FuncAnimation')
@patch.object(matplotlib.pyplot, 'figure')
@patch.object(BoidsView, 'initialise_view')
@patch.object(BoidsView, 'update_view')
def test_boids_controller_run_simulation(mock_update_view, mock_initialise_view, mock_figure, mock_func_animation):
    """Tests Boids run simulation method"""

    def check_func_animation_callback(figure, animation_callback, **kwargs):
        animation_callback(0)
        return None

    # Arrange
    model = MagicMock()
    sut = BoidsController(model)

    mock_func_animation.side_effect = check_func_animation_callback

    # Act
    sut.run_simulation()

    # Assert
    mock_func_animation.assert_called()
    mock_initialise_view.assert_called()
    mock_update_view.assert_called()
