# Standard setuptools

from setuptools import find_packages, setup


def readme():
    with open("README.md", encoding="utf-8") as f:
        README = f.read()
    return README


with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("requirements-optional.txt") as f:
    required_optional = f.read()

with open("requirements-test.txt") as f:
    required_test = f.read().splitlines()


extras_require = {
    # "analysis": required_optional.split("\n\n")[0].splitlines(),
    # "models": required_optional.split("\n\n")[1].splitlines(),
    # "tuners": required_optional.split("\n\n")[2].splitlines(),
    # "mlops": required_optional.split("\n\n")[3].splitlines(),
    # "parallel": required_optional.split("\n\n")[4].splitlines(),
    "test": required_test,
}

extras_require["full"] = (
    extras_require["test"]
    # + extras_require["models"]
    # + extras_require["tuners"]
    # + extras_require["mlops"]
    # + extras_require["parallel"]
)


setup(
    name="market_research",
    version="0.0.0",
    description="Open-source financial analysis in Python and Spark.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/mhall-simon/market-research",
    author="Matthew Hall",
    author_email="HallMJ@corning.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=["market_research*"]),
    include_package_data=True,
    install_requires=required,
    extras_require=extras_require,
    tests_require=required_test,
    python_requires=">=3.7",
)
