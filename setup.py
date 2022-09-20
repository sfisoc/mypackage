from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1.1.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package by sfiso',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/sfisoc/mypackage',
    author='Sifiso',
    author_email='gammer4live@gmail.com'
)