import cv2
import numpy as np
from typing import Optional, Dict
from utils.logger import setup_logger

logger = setup_logger(__name__)

class ReferenceDetector:
    """Detector for the reference object (10x10cm card)."""
    
    def __init__(self, config: dict):
        """
        Initialize the reference detector.
        
        Args:
            config: Configuration dictionary containing detector parameters
        """
        self.reference_size = config['size']
        self.min_area = config['min_area']
        self.max_area = config['max_area']
        self.edge_params = config.get('edge_detection', {
            'low_threshold': 50,
            'high_threshold': 150
        })
    
    def detect(self, image: np.ndarray) -> Optional[Dict]:
        """
        Detect the reference object in the image.
        
        Args:
            image: Input image in BGR format
            
        Returns:
            dict: Information about the detected reference object or None if not found
        """
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 
                         self.edge_params['low_threshold'],
                         self.edge_params['high_threshold'])
        
        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, 
                                     cv2.CHAIN_APPROX_SIMPLE)
        
        logger.debug(f"Found {len(contours)} contours in image")
        
        for contour in contours:
            area = cv2.contourArea(contour)
            if self.min_area < area < self.max_area:
                peri = cv2.arcLength(contour, True)
                approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
                
                if len(approx) == 4:
                    logger.info("Reference object detected")
                    return {
                        'corners': approx,
                        'center': np.mean(approx, axis=0)[0],
                        'area': area,
                        'reference_size': self.reference_size
                    }
        
        logger.warning("No reference object detected")
        return None