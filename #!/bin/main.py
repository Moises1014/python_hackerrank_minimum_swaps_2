#!/bin/python

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap =0
    li = []
    new_li=[]
    for x in range(0,len(arr)):
        li.append(arr[x])
    new_li = li[:]
    new_li.sort()
    for i in range(0,len(arr)):
       if new_li[i] == li[i]:
         i=i+1
       else:
        nu = new_li[i]
        index = li.index(nu)
        num_1 = li[i]
        li.pop(i)
        li.insert(i,nu)
        li.pop(index)
        li.insert(index,num_1)
        swap = swap +1
    return swap
         
        
         
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    arr = map(int, raw_input().rstrip().split())

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
