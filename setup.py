import os
from distutils.core import setup

setup(
    name = "hippocampus",
    version = "0.1.0",
    url = 'http://github.com/threadsafelabs/hippocampus',
    license = 'BSD',
    description = "Object-level analytics for Django models",
    author = 'Jonathan Lukens',
    author_email = 'jonathan@threadsafelabs.com',
    packages = ['hippocampus', 'hippocampus.templatetags'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
