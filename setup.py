import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colorprint3",
    version="1.2a1",
    author="trunghieumickey",
    author_email="trunghieumickey@outlook.com.vn",
    description="A simple library to print with color and style on Python 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/trunghieumickey/colorprint3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
    ],
    python_requires='>=3.8',
)
