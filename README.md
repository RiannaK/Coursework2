Assignment 2: Bad Boids
========================

| Branch | Status | Coverage | 
| ------ | ------ | -------- |
| Master |[![Build Status](https://travis-ci.org/RiannaK/Coursework2.svg?branch=master)](https://travis-ci.org/RiannaK/Coursework2)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework2/badge.svg?branch=master)](https://coveralls.io/github/RiannaK/Coursework2?branch=master) |
| Develop |[![Build Status](https://travis-ci.org/RiannaK/Coursework2.svg?branch=develop)](https://travis-ci.org/RiannaK/Coursework2)| [![Coverage Status](https://coveralls.io/repos/github/RiannaK/Coursework2/badge.svg?branch=develop)](https://coveralls.io/github/RiannaK/Coursework2?branch=develop) |


###What does it do?

[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406) was a program designed by Craig Reynolds to simulate the aggregate motion of a flock, swarm, herd or schools of animals. Inspired by this, the Boids package aims to provide an animated output of this simulation of the behaviour of a flock of animals (such as flocks of starling’s seen on winter evenings in Rome) based on a range of input parameters.

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

Once installed, the user must specify the input parameters contained within a configuration (yaml) file.

There are input parameters:

Table of inputs required

Once the configuration file has been updated, the boids script can be called from the command line using the following syntax:


This assignment was completed as part of the UCL [MPHYG001: Research Software Engineering with Python course] (http://github-pages.ucl.ac.uk/rsd-engineeringcourse/).
