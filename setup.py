import subprocess
import sys

import setuptools

if __name__ == '__main__':
    with open("README.md", "r") as fh:
        long_description = fh.read()

    setuptools.setup(
        name="jump",
        version='0.1.0',
        author="opper",
        author_email="",
        description=(
            "Utility that builds a 2-level menu based on applications and their available environments."
        ),
        long_description=long_description,
        long_description_content_type="text/markdown",
        url="https://github.com/opper/jump",
        packages=setuptools.find_packages(),
        classifiers=(
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        entry_points={
            'console_scripts': [
                'jump = jump.menu:main'
            ],
        },
        install_requires=['python-dotenv', 'pythondialog', 'requests'],
        include_package_data=True
    )