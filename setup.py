from setuptools import setup, find_packages

# ✅ Safe fallback: avoid crashing if README.md is missing on Render
def load_readme():
    try:
        with open("README.md", "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        return "RealNex SDK for syncing data with RealNex API."

setup(
    name="real_nex_sync_api_data_facade",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    long_description=load_readme(),
    long_description_content_type="text/markdown",
    author="Your Name",
    description="SDK for integrating with RealNex API",
)
