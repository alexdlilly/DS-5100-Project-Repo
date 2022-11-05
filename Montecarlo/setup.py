from setuptools import setup, find_packages

setup(
    name='montecarlo',
    version='1.0.0',
    url = 'https://github.com/alexdlilly/DS5100-2022-08-kzr3fb/tree/main/Montecarlo',
    author = 'Alexander Lilly',
    author_email='kzr3fb@virginia.edu',
    description='Module with a Die, Game, and Analyzer class for conducting montecarlo style simulations',
    packages=find_packages(),
    install_requires=['pandas >= 1.3.4', 'numpy >= 1.20.3'],
)