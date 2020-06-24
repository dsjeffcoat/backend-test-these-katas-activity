import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        # self.fail("TODO: Write add unit test")
        self.assertEqual(katas.add(1, 2), 3)

    def test_multiply(self):
        # self.fail("TODO: Write multiply unit test")
        self.assertEqual(katas.multiply(10, 20), 200)

    def test_power(self):
        # self.fail("TODO: Write power unit test")
        self.assertEqual(katas.power(3, 4), 81)

    def test_factorial(self):
        # self.fail("TODO: Write factorial unit test")
        self.assertEqual(katas.factorial(10), 3628800)

    def test_fibonacci(self):
        # self.fail("TODO: Write fibonacci unit test")
        self.assertEqual(katas.fibonacci(25), 46368)


if __name__ == '__main__':
    unittest.main()
