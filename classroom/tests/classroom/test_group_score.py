from unittest import TestCase, main

from classroom import group_score


class Test(TestCase):
    def test_score_1(self):
        self.assertEqual(group_score(range(1)), 3)

    def test_score_2(self):
        self.assertEqual(group_score(range(2)), 1)

    def test_score_3(self):
        self.assertEqual(group_score(range(3)), 0)

    def test_score_4(self):
        self.assertEqual(group_score(range(4)), 2)

    def test_score_5(self):
        self.assertEqual(group_score(range(5)), 5)


if __name__ == '__main__':
    main()