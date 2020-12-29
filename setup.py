import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yaml-config-reader",
    version="0.9",
    author="J4CK VVH173",
    author_email="i78901234567890@gmail.com",
    description="Package for reading configs from yml files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/J4CKVVH173/yaml-config-reader",
    packages=setuptools.find_packages(),
    install_requires=[
            'PyYAML==5.3.1',
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.6',
)
