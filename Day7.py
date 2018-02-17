#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
arr.reverse()
#converted the int array into string array
sarr = [str(a) for a in arr]
print(" ".join(sarr))
