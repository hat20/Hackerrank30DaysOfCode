def calculate_fine(d,m,y,dd,mm,yy):
    if(y<yy or (y==yy and m<mm) or (y==yy and m==mm and d<dd)):
        return 0
    elif y==yy and m==mm and d>dd:
        return 15*(d-dd)
    elif y==yy and m>mm:
        return 500*(m-mm)
    else:
        return 10000
        
d,m,y = [int(x) for x in input().split(' ')]    
dd,mm,yy = [int(x) for x in input().split(' ')]
print(calculate_fine(d,m,y,dd,mm,yy))