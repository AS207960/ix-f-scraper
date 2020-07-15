#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'networktoolkit']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Alfie Foster",
    author_email='bonzi@as207960.net',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
    ],
    description="IX-F Scraper",
    entry_points={
        'console_scripts': [
            'ix_f_scraper=ix_f_scraper.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='ix_f_scraper',
    name='ix_f_scraper',
    packages=find_packages(include=['ix_f_scraper', 'ix_f_scraper.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/as207960/ix-f-scraper',
    version='0.0.3',
    zip_safe=False,
)
