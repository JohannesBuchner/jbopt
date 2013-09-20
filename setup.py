from distutils.core import setup

setup(
    name='jbopt',
    version='0.1',
    author='Johannes Buchner',
    author_email='buchner.johannes@gmx.at',
    packages=['jbopt'],
    scripts=[],
    url='http://johannesbuchner.github.io/jbopt/',
    license='LICENSE.txt',
    description='Parameter space exploration toolbox',
    long_description=open('README.rst').read(),
    install_requires=[
        "scipy>=0.7.0",
    ],
)

