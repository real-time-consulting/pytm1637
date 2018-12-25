from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

def read(file_name):
    with open(os.path.join(here, file_name)) as f:
        text = f.read()

    return text

README = read('README.rst')
NEWS = read('NEWS.txt')


version = '1.0.0'

setup(name='pytm1637',
    version=version,
    description='Python Library for TM1637 LED driver.',
    long_description=README,
    classifiers=[
        # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: POSIX :: Linux',
    ],
    keywords='tm1637 seven segment led',
    author='Nenad Radulovic',
    author_email='nenad.b.radulovic@gmail.com',
    maintainer='Nenad Radulovic',
    maintainer_email='nenad.b.radulovic@gmail.com',
    url='https://gitlab.com/nradulovic',
    license='LGPL',
    packages=find_packages('src'),
    package_dir={'': 'src'}, include_package_data=True,
    zip_safe=False,
    install_requires=[
        # Currently no dependencies
    ],
    entry_points={
        'console_scripts':
            ['pyeds=main:main']
    }
)
