from setuptools import find_packages, setup
setup(
    name='ExtensibleAPIClient',
    version='0.1.0',
    description='Made for OGC apis',
    author='Omm',
    license='MIT',
    
    packages=find_packages(),
    install_requires=["argparser", "requests"],
    python_requires=">=3.6",
    entry_points={"console_scripts": ["genApi=src.cli"]},
)
