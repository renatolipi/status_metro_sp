# coding: UTF-8
from setuptools import setup

setup(
    name='metrosp',
    version='0.2.1',
    packages=['metrosp'],
    author='Renato Lipi',
    author_email='',
    description='Ferramenta de linha de comando para recuperar situação atual do Metro de SP',
    license='LGPLv3',
    keywords='metro metrosp SP',
    url='https://github.com/renatolipi/status_metro_sp',
    long_description=open('README.md').read(),
    install_requires=['beautifulsoup4 == 4.6.0', 'requests==2.18.4'],
)
