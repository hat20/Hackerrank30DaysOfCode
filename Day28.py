import re

N = int(input().strip())
l = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.search('@gmail.com$',emailID):
        l.append(firstName)
l.sort()
for i in l:
    print(i)