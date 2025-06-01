from setuptools import setup

setup(
    name="gccd-pune",
    version="1.0.0",
    py_modules=["gccd_pune"],
    entry_points={"console_scripts": ["gccd-pune=gccd_pune:main"]},
    description="Interactive CLI for Google Cloud Community Day Pune 2025",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Gitesh Mahadik",
    author_email="gmahadik8080@gmail.com",
    url="https://github.com/Gitesh08/gccd-pune",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["colorama>=0.4.6"],
)
