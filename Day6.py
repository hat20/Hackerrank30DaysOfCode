import sys

n = int(input())
    
def str_func(text):    
    s1,s2=[],[]
    for i, c in enumerate(text):
        if i % 2 == 0:
            s1.append(c)
        else:
            s2.append(c)
        res = "".join(s1) + " " + "".join(s2)
    return res
      
for i in range(0,n):
    text = input()
    print(str_func(text))            

        