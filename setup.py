from setuptools import setup, find_packages


setup(
    name='weather',
    version='0.1',
    packages=find_packages(),
    description='Weather patterns',
    author='Snir Avrahami',
    author_email='10960141@uvu.edu',
    url='https://github.com/avrahsni/CS3270/',
    license = "MIT AND (Apache-2.0 OR BSD-2-Clause)",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)