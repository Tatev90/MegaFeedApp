import unittest

from project.apitest.Sheet1 import list_of_lists
from project.apitest.Sheet2 import list_of_lists1
from project.apitest.Sheet3 import list_of_lists2
from project.apitest.Sheet4 import list_of_lists3
from project.apitest.main import obj, current_game


class Tests(unittest.TestCase):

    def test_auth(self):
        self.assertTrue(obj["Command"], "auth")
        self.assertIsNone(obj["Error"])

    def test_subscribe(self):
        self.assertIn(obj["Command"], "subscribeGames")
        self.assertIsNone(obj["Error"])

    def test_Sheet1(self):
        for item in current_game:
            for item2 in list_of_lists:
                if item[0] == item2[0]:
                    self.assertListEqual(item, item2)

    def test_Sheet2(self):
        for item in current_game:
            for item2 in list_of_lists1:
                if item[0] == item2[0]:
                    self.assertEqual(item[0], item2[0])
                    self.assertEqual(item[1], item2[1])
                    self.assertIn(item[2], item2[2])
                    self.assertEqual(item[3], item2[3])
                    self.assertEqual(item[4], item2[4])

    def test_Sheet3(self):
        for item in current_game:
            for item2 in list_of_lists2:
                if item[0] == item2[0] and item[1] == item2[1]:
                    self.assertListEqual(item, item2)

    def test_Sheet4(self):
        for item in list_of_lists3:
            for item2 in current_game:
                if item2[0] == 233 and item[0] == 233:
                    self.assertEqual(item[4], item2[4])


if __name__ == '__main__':
    unittest.main()
