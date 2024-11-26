import numpy as np
from typing import List, Dict
import cv2
from utils.logger import setup_logger

logger = setup_logger(__name__)

class SizeCalculator:
    """Calculator for determining real-world object dimensions."""
    
    def __init__(self, config: dict):
        """
        Initialize the size calculator.
        
        Args:
            config: Configuration dictionary containing measurement parameters
        """
        self.pixels_per_metric = None
        self.min_size = config['min_object_size']
        self.max_size = config['max_object_size']
        self.precision = config['precision']
    
    def calculate(self, objects: List[dict], reference: dict) -> List[dict]:
        """
        Calculate real dimensions of objects based on the reference object.
        
        Args:
            objects: List of detected objects
            reference: Reference object information
            
        Returns:
            List[dict]: List of objects with calculated dimensions
        """
        # Calculate scale based on reference object
        ref_width = reference['reference_size']
        ref_pixels = np.linalg.norm(
            reference['corners'][0] - reference['corners'][1]
        )
        self.pixels_per_metric = ref_width / ref_pixels
        
        logger.info(f"Scale: {self.pixels_per_metric:.4f} cm/pixel")
        
        measured_objects = []
        for obj in objects:
            # Calculate real dimensions
            corners = obj['corners']
            width_pixels = np.linalg.norm(corners[0] - corners[1])
            height_pixels = np.linalg.norm(corners[1] - corners[2])
            
            real_width = width_pixels * self.pixels_per_metric
            real_height = height_pixels * self.pixels_per_metric
            
            # Check if dimensions are within acceptable range
            if (self.min_size <= real_width <= self.max_size and
                self.min_size <= real_height <= self.max_size):
                measured_objects.append({
                    'corners': corners,
                    'width': round(real_width, self.precision),
                    'height': round(real_height, self.precision),
                    'area': round(real_width * real_height, self.precision)
                })
        
        logger.info(f"Calculated dimensions for {len(measured_objects)} objects")
        return measured_objects