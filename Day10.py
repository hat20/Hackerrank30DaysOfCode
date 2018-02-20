#!/bin/python3

import sys

def convert_to_binary(n):
    bits = []
    while(n>0):
        bits.append(n%2)
        n = n//2
    bits.reverse()
    return bits

def count_consecutive_ones(bits):
    l,i,count,countmax = len(bits),0,0,0
    while(i<l-1):
        if(bits[i]!=1):
            count = 0
        elif(bits[i]==1):
            count = 1
            j=i
            while(j<l-1):
                if(bits[j]==bits[j+1]):
                    count = count + 1
                else:
                    break
                j = j+1
        if(count>countmax):
            countmax = count
        i = i+1    
            
    print(countmax)        
        
    

n = int(input().strip())
binary_num = convert_to_binary(n)
count_consecutive_ones(binary_num)

