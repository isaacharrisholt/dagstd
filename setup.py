from setuptools import setup, find_packages

VERSION = '0.1.2'
DESCRIPTION = 'Dagstd'
with open('README.rst', 'r', encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="dagstd",
    version=VERSION,
    author="Isaac Harris-Holt",
    author_email="isaac@harris-holt.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    install_requires=[
        'dagster>=0.14.17',
    ],
    keywords=['dagster', 'data processing'],
    license='GNU GPLv3',
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
    python_requires='>=3.8',
)
