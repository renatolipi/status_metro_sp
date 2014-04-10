# coding: UTF-8
from setuptools import setup

setup(
    name = 'metrosp',
    version = '0.1.0',
    packages = ['metrosp'],
    author = 'Renato Lipi',
    author_email = '',
    description = 'Ferramenta de linha de comando para recuperar situação atual do Metro de SP',
    license = 'LGPLv3',
    keywords = 'metro metrosp SP',
    url = 'https://github.com/renatolipi/status_metro_sp',
    long_description = 'Ferramenta de linha de comando para recuperar situação atual das linhas do Metro de SP. Para mais infos: https://github.com/renatolipi/status_metro_sp/blob/master/README.md',
    install_requires = ['beautifulsoup4 >= 4.3.2', 'httplib2 == 0.7.4'],
)
