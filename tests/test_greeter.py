import unittest

from greeter import farewell, hello


class TestGreeter(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")

    def test_farewell(self):
        self.assertEqual(farewell("World"), "Goodbye, World!")


if __name__ == "__main__":
    unittest.main()
