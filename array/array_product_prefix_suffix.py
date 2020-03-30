from typing import List
import math
import os
import random
import re
import sys
from collections import defaultdict
import string
from pprint import pprint


def productExceptSelf(nums: List[int]) -> List[int]:
    """
    >>> productExceptSelf([1,2,3,4])
    [24, 12, 8, 6]
    """
    n = len(nums)
    
    prefix = [1 for _ in range(n)]
    suffix = [1 for _ in range(n)]
    totals = [0 for _ in range(n)]
    
    for i in range(n-1):
        prefix[i+1] = prefix[i] * nums[i]
        suffix[i+1] = suffix[i] * nums[~i]
        
    for i in range(n):
        totals[i] = prefix[i] * suffix[~i]
        
    return totals


if __name__ == "__main__":
    import doctest
    doctest.testmod()
