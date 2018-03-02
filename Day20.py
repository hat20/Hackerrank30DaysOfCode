import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
numSwapped =0
for i in range(0,n):
    for j in range(0,n-1):
        if(a[j]>a[j+1]):
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            numSwapped += 1
print("Array is sorted in",numSwapped,"swaps.")
print("First Element:",a[0])
print("Last Element:",a[n-1])