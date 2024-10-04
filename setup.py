from setuptools import setup, find_packages

setup(
    name="sw_assignments",
    version="1.0",
    packages=["modul_1", "modul_2"],  # Explicitly list your packages
    package_dir={
        "modul_1": "assignment1/src/modul_1",
        "modul_2": "assignment2/src/modul_2",
    },
    description="Two assignments with separate modules",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Maryam Abdollahi",
    author_email="mariam.abdollahi@gmail.com",
)
