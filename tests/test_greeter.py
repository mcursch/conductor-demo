import unittest

from greeter import hello, farewell


class TestGreeter(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello("World"), "Hello, World!")


class TestFarewell(unittest.TestCase):
    def test_farewell_alice(self):
        self.assertEqual(farewell("Alice"), "Goodbye, Alice!")

    def test_farewell_world(self):
        self.assertEqual(farewell("World"), "Goodbye, World!")


if __name__ == "__main__":
    unittest.main()
