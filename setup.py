from setuptools import setup, find_packages

try:
    with open("README.md", "r") as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = "RealNex SDK for syncing API data."

setup(
    name="real_nex_sync_api_data_facade",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
