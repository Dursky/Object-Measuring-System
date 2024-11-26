import numpy as np
import cv2
from typing import Tuple
from utils.logger import setup_logger

logger = setup_logger(__name__)

class PerspectiveAnalyzer:
    """Analyzer for perspective distortion in images."""
    
    def __init__(self):
        """Initialize the perspective analyzer."""
        pass
    
    def correct_perspective(self, image: np.ndarray, corners: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Correct perspective distortion in the image.
        
        Args:
            image: Input image
            corners: Corner points of the reference object
            
        Returns:
            Tuple containing the corrected image and transformation matrix
        """
        # Get dimensions
        height, width = image.shape[:2]
        
        # Define destination points for perspective transform
        dst_points = np.array([
            [0, 0],
            [width - 1, 0],
            [width - 1, height - 1],
            [0, height - 1]
        ], dtype=np.float32)
        
        # Calculate perspective transform
        matrix = cv2.getPerspectiveTransform(corners.astype(np.float32), dst_points)
        corrected = cv2.warpPerspective(image, matrix, (width, height))
        
        logger.info("Perspective correction applied")
        return corrected, matrix