from unittest import TestCase, main

from classroom import fail


class Test(TestCase):
    def test_good_group(self):
        classroom = [range(5), range(4)]
        result = fail(classroom, len, 4)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [range(5)])


if __name__ == '__main__':
    main()