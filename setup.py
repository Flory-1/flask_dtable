import re

from setuptools import setup

with open("src/flask_dtable/__init__.py", encoding="utf8") as f:
    version = re.search(r'__version__ = "(.*?)"', f.read()).group(1)

# Metadata goes in setup.cfg. These are here for GitHub's dependency graph.
setup(
    name='flask_dtable',
    version=version,
    install_requires=[
        "Flask"
    ],
    python_requires='>=3.6',
)