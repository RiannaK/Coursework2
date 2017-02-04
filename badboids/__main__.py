import sys

from badboids.boids import *


def main(args=None):
    """The main routine."""
    if args is None:
        args = sys.argv[1:]

    loader = BoidsParametersLoader()
    simulation_parameters = loader.load_simulation_parameters()
    setup_parameters = loader.load_boids_setup_parameters()

    builder = BoidsBuilder()
    builder.set_num_boids(setup_parameters.num_boids)
    builder.set_x_position_limits(setup_parameters.x_limits)
    builder.set_y_position_limits(setup_parameters.y_limits)
    builder.set_x_velocity_limits(setup_parameters.x_velocity_limits)
    builder.set_y_velocity_limits(setup_parameters.y_velocity_limits)
    boids = builder.finish()

    model = SimulatorModel(boids, simulation_parameters)
    view = BoidsView()
    controller = BoidsController(model, view)
    controller.run_simulation()


if __name__ == "__main__":  # pragma: no cover
    main()
