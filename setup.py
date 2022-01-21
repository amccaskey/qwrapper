import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qwrapper",
    version="0.0.4",
    author="kouhei nakaji",
    author_email="nakajijiji@gmail.com",
    description="You can receive the message 'Hello!!!'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/konakaji/qwrapper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "qiskit~=0.29.1",
        "Qulacs~=0.3.0"
    ],
    python_requires='>=3.7',
)
