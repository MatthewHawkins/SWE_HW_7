from SWE_HW_7.LeapYear.LeapYear import leapYear
import LeapYear as ly
import unittest


class TestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(ly.leapYear(2000), True)


if __name__ == "__main__":
    unittest.main()