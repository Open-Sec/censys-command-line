import setuptools
from setuptools import find_packages

from os import path

current_dir = path.abspath(path.dirname(__file__))

with open(path.join(current_dir, 'README.md'), encoding='utf-8') as f:
    long_desc = f.read()

setuptools.setup(
    name="censys_command_line",
    version="1.0.3",
    author="Art Sturdevant",
    author_email="support@censys.io",
    description="Command-line tool for Censys! Quickly investigate suspicious hosts or answer complex questions about your infrastructure using Censys right from the command-line! https://www.censys.io",
    long_description=long_desc,
    long_description_content_type='text/markdown',
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
