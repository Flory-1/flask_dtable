import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("src/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

setuptools.setup(
    name='flask_dtable',
    version=version,
    author='Florian Lämmlein',
    author_email='florian.leammlein@gmail.com',
    description="Creates and returns an HTML table",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/Flory-1/flask_dtable',
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: flask_dtable",
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[

    ],
    python_requires='>=3.6',
)