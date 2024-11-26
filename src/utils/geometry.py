import numpy as np
from typing import List, Tuple

def calculate_angle(point1: np.ndarray, point2: np.ndarray, point3: np.ndarray) -> float:
    """
    Calculate angle between three points.
    
    Args:
        point1, point2, point3: Points forming the angle (point2 is vertex)
        
    Returns:
        float: Angle in degrees
    """
    vector1 = point1 - point2
    vector2 = point3 - point2
    
    cos_angle = np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    angle = np.arccos(np.clip(cos_angle, -1.0, 1.0))
    return np.degrees(angle)

def order_points(points: np.ndarray) -> np.ndarray:
    """
    Order points in clockwise order starting from top-left.
    
    Args:
        points: Array of points to order
        
    Returns:
        np.ndarray: Ordered points
    """
    rect = np.zeros((4, 2), dtype=np.float32)
    
    s = points.sum(axis=1)
    rect[0] = points[np.argmin(s)]  # Top-left
    rect[2] = points[np.argmax(s)]  # Bottom-right
    
    diff = np.diff(points, axis=1)
    rect[1] = points[np.argmin(diff)]  # Top-right
    rect[3] = points[np.argmax(diff)]  # Bottom-left
    
    return rect

def calculate_distance(point1: np.ndarray, point2: np.ndarray) -> float:
    """
    Calculate Euclidean distance between two points.
    
    Args:
        point1, point2: Points to measure distance between
        
    Returns:
        float: Distance between points
    """
    return np.linalg.norm(point1 - point2)

# src/utils/calibration.py
import numpy as np
import cv2
from typing import Tuple, Optional

class CameraCalibration:
    """Handle camera calibration for more accurate measurements."""
    
    def __init__(self):
        self.camera_matrix = None
        self.dist_coeffs = None
    
    def calibrate(self, 
                 object_points: List[np.ndarray],
                 image_points: List[np.ndarray],
                 image_size: Tuple[int, int]) -> Tuple[np.ndarray, np.ndarray]:
        """
        Calibrate camera using chessboard pattern.
        
        Args:
            object_points: 3D points in real world space
            image_points: 2D points in image plane
            image_size: Size of the image (width, height)
            
        Returns:
            Tuple containing camera matrix and distortion coefficients
        """
        ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(
            object_points, image_points, image_size, None, None
        )
        
        self.camera_matrix = mtx
        self.dist_coeffs = dist
        return mtx, dist
    
    def undistort_image(self, image: np.ndarray) -> Optional[np.ndarray]:
        """
        Remove lens distortion from image.
        
        Args:
            image: Input image
            
        Returns:
            np.ndarray: Undistorted image or None if not calibrated
        """
        if self.camera_matrix is None or self.dist_coeffs is None:
            return None
            
        return cv2.undistort(image, self.camera_matrix, self.dist_coeffs)