import codecs
import os

from setuptools import find_packages, setup

setup(
    name="housing_data_package",
    version="0.0.1",
    author="Sai Ram",
    description="House Price prediction",
    author_email="sairam.kancharla@tigeranalytics.com",
    packages=find_packages(where="src"),
    install_requires=[
        "requests",
        'importlib-metadata; python_version == "3.8"',
    ],
    package_dir={"": "src"},
)
