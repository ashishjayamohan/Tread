import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tread-ashishjayamohan",
    version="0.0.1",
    author="Ashish Jayamohan",
    author_email="ashishjayamohan@gmail.com",
    description="A tiny data science package.",
    long_description="Nothing here for right now",
    long_description_content_type="text/markdown",
    url="https://github.com/ashishjayamohan/Tread",
    packages=setuptools.find_packages("numpy", "matplotlib"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
