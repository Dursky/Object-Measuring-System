import logging
import yaml
from pathlib import Path

def setup_logger(name):
    """Configure and return a logger instance."""
    with open('config/logging_config.yaml', 'r') as f:
        config = yaml.safe_load(f)
        
    # Create logs directory if it doesn't exist
    Path('logs').mkdir(exist_ok=True)
    
    # Configure logging
    logging.config.dictConfig(config)
    return logging.getLogger(name)