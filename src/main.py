import argparse
import cv2
import yaml
from pathlib import Path
from detector.reference_detector import ReferenceDetector
from detector.object_detector import ObjectDetector
from measurement.size_calculator import SizeCalculator
from utils.visualization import visualize_results
from utils.logger import setup_logger

logger = setup_logger(__name__)

def parse_arguments():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description='Object Measurement System')
    parser.add_argument('--image', type=str, required=True, help='Path to input image')
    parser.add_argument('--config', type=str, default='config/config.yaml', help='Path to configuration file')
    parser.add_argument('--output', type=str, default='data/output', help='Output directory')
    return parser.parse_args()

def main():
    """Main application entry point."""
    args = parse_arguments()
    
    # Load configuration
    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)
    
    # Load image
    logger.info(f"Loading image from {args.image}")
    image = cv2.imread(args.image)
    if image is None:
        raise ValueError(f"Could not load image: {args.image}")
    
    # Initialize detectors
    reference_detector = ReferenceDetector(config['reference'])
    object_detector = ObjectDetector(config['detection'])
    size_calculator = SizeCalculator(config['measurement'])
    
    # Detect objects
    logger.info("Detecting reference object")
    reference_object = reference_detector.detect(image)
    if reference_object is None:
        raise ValueError("Reference object not found in image")
    
    logger.info("Detecting measurement objects")
    objects = object_detector.detect(image)
    
    # Calculate dimensions
    logger.info("Calculating object dimensions")
    measurements = size_calculator.calculate(objects, reference_object)
    
    # Visualize results
    logger.info("Generating visualization")
    result_image = visualize_results(image, measurements, config['visualization'])
    
    # Save results
    output_path = Path(args.output)
    output_path.mkdir(parents=True, exist_ok=True)
    
    output_file = output_path / 'result.jpg'
    cv2.imwrite(str(output_file), result_image)
    logger.info(f"Results saved to {output_file}")

if __name__ == '__main__':
    main()
