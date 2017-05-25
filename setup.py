# coding=utf-8

from setuptools import setup, find_packages


setup(
    name='nameshark-vcard',
    version='1.0.0',
    packages=find_packages(exclude=['tests', ]),
    url='https://github.com/proinsias/nameshark-vcard',
    license='MIT',
    author="Francis O'Donovan",
    author_email='francis.odonovan@gmail.com',
    description='Converts vcards to the json format expected by the Name Shark app',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
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
