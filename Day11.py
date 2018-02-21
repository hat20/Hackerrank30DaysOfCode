#!/bin/python3

import sys

def hourglass_sum(arr):
    i,j,k,add,maxsum=0,0,0,0,-100
    while i<4:
        while j<4:
            add = addition_of_hourglass(arr,i,j)
            if(maxsum < add):
                maxsum = add

            j = j+1
        j = 0
        i = i+1
    print(maxsum)
    
    
def addition_of_hourglass(arr,i,j):
    add = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
    return add


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

hourglass_sum(arr)
