from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    with open('requirements.txt', 'r') as file:
        requirements = file.read().splitlines()

    if '-e .' in requirements:
        requirements.remove('-e .')
    return requirements

setup(
    name="src",
    version="0.0.1",
    author="Rajan ",
    author_email="r.devkota.98@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
