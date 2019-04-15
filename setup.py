import setuptools
from setuptools import find_packages

setuptools.setup(
    name="censys_command_line",
    version="1.0.1",
    author="Art Sturdevant",
    author_email="support@censys.io",
    description="Easily query the Censys API from the command line",
    install_requires=['censys'],
    packages=find_packages(),
    py_modules=['censys'],
    python_requires='>=2.7',
    scripts=['censys'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='censys threat hunting osint ports scan'
)
