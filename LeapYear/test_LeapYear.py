from SWE_HW_7.LeapYear.LeapYear import leapYear
import LeapYear as ly
import unittest


class TestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(ly.leapYear(4), True)
    def test_two(self):
        self.assertEqual(ly.leapYear(3), False)
    def test_three(self):
        self.assertEqual(ly.leapYear(2000), False)


if __name__ == "__main__":
    unittest.main()