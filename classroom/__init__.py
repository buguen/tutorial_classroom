import glob
import os

import numpy as np
import yaml


def load_classroom(glob_pattern):
    for fname in sorted(glob.glob(glob_pattern)):
        with open(fname) as fh:
            yield tuple(yaml.safe_load(fh).get('members') or [])


def group_score(group):
    length = len(group)
    # Map length of group to a score.
    scores_mapping = {3: 0,
                      2: 1,
                      4: 2,
                      1: 3}
    # Get the score. If the length isn't defined
    # in the scored_mapping, use length as default.
    score = scores_mapping.get(length, length)
    return score


def fail(classroom, scoring_function, maximum_score):
    for group in classroom:
        if scoring_function(group) > maximum_score:
            yield group


def group_lengths(classroom):
    return np.array([len(group) for group in classroom])
