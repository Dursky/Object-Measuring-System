import cv2
import numpy as np
from typing import List, Dict
from utils.logger import setup_logger

logger = setup_logger(__name__)

def visualize_results(image: np.ndarray, measurements: List[Dict], config: Dict) -> np.ndarray:
    """
    Visualize measurement results on the image.
    
    Args:
        image: Original image
        measurements: List of objects with their measurements
        config: Visualization configuration
        
    Returns:
        np.ndarray: Image with visualized measurements
    """
    result = image.copy()
    
    for obj in measurements:
        # Draw object contour
        corners = obj['corners'].reshape((-1, 1, 2)).astype(np.int32)
        cv2.polylines(result, [corners], True,
                     config['colors']['object'],
                     config['text']['thickness'])
        
        # Add dimensions text
        center = np.mean(corners, axis=0)[0].astype(int)
        text = f"{obj['width']}x{obj['height']}cm"
        cv2.putText(result, text, tuple(center),
                   cv2.FONT_HERSHEY_SIMPLEX,
                   config['text']['font_scale'],
                   config['text']['color'],
                   config['text']['thickness'])
    
    logger.info("Visualization generated")
    return result