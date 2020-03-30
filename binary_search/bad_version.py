#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import string
from pprint import pprint

class isBadVersion:

    def __init__(self, b):
        self.b = b

    def __call__(self, n):
        return n == self.b


def firstBadVersion(n, b):
    """
    :type n: int
    :rtype: int

    >>> firstBadVersion(10, 5)
    5
    """

    badVersion = isBadVersion(b)

    if n <= 1:
        return n
    
    beg_version = 0
    end_version = n # 1
    
    while beg_version < end_version:
        mid_version = beg_version + (end_version - beg_version) // 2
        
        if not badVersion(mid_version):
            beg_version = mid_version + 1
        else:
            end_version = mid_version
            
    return beg_version

if __name__ == "__main__":
    import doctest
    doctest.testmod()
