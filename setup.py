# /home/harish/intern/factentry_hlib/setup.py

from setuptools import setup, find_packages

setup(
    name="factentry_hlib",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        'pytesseract',
        'pymupdf',
        'langdetect',
        'pandas',
        'pillow',
        'icecream',
        # Add any other dependencies here
    ],
    entry_points={},
)
