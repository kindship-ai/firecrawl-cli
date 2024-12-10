from setuptools import setup, find_packages

setup(
    name="firecrawl-cli",
    description="A CLI tool for FireCrawl - Convert websites to markdown with ease",
    version="0.1",
    author="Martin Källström",
    packages=find_packages(),
    install_requires=[
        "click>=8.1.7",
        "firecrawl-py>=1.0.0",
        "pydantic>=2.0.0",
    ],
    entry_points={"console_scripts": ["firecrawl = pycli.cli:cli"]},
)
