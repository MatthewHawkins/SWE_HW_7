import FizzBuzz as fb
import unittest


class TestCase(unittest.TestCase):
    def test_init(self):
        self.assertEqual(fb.fizzbuzz(1), 1)


if __name__ == "__main__":
    unittest.main()