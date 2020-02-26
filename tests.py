import unittest
import task


class TestCase(unittest.TestCase):
    def test1(self):
        expected = "success"
        self.assertEqual(expected, task.firstrun())

    def test2(self):
        expected = "failure"
        self.assertNotEqual(expected, task.firstrun())

    def test_area(self):
        radius = 5
        self.assertEqual(78, round(task.cir_area(radius)))


if __name__ == '__main__':
    unittest.main()
