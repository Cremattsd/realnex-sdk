from setuptools import setup, find_packages

setup(
    name="real_nex_sync_api_data_facade",
    version="1.0.0",
    packages=find_packages(where="src"),  # Look in the 'src' directory for packages
    package_dir={"": "src"},  # Tell setuptools the source is inside the 'src' folder
    install_requires=[
        "requests",  # Any dependencies your SDK needs
    ],
)