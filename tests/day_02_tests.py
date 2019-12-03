import unittest
import day_02


class MyTestCase(unittest.TestCase):
    def test_case01(self):
        self.assertEqual(day_02.process_opcodes([1,0,0,0,99]), [2,0,0,0,99])
    def test_case02(self):
        self.assertEqual(day_02.process_opcodes([2,3,0,3,99]), [2,3,0,6,99])
    def test_case03(self):
        self.assertEqual(day_02.process_opcodes([2,4,4,5,99,0]), [2,4,4,5,99,9801])
    def test_case04(self):
        self.assertEqual(day_02.process_opcodes([1,1,1,4,99,5,6,0,99]), [30,1,1,4,2,5,6,0,99])


if __name__ == '__main__':
    unittest.main()
