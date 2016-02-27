import os
import codecs

from setuptools import setup

import slackviewer


def read(filename):
    """Read and return `filename` in root dir of project and return string"""
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, filename), 'r').read()


install_requires = read("requirements.txt").split()
long_description = read('README.md')


setup(
    name="slackviewer",
    version=slackviewer.__version__,
    url='https://github.com/hfaran/slack-export-viewer',
    license='MIT License',
    author='Hamza Faran',
    description=('Slack Export Archive Viewer'),
    long_description=long_description,
    packages=["slackviewer"],
    install_requires = install_requires,
    entry_points={'console_scripts': [
        'slack-export-viewer = slackviewer.main:main'
    ]},
    include_package_data=True,
    # https://github.com/mitsuhiko/flask/issues/1562
    zip_safe=False
)