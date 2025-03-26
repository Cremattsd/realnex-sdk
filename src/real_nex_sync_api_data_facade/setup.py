from setuptools import setup, find_packages

setup(
    name="real_nex_sync_api_data_facade",
    version="1.0.0",
    packages=find_packages(where="src/real_nex_sync_api_data_facade"),  # This should point to the correct directory
    package_dir={"": "src/real_nex_sync_api_data_facade"},  # Make sure it points to the correct path
    install_requires=[
        "requests",  # Add any dependencies your SDK needs
    ],
)