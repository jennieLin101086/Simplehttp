from setuptools import setup, find_packages

with open("README.rst", "r") as readme_file:
    readme = readme_file.read()



setup(
    name = 'jennie-simplerequest',
    version='0.0.1',
    license='MIT',
    long_description=readme,
    package=find_packages(),
    # install_requires=open('requirements.txt').readlines()

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=[]

)