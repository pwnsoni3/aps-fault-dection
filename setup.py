from  setuptools import find_packages, setup



def get_requirements():
    pass

setup(
    name="sensor",
    version="0.0.1",
    author="pawan_kumar_soni",
    author_email="pwnsoni3@gmail.com",
    package=find_package(),
    install_requires=get_requirements(),
)


