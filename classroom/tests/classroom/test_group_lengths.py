from unittest import TestCase, main

import numpy as np
from numpy.testing import assert_array_equal

from classroom import group_lengths


class Test(TestCase):
    def test_score_1(self):
        expected = np.array([4, 2, 6, 3, 0])
        classroom = [range(length) for length in expected]
        assert_array_equal(group_lengths(classroom), expected)


if __name__ == '__main__':
    main()