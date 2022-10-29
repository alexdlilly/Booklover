from setuptools import setup, find_packages

setup(
    name='BookLover',
    version='1.0.0',
    url = 'https://github.com/alexdlilly/Booklover-DS5100-ADL.git',
    author = 'Alexander Lilly',
    author_email='kzr3fb@virginia.edu',
    description='Class for keeping a log of books read and their associated reviews',
    packages=find_packages(),
    install_requires=['pandas >= 1.3.4'],
)
    