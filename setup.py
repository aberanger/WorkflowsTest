from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="workflows_test",
    version="0.0.1",
    description="Test d'utilisation de workflows github avec python",
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/aberanger/WorkflowsTest",
    author="Anna Béranger",
    author_email="anbberanger@gmail.com",
    keywords="workflows",
    license="MIT",
    packages=["hello"],
    install_requires=[],
    include_package_data=True,
)