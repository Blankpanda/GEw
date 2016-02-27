from setuptools import setup, find_packages
from codecs import open
from os import path



setup(
    name='gew',
    version='0.0.17',
    description='Old School RuneScape Grand Exchange wrapper',
    long_description='',
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
    include_package_data=True,
    install_requires=[''],
    package_data={'gew' : ['items.json']},
    data_files=['gew/items.json']
)
