from setuptools import setup


setup(
    name='csv2jsonl',
    version='0.1.1',
    description='Converts a CSV file to JSONLines.',
    long_description=open('README.rst', 'rt', encoding='utf-8').read(),
    url='https://github.com/jruere/csv2jsonl',
    license="LGPLv3",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords="jsonlines csv",
    author="Javier Ruere",
    author_email="javier@ruere.com.ar",
    zip_safe=True,
    scripts=[
        'csv2jsonl.py',
    ],
    install_requires=[
        "jsonlines~=1.2.0",
    ],
)
