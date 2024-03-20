import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__="0.0.0"
REPO_NAME="textsummarizer-project"
SRC_REPO="textsummarizer"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    url="https://github.com/naltinyos/textsummarizer",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)


