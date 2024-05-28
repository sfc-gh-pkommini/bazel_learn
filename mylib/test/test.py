import unittest

from mylib.name import get_name


class TestGetName(unittest.TestCase):

    def testValue(self) -> None:
        self.assertEqual(get_name(), "Bazel")


if __name__ == "__main__":
    unittest.main()
