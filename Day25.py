import math
def prime(n):
    sq = int(math.sqrt(n))
    if(n==2):
        return "Prime"
    if(n==1 or n%2==0):
        return "Not prime"
    for i in range(2,sq+1):
        if not n%i:
            return "Not prime"
    return "Prime"

t = int(input())
for i in range(0,t):
    n = int(input())
    print(prime(n))
    