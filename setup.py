import setuptools
import glob

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="<PROJECT>",
    version="0.0.1",
    author="Daniel Jörgens",
    author_email="djoerch@gmail.com",
    description="Analysis of <...>.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/djoerch/<PROJECT>",
    packages=setuptools.find_packages("src"),
    package_data={
        "": ["*.yml"],
    },
    package_dir={"": "src"},
    install_requires=[],
    scripts=glob.glob("scripts/*.py"),
)
