import unittest
from utils import load_ciks

class TestCiksLoader(unittest.TestCase):
    
    def test_load_ciks_valid_file(self):
        ciks = load_ciks('data/CIK.txt')
        self.assertIsInstance(ciks, list)
        self.assertGreater(len(ciks), 0)

    def test_load_ciks_emtpy_file(self):
        with open('data/empty_CIK.txt', 'w') as f:
            pass
        ciks = load_ciks('data/empty_CIK.txt')
        self.assertEqual(ciks, [])
    
    def test_load_ciks_invalid_file(self):
        with self.assertRaises(FileNotFoundError):
            load_ciks('nonexistent_file.txt')
    



