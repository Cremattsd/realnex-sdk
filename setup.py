from setuptools import setup, find_packages

setup(
    name="real_nex_sync_api_data_facade",
    version="1.0.0",
    packages=find_packages(where="src"),  # This finds all packages under 'src'
    package_dir={"": "src"},  # The src directory contains all packages
    install_requires=[
        "requests",  # Add any dependencies your SDK needs
    ],
)