from badboids.boids import BoidsBuilder, Simulator

if __name__ == "__main__":

    num_boids = 50
    x_limits = -450, 50
    y_limits = 300, 600
    x_velocity_limits = 0, 10
    y_velocity_limits = -20, 20

    builder = BoidsBuilder()
    builder.set_num_boids(num_boids)
    builder.set_x_position_limits(x_limits)
    builder.set_y_position_limits(y_limits)
    builder.set_x_velocity_limits(x_velocity_limits)
    builder.set_y_velocity_limits(y_velocity_limits)
    boids = builder.finish()

    simulator = Simulator(boids)  # todo add simulation_parameters = config file
    simulator.run_simulation()