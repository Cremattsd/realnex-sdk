from setuptools import setup, find_packages

setup(
    name="real_nex_sync_api_data_facade",
    version="1.0.0",
    packages=find_packages(where="src"),  # Automatically discover the SDK's packages under the "src" directory
    package_dir={"": "src"},
    install_requires=[
        "requests",  # Add any dependencies your SDK needs
    ],
    python_requires='>=3.7',  # You can adjust this to match your Python version requirements
    author="Your Name",  # Replace with your name
    author_email="your.email@example.com",  # Replace with your email address
    description="A package to integrate RealNex CRM with other systems",
    long_description=open('README.md').read(),  # Make sure you have a README.md file for a detailed description
    long_description_content_type="text/markdown",  # This ensures that the README is rendered as markdown
    url="https://github.com/Cremattsd/realnex-sdk",  # Replace with your GitHub URL
    classifiers=[  # These classifiers help categorize your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Adjust license type as needed
        "Operating System :: OS Independent",
    ],
    include_package_data=True,  # If you have non-Python files (like templates, data, etc.), include them
)
