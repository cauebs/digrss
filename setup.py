from setuptools import setup

VERSION = '1.0'
REQUIREMENTS = ['feedparser>=5.2.1']
MODULES = []

setup(
    name='digrss',
    version=VERSION,
    py_modules=['digrss'],
    install_requires=REQUIREMENTS,
    url='https://github.com/cauebs/digrss',
    download_url=('https://github.com/cauebs/digrss/archive/master.zip'),
    keywords=['feed', 'atom', 'rss'],
    maintainer='Cauê Baasch de Souza',
    maintainer_email='cauebaasch+pypi@gmail.com',
    description='simple feed polling'
)