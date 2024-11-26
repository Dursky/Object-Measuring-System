import cv2
import numpy as np
from typing import List, Dict
from utils.logger import setup_logger

logger = setup_logger(__name__)

def get_default_config():
    """Return default visualization configuration."""
    return {
        'colors': {
            'reference': [0, 255, 0],
            'object': [0, 0, 255],
            'text': [255, 255, 255]
        },
        'text': {
            'font_scale': 0.8,
            'thickness': 2,
            'color': [255, 255, 255],
            'font': cv2.FONT_HERSHEY_SIMPLEX
        },
        'line': {
            'thickness': 2,
            'type': cv2.LINE_AA
        }
    }

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
    # Merge default config with provided config
    default_config = get_default_config()
    
    # Use provided config values or defaults
    text_color = config.get('text', {}).get('color', default_config['text']['color'])
    text_scale = config.get('text', {}).get('font_scale', default_config['text']['font_scale'])
    text_thickness = config.get('text', {}).get('thickness', default_config['text']['thickness'])
    object_color = config.get('colors', {}).get('object', default_config['colors']['object'])
    
    result = image.copy()
    
    for obj in measurements:
        # Draw object contour
        corners = obj['corners'].reshape((-1, 1, 2)).astype(np.int32)
        cv2.polylines(result, [corners], True, object_color, text_thickness)
        
        # Add dimensions text
        center = np.mean(corners, axis=0)[0].astype(int)
        text = f"{obj['width']}x{obj['height']}cm"
        cv2.putText(result, text, tuple(center),
                   cv2.FONT_HERSHEY_SIMPLEX,
                   text_scale,
                   text_color,
                   text_thickness)
    
    logger.info("Visualization generated")
    return result