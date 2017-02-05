Assignment 2: Bad Boids
========================

| Branch | Status | Coverage | 
| ------ | ------ | -------- |
| Master |[![Build Status](https://travis-ci.org/RiannaK/Coursework2.svg?branch=master)](https://travis-ci.org/RiannaK/Coursework2)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework2/badge.svg?branch=master)](https://coveralls.io/github/RiannaK/Coursework2?branch=master) |
| Develop |[![Build Status](https://travis-ci.org/RiannaK/Coursework2.svg?branch=develop)](https://travis-ci.org/RiannaK/Coursework2)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework2/badge.svg?branch=develop)](https://coveralls.io/github/RiannaK/Coursework2?branch=develop) |


###What does it do?

[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406) was a program designed by Craig Reynolds to simulate the aggregate motion of a flock, swarm, herd or schools of animals. Inspired by this, the Bad Boids package provides an animated output of the simulated behaviour of a flock of animals based on a range of input parameters.

###How to Install

There are two options to install the package: manually download and install, or install directly from GitHub using the standard pip command.

Downloading from GitHub?
 
 * Download the package as a zip file from GitHub
 * From the command line, install using the following command:
	- For Windows users ```python setup.py install```
	- For Mac and Linux ```sudo python setup.py install```
 
Installing directly from GitHub?
 
 * Type ```pip install git+git://github.com/RiannaK/Coursework2.git``` into the terminal


###How to Use

Once installed, the user can chose to run boids using the default settings.

``` badboids ```

If desired, the user can specify their own simulation parameters and setup parameters within a configuration (.yaml) file.

In this case, the boids script can be called from the command line using the following syntax:

``` badboids --config "insert\full\file\path\to\config.yaml" ``` 

####Boid setup parameters

| Parameter         | Default  | Description | 
| ----------------- | -------- | ----------- |
| num_boids         | 50       | Number of boids                                               |
| x_limits          |[-450, 50]| Bounds on the initial x position for randomly generated boids |
| y_limits          |[300, 600]| Bounds on the initial y position for randomly generated boids |
| x_velocity_limits |[0, 10]   | Bounds on the initial x velocity for randomly generated boids |
| y_velocity_limits |[-20, 20] | Bounds on the initial y velocity for randomly generated boids |

####Simulation parameters

| Parameter                 | Default  | Description | 
| ------------------------- | -------- | ----------- |
| formation_flying_distance |10000     | Cutoff separation below which the speed of nearby boids will be matched |
| formation_flying_strength |0.125     | Controls how greatly the speed is matched |
| alert_distance            |100       | Defines how close boids can be before trying to fly away  |
| move_to_middle_strength   |0.01      | Strength with which boids move towards the middle         |
| delta_t                   |1.0       | Time resolution for simulation (abitrary units)           |

An example configuration (.yaml) file can be seen below:

```
boids_setup_parameters:
- num_boids: 50
  x_limits: [-450, 50]
  y_limits: [300, 600]
  x_velocity_limits: [0, 10]
  y_velocity_limits: [-20, 20]

simulation_parameter_defaults:
- formation_flying_distance: 10000
  formation_flying_strength: 0.125
  alert_distance: 100
  move_to_middle_strength: 0.01
  delta_t: 1.0
```

This assignment was completed as part of the UCL [MPHYG001: Research Software Engineering with Python course] (http://github-pages.ucl.ac.uk/rsd-engineeringcourse/).
