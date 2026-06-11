import unittest

from greeter import hello


class TestGreeter(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")


if __name__ == "__main__":
    unittest.main()
