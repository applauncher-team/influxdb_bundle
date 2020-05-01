from setuptools import setup, find_packages

with open('requirements.txt') as fp:
    install_requires = fp.read()

setup(
    name='influxdb_bundle',
    packages=find_packages(),
    version='1.0',
    description='Influxdb support for applauncher',
    author='Alvaro Garcia Gomez',
    author_email='maxpowel@gmail.com',
    url='https://github.com/applauncher-team/influxdb_bundle',
    download_url='https://github.com/applauncher-team/influxdb_bundle/archive/master.zip',
    keywords=['applauncher', 'influxdb'],
    classifiers=['Topic :: Adaptive Technologies', 'Topic :: Software Development', 'Topic :: System',
                 'Topic :: Utilities'],
    install_requires=install_requires
)