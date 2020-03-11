# coding: utf-8
from setuptools import setup, find_packages

setup(
    name='django-geoposition-2',
    version=__import__('geoposition').__version__,
    description=
    'Django model field that can hold a geoposition, and corresponding admin widget.',
    author='Michael Verdegaal',
    author_email='michaelverdegaal@hotmail.nl',
    url='https://github.com/MichaelVerdegaal/django-geoposition',
    packages=find_packages(),
    zip_safe=False,
    package_data={
        'geoposition': [
            'locale/*/LC_MESSAGES/*',
            'templates/geoposition/widgets/*.html',
            'static/geoposition/*',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Framework :: Django',
    ])
