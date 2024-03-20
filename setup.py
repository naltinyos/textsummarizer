import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__="0.0.0"
REPO_NAME="textsummarizer-project"
AUTHOR_USER_NAME = "nyos"
SRC_REPO="textsummarizer"
AUTHOR_EMAIL = "nd"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL,
    description = "nlp",
    long_description=long_description,
    long_description_content="text/markdown",
    url="https://github.com/naltinyos/textsummarizer",
    project_urls={
        "Bug tracker": "https://github.com/naltinyos/textsummarizer/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


