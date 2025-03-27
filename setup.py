from setuptools import setup, find_packages
import os

# ✅ Safe fallback for missing README.md (for Render or any build environment)
try:
    with open("README.md", "r", encoding="utf-8") as f:
        long_description = f.read()
except Exception:
    long_description = "RealNex SDK for API integration."

setup(
    name="real_nex_sync_api_data_facade",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    description="SDK for integrating with RealNex API",
)
