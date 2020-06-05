from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()



setup(
    name = 'simplehttp',
    version='0.0.1',
    license='MIT',
    long_description=readme,
    long_description_content_type="text/markdown",
    py_modules=["simplehttp"],
    package=find_packages()

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    # install_requires=[]

)