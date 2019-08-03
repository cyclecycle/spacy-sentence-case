import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spacy-sentence-case",
    version="0.0.1",
    author="Nicholas Morley",
    author_email="nick.morley111@gmail.com",
    description=" Convert sentences to sentence case.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cyclecycle/spacy-sentence-case",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
