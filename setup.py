# The MIT License (MIT)
#
# Copyright (c) 2016 Francis T. O'Donovan
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# coding=utf-8

"""Setup script."""
import os
from setuptools import setup, find_packages

DESCRIPTION = 'Converts vcards to the json format expected by the Name Shark app.'
if os.path.exists('README.rst'):
    LONG_DESCRIPTION = open('README.rst').read()
else:
    LONG_DESCRIPTION = DESCRIPTION

setup(
    name='nameshark-vcard',
    use_scm_version=True,
    packages=find_packages(exclude=['tests', ]),
    setup_requires=['setuptools_scm', ],
    url='https://github.com/proinsias/nameshark-vcard',
    license='MIT',
    author="Francis O'Donovan",
    author_email='francis.odonovan@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        ],
    install_requires=[
        'probablepeople',
        'vobject',
        ],
    )
