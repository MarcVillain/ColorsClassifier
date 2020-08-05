"""
Usage:
    python setup.py py2app
"""

from setuptools import setup, find_packages

APP = ["colorsclassifier/classify.py"]
DATA_FILES = []
OPTIONS = {"argv_emulation": True}

setup(
    name="colorsclassifier",
    version="1.0",
    author="Marc Villain",
    author_email="marc.villain@epita.fr",
    description="Simple script that lets you order images based on color.",
    url="https://github.com/MarcVillain/ColorsClassifier",
    packages=find_packages(),
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
    install_requires=[
        "colormath",
        "colorthief",
        "numpy",
        "opencv-python",
        "Pillow",
        "PyYAML",
    ],
    entry_points={
        "console_scripts": [
            "colorsclassifier=colorsclassifier.classify:main",
        ],
        "gui_scripts": [
            "colorsclassifier=colorsclassifier.classify:main",
        ]
    }
)
