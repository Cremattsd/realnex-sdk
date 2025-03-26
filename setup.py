from setuptools import setup, find_packages

setup(
    name="real_nex_sync_api_data_facade",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",  # Add any dependencies your SDK needs
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="RealNex Sync API Data Facade",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Cremattsd/realnex-sdk",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)