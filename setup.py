from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function reads the 'requirements.txt' file and returns a list of dependencies.
    Each line in the file should contain a package name.
    """
    requirements = []

    # Open the requirements.txt file and read all the lines
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()

    # Remove any extra newline characters
    requirements = [req.replace('\n', "") for req in requirements]

    # Correct indentation
    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

# Setup function for the package
setup(
    name='mlProjects',  # Name of your project
    version='0.0.1',  # Version of your project
    author='raunak',  # Author of the project
    author_email='raunakdwivedi2303@gmail.com',  # Author's email
    packages=find_packages(),  # This will automatically find all packages in the project
    install_requires=get_requirements('requirements.txt')  # List of dependencies from requirements.txt
)
