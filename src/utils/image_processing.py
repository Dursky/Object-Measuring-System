import cv2
import numpy as np
from typing import Tuple

def preprocess_image(image: np.ndarray) -> np.ndarray:
    """
    Preprocess the image for better object detection.
    
    Args:
        image: Input image in BGR format
        
    Returns:
        np.ndarray: Preprocessed image
    """
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Enhance contrast
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    enhanced = clahe.apply(blurred)
    
    return enhanced

def get_image_info(image: np.ndarray) -> Tuple[int, int, int]:
    """
    Get basic information about the image.
    
    Args:
        image: Input image
        
    Returns:
        Tuple containing height, width, and number of channels
    """
    height, width = image.shape[:2]
    channels = image.shape[2] if len(image.shape) > 2 else 1
    return height, width, channels

def resize_image(image: np.ndarray, max_dimension: int = 1200) -> np.ndarray:
    """
    Resize image while maintaining aspect ratio.
    
    Args:
        image: Input image
        max_dimension: Maximum dimension (width or height)
        
    Returns:
        np.ndarray: Resized image
    """
    height, width = image.shape[:2]
    if height > max_dimension or width > max_dimension:
        scale = max_dimension / max(height, width)
        new_width = int(width * scale)
        new_height = int(height * scale)
        return cv2.resize(image, (new_width, new_height))
    return image