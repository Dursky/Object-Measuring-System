# Object Measurement System

A computer vision system for measuring object dimensions using a reference card.

## Features

- Automatic reference object detection (10x10cm card)
- Multiple object measurement
- Perspective and geometric analysis
- Visual output with measurements

## Installation

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py --image path/to/image.jpg
```

# requirements.txt

numpy>=1.21.0
opencv-python>=4.5.3
pyyaml>=5.4.1
tensorflow>=2.6.0
pytest>=6.2.5
matplotlib>=3.4.3
scikit-image>=0.18.3

# setup.py

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
author="Michal Durski",
description="A system for measuring object dimensions using reference-based computer vision",
)

# .gitignore

venv/
**pycache**/
_.pyc
.pytest_cache/
_.log
data/output/\*
