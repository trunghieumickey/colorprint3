import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorprint3", # Replace with your own username
    version="1.0.0",
    author="trunghieumickey",
    author_email="trunghieumickey@outlook.com.vn",
    description="Print color in Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trunghieumickey/colorprint3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
