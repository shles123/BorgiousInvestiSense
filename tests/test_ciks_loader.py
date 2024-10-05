import unittest
import os
from src.utils import load_ciks

class TestCiksLoader(unittest.TestCase):
    
    def setUp(self):
        self.test_file = 'data/empty_CIK.txt'
        with open(self.test_file, 'w') as f:
            pass
    
    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_load_ciks_valid_file(self):
        ciks = load_ciks('data/CIK.txt')
        self.assertIsInstance(ciks, list)
        self.assertGreater(len(ciks), 0)

    def test_load_ciks_emtpy_file(self):
        self.test_file = 'data/empty_CIK.txt'
        with open(self.test_file, 'w') as f:
            pass
        ciks = load_ciks(self.test_file)
        self.assertEqual(ciks, [])
    
    def test_load_ciks_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            load_ciks('nonexistent_file.txt')
    



