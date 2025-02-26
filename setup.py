from setuptools import setup, find_packages

setup(
    name="auto",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["watchdog"],
    entry_points={
        "console_scripts": [
            "auto = auto.main:main",
        ],
    },
)
