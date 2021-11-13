#!/usr/bin/env python
import setuptools

try:
    with open('README.md', 'r', encoding='utf-8') as fh:
        long_description = fh.read()
except (IOError, OSError):
    long_description = ''

setuptools.setup(
    name='xontrib-default-command',
    version='0.0.3',
    license='MIT',
    author='mattmc3',
    author_email='ohmyxonsh@gmail.com',
    description="Run a default command when you press return on an empty command line.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    install_requires=['xonsh'],
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
    platforms='any',
    url='https://github.com/oh-my-xonsh/xontrib-default-command',
    project_urls={
        "Documentation": "https://github.com/oh-my-xonsh/xontrib-default-command/blob/main/README.md",
        "Code": "https://github.com/oh-my-xonsh/xontrib-default-command",
        "Issue tracker": "https://github.com/oh-my-xonsh/xontrib-default-command/issues",
    },
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Unix Shell",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: System :: Shells",
        "Topic :: System :: System Shells",
        "Topic :: Terminals",
    ]
)
