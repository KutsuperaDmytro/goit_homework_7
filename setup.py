from setuptools import setup, find_packages

setup(
    name="Folder",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "clean-folder = Folder.clean:main"
        ]
    },
)