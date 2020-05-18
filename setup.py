from setuptools import setup

_locals = {}
exec(open("baseemoji/_version.py").read(), None, _locals)
version = _locals["__version__"]
long_description = open("README.rst").read()

setup(
    name="base-emoji",
    version=_locals["__version__"],
    author="Ali Moallim",
    author_email="amoallim15@gmail.com",
    url="https://github.com/amoallim15/base-emoji",
    packages=["baseemoji"],
    description=(
        "A binary-to-emoji encoding scheme that represent"
        "binary data in a subset of the Unicode Emoji symbols."
    ),
    long_description=long_description,
    keywords="base emoji encode decode scheme",
    python_requires=">= 3.5",
    entry_points={"console_scripts": ["baseemoji = baseemoji.__main__:main"]},
    license="MIT",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
    ],
)
