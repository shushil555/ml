from setuptools import find_packages, setup

from typing import List 

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    '''
    this willl return list of requirements
    '''

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
name='ml',
version='0.0.1',
author='Shushil',
author_email='shushilpaudel2014@gmail.com',
packages=find_packages(),
install__requires=get_requirements('requirements.txt')


)