import matplotlib
from mock import patch

from badboids.__main__ import main as entry
from badboids.boids import *


@patch.object(BoidsController, 'run_simulation')
@patch.object(matplotlib.pyplot, 'figure')
@patch.object(BoidsParametersLoader, 'load_simulation_parameters')
@patch.object(BoidsParametersLoader, 'load_boids_setup_parameters')
def test_main(mock_boids_setup_loader, mock_simulation_parameters_loader, mock_figure, mock_run_simulation):
    """Tests entry method"""

    # Arrange
    mock_boids_setup_loader.return_value = BoidsSetupParameters.get_defaults()
    mock_simulation_parameters_loader.return_value = SimulationParameters.get_defaults()

    # Act
    entry()

    # Assert
    mock_boids_setup_loader.assert_called_once()
    mock_simulation_parameters_loader.assert_called_once()
    mock_figure.assert_called_once()
    mock_run_simulation.assert_called_once()
