import unittest
import sys, os

sys.path.append(os.getcwd())
from bot2 import *

test1 = 1
test2 = 2
test3 = 3

class TestGetRoots(unittest.TestCase):
    def test1_bot(self):
        res = summary(milk,milk_price,meat_fish,meat_fish_price,bread,bread_price,test1,test2,test3)
        self.assertEqual("Итоговая сумма = 670\n", res)
    def test2_bot(self):
        res = summary(milk,milk_price,meat_fish,meat_fish_price,bread,bread_price,test2,test1,test3)
        self.assertEqual("Итоговая сумма = 310\n", res)

if __name__ == "__main__":
    unittest.main()