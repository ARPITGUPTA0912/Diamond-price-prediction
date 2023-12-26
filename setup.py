from setuptools import find_packages, setup
from typing import List
hyphen_e_dot ='-e .'


def requirement(filepath: str)-> List[str]:
    required=[]
    with open(filepath) as fileobj:
        required=fileobj.readlines()
        [req.replace("\n", " ") for req in required]
        
        if hyphen_e_dot in required:
            required.remove(hyphen_e_dot)

        
    return required
    

setup(
    name= "Diamond price",
    version="0.0.1",
    author='Arpit Gupta',
    author_email='arpitgupta7690@gmail.com',
    packages = find_packages(),
    install_requires= requirement('requirement.txt')
    # same as name
)