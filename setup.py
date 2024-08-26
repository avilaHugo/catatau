from setuptools import find_packages, setup

setup(
    name="catatau",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # Runtime dependencies
    extras_require={
        "dev": [
            "pandas",  # Development dependencies (testing, linting, etc.)
        ],
    },
)
