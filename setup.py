#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name="badboids",
    version="0.1.0",
    description="boids provides an animated output of the simulated behaviour of a flock of animals",
    author="Rianna Kelly",
    author_email="rianna.kelly.16@ucl.ac.uk",
    packages=find_packages(exclude=["*test"]),
    package_data={"badboids": ["*.yaml"]},
    include_package_data=True,
    test_suite="pytest",
    tests_require=["mock", "pytest", "yaml"],
    scripts=["scripts/boids"],
    entry_points=dict(console_scripts=["badboids = badboids.__main__:main"]),
    install_requires=["argparse", "matplotlib", "numpy"]
)
