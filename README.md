# Object Measurement System

A computer vision system for measuring object dimensions using a reference card.

## Features

- Automatic reference object detection (10x10cm card)
- Multiple object measurement
- Perspective and geometric analysis
- Visual output with measurements

## Installation

```bash
python3 -m venv venv
source ./venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py --image path/to/image.jpg
```
