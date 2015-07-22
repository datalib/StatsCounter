import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='statscounter',
    version='0.0.011',
    url='https://github.com/datalib/statscounter',
    license='MIT',
    description="Python's missing statistical Swiss Army knife",
    packages=['statscounter'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[],
    keywords='stats statistics statistic statistical measurements \
             mean average avg standard deviation std dev stddev \
             variance Counter StatsCounter collection measurement \
             measure count sum elements items',
    author='Rodrigo Palacios',
    author_email='rodrigopala91@gmail.com',
    scripts=[],
    package_data={},
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
)
