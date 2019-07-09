#!/usr/bin/env python

# Usage
# Some sort of initialization method which can link to
# additional modules, expanding a library beyond just
# a single file

# Imports
# Must call which files to import and which functions
# from those files
from reuse_ex3.file1 import test1
from reuse_ex3.file2 import test2
from reuse_ex3.file3 import test3

__all__ = ["test1", "test2", "test3"]
