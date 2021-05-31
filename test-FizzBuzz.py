import FizzBuzz as fb
import unittest


class TestCase(unittest.TestCase):
    def test_one(self):
        self.assertEqual(fb.fizzBuzz(1), 1)
    def test_fizz(self):
        self.assertEqual(fb.fizzBuzz(3), "Fizz")
    def test_buzz(self):
        self.assertEqual(fb.fizzBuzz(5), "Buzz")


if __name__ == "__main__":
    unittest.main()