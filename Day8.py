
dict = {}
def init_dictionary(name,val):
    dict[name] = val
    
def search_dictionary(name):
    if name in dict:
        print(name,end='')
        print("=",end='')
        print(dict[name])
    else:
        print("Not found")

n = int(input())
for i in range(0,n):
    name,value = input().split(" ")
    value = int(value)
    init_dictionary(name,value)

#unknown number of queries    
queries = []
while True:
    try:
        inp = input()
        if inp =="":
            break
        else:    
            queries.append(inp)
    except EOFError:
        break
    
for i in queries:
    search_dictionary(i)