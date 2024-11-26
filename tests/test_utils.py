import pytest
import numpy as np
import cv2
from src.utils.image_processing import preprocess_image, resize_image
from src.utils.geometry import calculate_angle, order_points

class TestImageProcessing:
    def test_preprocess_image(self):
        image = np.ones((100, 100, 3), dtype=np.uint8) * 128
        processed = preprocess_image(image)
        assert processed.shape[:2] == (100, 100)
        assert len(processed.shape) == 2  # Should be grayscale
    
    def test_resize_image(self):
        image = np.ones((2000, 1000, 3), dtype=np.uint8)
        resized = resize_image(image, max_dimension=1200)
        assert max(resized.shape[:2]) == 1200

class TestGeometry:
    def test_calculate_angle(self):
        p1 = np.array([0, 0])
        p2 = np.array([0, 0])
        p3 = np.array([1, 1])
        angle = calculate_angle(p1, p2, p3)
        assert 0 <= angle <= 180
    
    def test_order_points(self):
        points = np.array([
            [100, 100],
            [200, 100],
            [200, 200],
            [100, 200]
        ])
        ordered = order_points(points)
        assert ordered.shape == (4, 2)