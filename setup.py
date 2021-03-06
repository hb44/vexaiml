import os
from setuptools import find_packages, setup


# directory = os.path.abspath(os.path.dirname(__file__))
"""
with open(os.path.join(directory, 'README.rst')) as f:
    long_description = f.read()
"""

setup(
    name="vexaiml",
    version='0.0.1',
    description='Artifical Intelligence Markup Language'
    # long_description=long_description,
    url='https://github.com/benhoff/vexaiml',
    license='GPL3',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 2',
        'Operating System :: OS Independent'],
    keywords='artifical',
    author='Ben Hoff',
    author_email='beohoff@gmail.com',
    entry_points={'microphone.audioengines': ['pyaudio = microphone.audioengines.pyaudio_ae',
                                              'base = microphone.audioengine_plugin']},

    packages= find_packages(), # exclude=['docs', 'tests']
    install_requires=[
        'pluginmanager',
        'aiml'
        ],

    extras_require={
        'dev': ['flake8']
        },
)
