import setuptools
from setuptools import find_packages, setup
setup(
    name='wrapperclient',
    version='0.1.0',
    description='Made for OGC apis',
    author='Omm',
    license='MIT',
    long_description="A demo for OGC apis",
    long_description_content_type="text",
    packages=find_packages(exclude=["tests.*", "tests", "examples.*", "examples"]),
    install_requires=["requests"],
    python_requires=">=3.6",
)
