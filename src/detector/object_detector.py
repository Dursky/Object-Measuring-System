import cv2
import numpy as np
from typing import List, Dict
from utils.logger import setup_logger

logger = setup_logger(__name__)

class ObjectDetector:
    """Detector for objects to be measured."""
    
    def __init__(self, config: dict):
        """
        Initialize the object detector.
        
        Args:
            config: Configuration dictionary containing detector parameters
        """
        self.config = config
        self.confidence_threshold = config['confidence_threshold']
    
    def detect(self, image: np.ndarray) -> List[Dict]:
        """
        Detect objects to be measured in the image.
        
        Args:
            image: Input image in BGR format
            
        Returns:
            List[dict]: List of detected objects with their properties
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred,
                         self.config['edge_detection']['low_threshold'],
                         self.config['edge_detection']['high_threshold'])
        
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)
        
        objects = []
        for contour in contours:
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour,
                                    self.config['contour_approximation']['epsilon_factor'] * peri,
                                    True)
            
            if len(approx) >= 4:  # At least rectangular
                objects.append({
                    'corners': approx,
                    'contour': contour,
                    'area': cv2.contourArea(contour)
                })
        
        logger.info(f"Detected {len(objects)} measurable objects")
        return objects