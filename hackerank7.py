''' Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.'''

import math
import os
import random
import re
import sys




if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    reverse=arr[::-1]
    for i in range(len(reverse)):
        print(reverse[i], end=' ')