import pytest
import numpy as np
import cv2
from src.detector.reference_detector import ReferenceDetector
from src.detector.object_detector import ObjectDetector

def create_test_image():
    """Create a simple test image with a reference square."""
    image = np.zeros((500, 500, 3), dtype=np.uint8)
    # Draw reference square
    cv2.rectangle(image, (100, 100), (200, 200), (255, 255, 255), 2)
    # Draw test object
    cv2.rectangle(image, (300, 300), (400, 350), (255, 255, 255), 2)
    return image

class TestReferenceDetector:
    @pytest.fixture
    def detector(self):
        config = {
            'size': 10,
            'min_area': 1000,
            'max_area': 100000,
            'edge_detection': {
                'low_threshold': 50,
                'high_threshold': 150
            }
        }
        return ReferenceDetector(config)
    
    def test_reference_detection(self, detector):
        image = create_test_image()
        result = detector.detect(image)
        assert result is not None
        assert 'corners' in result
        assert result['corners'].shape == (4, 1, 2)
        assert 'reference_size' in result
        assert result['reference_size'] == 10

class TestObjectDetector:
    @pytest.fixture
    def detector(self):
        config = {
            'confidence_threshold': 0.7,
            'edge_detection': {
                'low_threshold': 50,
                'high_threshold': 150
            },
            'contour_approximation': {
                'epsilon_factor': 0.02
            }
        }
        return ObjectDetector(config)
    
    def test_object_detection(self, detector):
        image = create_test_image()
        objects = detector.detect(image)
        assert len(objects) > 0
        assert 'corners' in objects[0]
        assert 'contour' in objects[0]
        assert 'area' in objects[0]
