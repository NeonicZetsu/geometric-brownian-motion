from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="geometric-brownian-motion",
    version="0.1.0",
    author="NeonicZetsu",
    author_email="",  # Add your email if desired
    description="GBM implementation with Monte Carlo option pricing and live calibration from Yahoo Finance data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/geometric-brownian-motion",  # Update with your GitHub URL
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24",
        "scipy>=1.10",
        "matplotlib>=3.7",
        "pandas>=2.0",
        "yfinance>=0.2",
    ],
    extras_require={
        "dev": ["pytest", "jupyter"],
    },
)