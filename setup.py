
from setuptools import setup, find_packages

with open("version", "r") as file:
    version = file.read(5)

setup(
    name="written_book_exporter",
    version=version,
    description="Exports all written books from a Minecraft World",
    author="TheRedstoneer",
    packages=["written_book_exporter"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
