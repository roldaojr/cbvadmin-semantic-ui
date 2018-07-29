from setuptools import setup
from cbvadmin_semantic_ui import __version__

setup(
    name='cbvadmin-semantic-ui',
    version=__version__,
    description='Semantic UI template for CBVadmin',
    long_description=open('README.rst').read(),
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=['admin', 'django'],
    author='roldaojr',
    author_email='roldaogjr@gmail.com',
    url='https://github.com/roldaojr/cbvadmin-semantic-ui',
    license='LGPL',
    packages=['cbvadmin_semantic_ui'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3',
    install_requires=[
        'cbvadmin>=0.4.0',
        'crispy-semantic-ui>=1.0',
    ]
)
