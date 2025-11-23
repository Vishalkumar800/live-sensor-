from setuptools import setup,find_packages
from typing import List

#.\.venv\Scripts\activate

def get_requirements() -> List[str]:
    
    requirements_list : List[str] = []
    return requirements_list
    

setup(
    name='sensor_analysis',
    version='0.0.1',
    author='Vishal',
    packages=find_packages(),
    install_requires = get_requirements(), #['pymongo']
)