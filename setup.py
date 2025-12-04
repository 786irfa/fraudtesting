"""
the setup.py file is an essential part of packaging and distributing python projects 
it is used by setuptools to define the 
configuration of your project such as metadata dependencies and more
"""
from setuptools import find_packages,setup
from typing import List
def get_requirements()->List[str]:
    """
    this function will return list of requiremenst 

    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt","r")as file:
            ##readlines from the file 
            lines=file.readlines()
            ##process each lines 
            for line in lines:
                requirement=line.strip()
                ##ignore empty lines and -e.
                if requirement and requirement!="-e .":
                 requirement_lst.append(requirement)
    except FileNotFoundError:
       print("requirements.txt file not found")
    return requirement_lst
print(get_requirements())
setup(
   name="Frauddetection",
   version="0.2",
   author="Irfan rana",
   author_email="if476771@gmail.com",
   packages=find_packages(),
   install_requires=get_requirements()
)

