from setuptools import setup, find_packages

setup(
    name="real_nex_sync_api_data_facade",
    version="1.0.0",
    packages=find_packages(where="src"),  # Look for packages inside the 'src' folder
    package_dir={"": "src"},  # Ensure setuptools knows the root is inside 'src'
    install_requires=[
        "requests",  # Add any dependencies your SDK needs
    ],
)