import glob
import os

import numpy as np
import yaml


def load_classroom(glob_pattern):
    """
    Given a glob pattern, returns a generator of groups (tuple of usernames).
    
    Parameters
    ==========
    glob_pattern : str
        The pattern to pass to glob to find appropriate groups stored in YAML
        form.
    
    Returns
    =======
    groups : generator of tuples
        The groups found in the YAML files. One tuple of usernames per group.

    """
    for fname in sorted(glob.glob(glob_pattern)):
        with open(fname) as fh:
            yield tuple(yaml.safe_load(fh).get('members') or [])


def group_score(group):
    """
    Score the quality of a group based on its size.
    
    Parameters
    ==========
    group : tuple
        The usernames of the members of this group.
    
    Returns
    =======
    score : int
        The "score" that this function assigns to the group.

    """
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
    """
    Filter the groups depending on whether they fail or not.
    
    .. note::
    
        When actually implementing this, one would normally simply define a
        function which determines whether a group passes or fails, and use
        Python's builtin filter function.
    
    Parameters
    ==========
    classroom : list of groups (tuples)
        The classroom, made up of tuples containing github usernames. One tuple
        per group.
    scoring_function : function
        The function to use to score each group.
    maximum_score : int
        If the score exceeds the maximum score, the group fails.
    
    Returns
    =======
    failed_groups : generator of groups
        The groups which failed to get below a certain score.

    """
    for group in classroom:
        if scoring_function(group) > maximum_score:
            yield group


def group_lengths(classroom):
    """Return an array of the lengths of each of the groups."""
    return np.array([len(group) for group in classroom])
