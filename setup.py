from setuptools import setup, find_packages

setup(
    name="object-measurement",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "opencv-python>=4.5.3",
        "pyyaml>=5.4.1",
        "tensorflow>=2.6.0",
        "matplotlib>=3.4.3",
        "scikit-image>=0.18.3",
    ],
    author="Michał Durski",
    description="A system for measuring object dimensions using reference-based computer vision",
)