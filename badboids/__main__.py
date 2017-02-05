import sys

from argparse import ArgumentParser

from badboids.boids import *


def main(args=''):
    parsed_arguments = parse_arguments(args)

    loader = BoidsParametersLoader(parsed_arguments.config)
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
    controller = BoidsController(model)
    controller.run_simulation()


def parse_arguments(args):
    # Create the argument parser.
    parser = ArgumentParser(
        description="Command line tool for simulating the behaviour of a flock of animals.")

    # Now we add the arguments.
    parser.add_argument('-c', '--config', type=str, default='',
                        help='the full path of the config file (.yaml) that specifies simulation parameters and setup. ' +
                             'If no file is specified, default parameters will be used.')

    # Parse the args
    return parser.parse_args(args=args)


if __name__ == "__main__":  # pragma: no cover
    main(sys.argv[1:])
