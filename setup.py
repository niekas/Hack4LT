#! coding: utf-8
from setuptools import find_packages
from setuptools import setup


setup(
    name = 'Hack4LT',
    version = '0.1',
    url = 'http://Hack4.LT',
    license = 'BSD',
    description = 'Lithuanian Python community website for events, lectures, hacking, knowledge sharing and more.',
    maintainer = u'niekas',
    maintainer_email = 'albertas.gimbutas@mii.vu.lt',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[]
)
