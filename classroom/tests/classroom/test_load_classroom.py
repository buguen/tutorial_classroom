import os
import types
from unittest import TestCase, main

import classroom
from classroom.tests import SAMPLE_DATA_DIR


class Test(TestCase):
    def test_sample_data(self):
        # Assert that using "load_classroom" with the sample data
        # results in the expected delegates.
        pattern = os.path.join(SAMPLE_DATA_DIR, '*.yaml')
        groups = classroom.load_classroom(pattern)
        self.assertIsInstance(groups, types.GeneratorType)
        expected = [('Ringo', 'John', 'Paul', 'George'),
                    ('Barney', 'Fred'),
                    ('Jackie', 'Tito', 'Jermaine', 'Marlon',
                     'Randy', 'Michael')]
        self.assertEqual(list(groups), expected)


if __name__ == '__main__':
    main()
