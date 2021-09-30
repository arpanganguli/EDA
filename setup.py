import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="EDA",
    version="0.1",
    author="Arpan Ganguli",
    author_email="arpan@alumni.lse.ac.uk",
    description="Automating the exploratory data analysis pipeline",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://gitlab/esip/prototype-rap/-/tree/eda_dev/EDA",
    project_urls={
        "Bug Tracker": "http://gitlab/esip/prototype-rap/-/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    package_data={'': ['templates/*', 'static/*']},
    python_requires=">=3.6",
)
