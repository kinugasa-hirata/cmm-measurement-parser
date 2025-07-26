from setuptools import setup

# Read the README file for long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cmm-measurement-parser",
    version="1.0.0",
    author="shuhei",
    author_email="kinugasa.hirata@gmail.com",
    description="Professional CMM measurement data parser for coordinate measuring machines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shuhei-kinugasa/cmm-measurement-parser",  # Change 'shuhei-kinugasa' to your actual GitHub username
    py_modules=["cmm_measurement_parser"],
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Quality Control",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.0.0",
        "numpy>=1.18.0",
        "openpyxl>=3.0.0",
    ],
    keywords="cmm, measurement, coordinate, measuring, machine, quality, control, metrology, japanese, calypso",
    project_urls={
        "Bug Reports": "https://github.com/shuhei-kinugasa/cmm-measurement-parser/issues",
        "Source": "https://github.com/shuhei-kinugasa/cmm-measurement-parser/",
        "Documentation": "https://github.com/shuhei-kinugasa/cmm-measurement-parser/blob/main/README.md",
    },
)