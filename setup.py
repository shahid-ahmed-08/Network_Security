"""
The setup.py file is an essential part of packaging and distributing Python projects.
It is used by setuptools (or distutils in older Python versions) to define the configuration
of your project, such as its metadata, dependencies, and more.
"""
from setuptools import find_packages, setup
from typing import List


def get_requirements() -> List[str]:
    """
    Read requirements.txt and return a list of dependencies, stripping '-e .' if present.
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Shahid",
    author_email="shahid91309@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
)


if __name__ == "__main__":
    print(get_requirements())
