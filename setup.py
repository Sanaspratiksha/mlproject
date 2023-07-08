from setuptools import  find_packages,setup
from typing import List

HYPEN_E_DOT='e .'

def get_Requirements(file_path:str)->List[str]:
    '''
    this function will return the kist of requirement
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirement=file_obj.readlines()
        requirements=[req.replace("\n"," ")for req in requirements]


        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(

name='mlproject',
version='0.0.1',
author='pratiksha',
author_email='pratiksha28199@gmail.com',
packages=find_packages(),
install_required= get_Requirements('requirements.txt')

)


