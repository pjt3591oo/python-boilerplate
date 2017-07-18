from packages.example import tp

import unittest


class test_package1(unittest.TestCase):
    def setUp(self):
        pass

    def test_case1(self):
        self.assertEqual(tp.test(), 10)

    def test_case2(self):
        self.assertNotEqual(tp.test(), 10)