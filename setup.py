from setuptools import setup, find_packages

setup(
    name='minutedb',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'filelock',
    ],
    test_suite='tests',
)
