# coding: UTF-8
from setuptools import setup

setup(
    name = 'metrosp',
    version = '1.0.3.rc001',
    packages = ['metrosp'],
    author = 'Renato Lipi',
    author_email = '',
    description = 'Ferramenta de linha de comando para recuperar situação atual do Metro de SP',
    license = 'LGPLv3',
    keywords = 'metro metrosp SP',
    url = 'https://github.com/renatolipi/status_metro_sp',
    long_description_content_type="text/plain",
    long_description = 'Ferramenta de linha de comando para recuperar situação atual das linhas do Metro de SP. Para mais infos: https://github.com/renatolipi/status_metro_sp/blob/master/README.md',
    install_requires = ['beautifulsoup4==4.12.3', 'requests==2.32.3',],
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
)
