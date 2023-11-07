"""Setup will allow to create ml project as package"""

from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' #auto trigger setup.py ie indication to build setup.py file
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='FlightPricePrediction',
version='0.0.1',
author='saks0106',
author_email='sakshemgotekar@gmail.com',
packages=find_packages(), #in src it will search for __init__ and install it
install_requires=get_requirements('requirements.txt')

)