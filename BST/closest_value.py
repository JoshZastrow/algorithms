#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
import string
from pprint import pprint

"""
find the closet value to target in a binary search tree.
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    """
    >>> solve = Solution()
    >>> root = TreeNode(
    ... val=4, 
    ... left=TreeNode(
    ...     val=2, 
    ...     left=TreeNode(
    ...         val=1), 
    ...     right=TreeNode(
    ...         val=3)
    ...     ),
    ... right=TreeNode(
    ...     val=5, 
    ...     left=None, 
    ...     right=TreeNode(
                val=10)
    ...     )
    ... )
    >>> solve.closestValue(root, 3.7)
    4
    >>> solve.closestValue(root, 2.7)
    3

    """
    def closestValue(self, root, target):
        closest_value = root.val
        
        while root:
            if abs(root.val - target) < abs(closest_value - target):
                closest_value = root.val

            if root.val > target:
                root = root.left
            elif root.val < target:
                root = root.right
            else:
                return root.val
                
        return closest_value


if __name__ == "__main__":
    import doctest
    doctest.testmod()
