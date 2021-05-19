# For this problem, the goal is to write code for finding all files under a directory
# (and all directories beneath it) that end with ".c"

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):  # Check if user
        return 'Invalid path'

    found_entities = os.listdir(os.path.join(path, "."))
    paths = list()

    for entity in found_entities:
        if os.path.isdir(os.path.join(path, entity)):
            paths += find_files(suffix, os.path.join(path, entity))

        elif entity.endswith(suffix):
            paths.append(os.path.join(path, entity))

    return paths


# Tests

print(find_files('.c', './testdir/'))
#  returns ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files('.c', './testdir/subdir1/'))
#  returns ['./testdir/subdir1/a.c']

print(find_files('.c', '.'))
#  returns ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files('.h', '.'))
#  returns ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']

print(find_files('.h', ''))
# returns error
