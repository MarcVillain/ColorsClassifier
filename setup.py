"""
Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ["classify.py"]
DATA_FILES = []
OPTIONS = {}

setup(
    name="Colors Classifier",
    version="1.0",
    author="Marc Villain",
    author_email="marc.villain@epita.fr",
    description="Simple script that lets you order images based on color.",
    url="https://github.com/MarcVillain/ColorClassifier",
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
