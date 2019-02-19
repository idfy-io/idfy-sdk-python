import setuptools

from idfy_sdk.version import version

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="idfy_sdk",
    version=version,
    author="Idfy",
    author_email="support@idfy.io",
    description="SDK for using the Idfy API in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Signereno/Python-SDK",
    #package_dir={'':'./src'},
    #packages=['idfy_sdk'],
    packages=setuptools.find_packages(exclude=['test', 'test.*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Requests',
        'six',  # Remove this dependancy.
    ],

)