import unittest
import task
from datetime import date


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

    def test_first_last(self):
        brack = [2, 4, 6, 8, 18]
        first, last = task.first_y_last(brack)
        self.assertEqual(first, 2)
        self.assertEqual(18, last)

    def test_days_between(self):
        last_date = date(2020, 3, 1)
        first_date = date(2020, 2, 23)

        self.assertEqual(7, task.date_between(first_date, last_date))


if __name__ == '__main__':
    unittest.main()
