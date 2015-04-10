from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='statscounter',
    version='0.0.0',
    url='https://github.com/rodricios/statscounter',
    license='MIT',
    description='The missing statistics-powered Python container',
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
    test_suite='nose.collector',
    tests_require=['nose'],
)
