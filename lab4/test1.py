import unittest
import sys, os


sys.path.append(os.getcwd())
from main import *

test1 = [0]
test2 = [-1.41, 1.41]
test3 = [-2.0, 2.0, 0.0]

class TestGetRoots(unittest.TestCase):
    def test_get_roots1(self):
        self.assertEqual(get_roots(1, 0, 0), test1)
    def test_get_roots2(self):
        self.assertEqual(get_roots(1, 0, -4), test2)
    def test_get_roots3(self):
        self.assertEqual(get_roots(1, -4, 0), test3)

if __name__ == "__main__":
    unittest.main()