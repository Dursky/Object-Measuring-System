import pytest
import numpy as np
from src.measurement.size_calculator import SizeCalculator

class TestSizeCalculator:
    @pytest.fixture
    def calculator(self):
        config = {
            'min_object_size': 1,
            'max_object_size': 100,
            'precision': 2
        }
        return SizeCalculator(config)
    
    def test_size_calculation(self, calculator):
        reference = {
            'corners': np.array([[0, 0], [100, 0], [100, 100], [0, 100]]),
            'reference_size': 10
        }
        
        objects = [{
            'corners': np.array([[200, 200], [300, 200], [300, 250], [200, 250]])
        }]
        
        results = calculator.calculate(objects, reference)
        assert len(results) == 1
        assert 'width' in results[0]
        assert 'height' in results[0]
        assert 'area' in results[0]