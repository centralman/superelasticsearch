try:
    from setuptools import setup, find_packages
except ImportError:
    from distribute_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

__name__ = 'superelasticsearch'
__version__ = '0.4.4'
__author__ = 'Vaidik Kapoor'
__author_email__ = 'vaidik.kapoor@wingiify.com'

# read contents of a file
read_file = lambda x: open(x, 'r').read()

setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    description=('A super awesome extended version of the official '
                 'Elasticsearch Python client.'),
    long_description=read_file('README.md'),
    platforms=('Any',),
    packages=find_packages(exclude=['tests']),
    install_requires = [
        'elasticsearch',
    ],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock',
        'datadiff',
    ]
)
