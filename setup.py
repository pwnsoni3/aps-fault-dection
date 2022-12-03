from  setuptools import find_packages, setup


REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list=requirement_file.readline()
    requirement_list=[requirement_name.replace("\n","") for requirement_name in requirement_list] 
    if HYPHEN_E_DOT in requirement_list:
        requirement_list.remove(HYPHEN_E_DOT)
    return requirement_list
    

setup(
    name="sensor",
    version="0.0.1",
    author="pawan_kumar_soni",
    author_email="pwnsoni3@gmail.com",
    package=find_package(),
    install_requires=get_requirements(),
)


