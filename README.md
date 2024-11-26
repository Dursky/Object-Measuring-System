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
pip install -e .
pip install -r requirements.txt
```

## Usage

```bash
python src/main.py --image path/to/image.jpg
```

# Quick Start Guide - Object Measurement System

## 1. Virtual Environment

```bash
# Activate virtual environment
source ./venv/bin/activate   # Linux/Mac
# or
venv\Scripts\activate      # Windows
```

## 2. Running Tests

```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_detector.py

# Run tests with detailed output
pytest -v tests/

# Run tests with print statements
pytest -s tests/
```

## 3. Running the System

```bash
# Basic usage
python3 src/main.py --image data/examples/your_image.jpg

# With custom config
python3 src/main.py --image data/examples/your_image.jpg --config config/config.yaml --output data/output/
```

## 4. Configuration Parameters

### Quick Parameter Adjustment (config/config.yaml)

```yaml
reference:
  size: 10 # Reference card size in cm
  min_area: 1000 # Minimum pixel area for reference detection
  max_area: 100000 # Maximum pixel area for reference detection

detection:
  confidence_threshold: 0.7 # Detection confidence threshold
  min_object_size: 20 # Minimum object size in pixels

measurement:
  precision: 2 # Decimal places in measurements
```

## 5. Example Usage

### Step 1: Prepare Reference Image

- Place a 10x10cm reference card in the scene
- Ensure good lighting and contrast
- Take photo with the reference card clearly visible

### Step 2: Run Analysis

```bash
# Example with sample image
python src/main.py --image data/examples/room_photo.jpg
```

### Step 3: Check Results

```bash
# Results are saved in:
data/output/result.jpg  # Annotated image
```

## 6. Common Issues & Solutions

### Poor Detection

```yaml
# Adjust in config/config.yaml
detection:
  edge_detection:
    low_threshold: 30 # Lower for better edge detection
    high_threshold: 100
```

### Inaccurate Measurements

```yaml
reference:
  size: 10 # Ensure this matches your reference card
  min_area: 500 # Try lowering if reference not detected
```

## 7. Development Tasks

### Adding Test Images

```bash
# Add test images to
data/examples/

# Add reference patterns to
data/reference/
```

### Modifying Visualization

```yaml
# In config/config.yaml
visualization:
  colors:
    reference: [0, 255, 0] # Green
    object: [0, 0, 255] # Red
  text:
    font_scale: 0.8
```

## 8. Sample Commands

```bash
# Test run with debugging
python src/main.py --image data/examples/test.jpg --debug

# Process multiple images
for img in data/examples/*.jpg; do
    python src/main.py --image "$img"
done

# Run with custom output directory
python src/main.py --image test.jpg --output custom_results/
```

## 9. Tips

- Use a white or high-contrast reference card
- Keep the reference card flat and unobstructed
- Ensure consistent lighting
- Keep the camera relatively stable
- Photos should be at least 1080p resolution for best results

## 10. Performance Optimization

```yaml
# Adjust in config/config.yaml for faster processing
detection:
  max_objects: 10 # Limit number of objects
  min_object_size: 50 # Increase to ignore small objects
```

# Author: Michał Durski
