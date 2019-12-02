import unittest
import day_01


class MyTestCase(unittest.TestCase):
    def test_case01(self):
        self.assertEqual(day_01.fuel_required_by_module(12), 2)

    def test_case02(self):
        self.assertEqual(day_01.fuel_required_by_module(14), 2)

    def test_case03(self):
        self.assertEqual(day_01.fuel_required_by_module(1969), 654)

    def test_case04(self):
        self.assertEqual(day_01.fuel_required_by_module(100756), 33583)

    def test_case01_v2(self):
        self.assertEqual(day_01.fuel_required_by_module_v2(14), 2)

    def test_case03_v2(self):
        self.assertEqual(day_01.fuel_required_by_module_v2(1969), 966)

    def test_case04_v2(self):
        self.assertEqual(day_01.fuel_required_by_module_v2(100756), 50346)


if __name__ == '__main__':
    unittest.main()
