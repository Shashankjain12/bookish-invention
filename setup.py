"""
This is ready to use library with many certain features of creating notes from active use of photos or any kind of pdf relted documents
"""

from setuptools import setup
REQUIRED_PKGS=[
        "tkinter",
        "pillow",
        "nltk",
        "numpy",
        "translate",
        "re",
        "PyPDF2",
        "pytesseract",
        "opencv-python",
        "pytest",
        ]
setup(
        name="bookish-invention",
        version="0.1b0",
        packages="bookishinvention",
        author="Shashank Jain",
        install_requires=REQUIRED_PKGS,
        )

