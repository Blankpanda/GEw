from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='gew',
    version='0.0.1',
    description='Old School RuneScape Grand Exchange wrapper',
    long_description=long_description,
    url='https://github.com/Blankpanda/GE_wrapper',
    author='Caleb Ellis',
    author_email='elliscaleb1998@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='api development',
    packages=find_packages(exclude=['examples', 'scripts']),
    install_requires=[''],
    data_files=[('gew/res/items.json')],

)
