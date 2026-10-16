# test_sketchgranary.py
"""
Tests for SketchGranary module.
"""

import unittest
from sketchgranary import SketchGranary

class TestSketchGranary(unittest.TestCase):
    """Test cases for SketchGranary class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchGranary()
        self.assertIsInstance(instance, SketchGranary)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchGranary()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
