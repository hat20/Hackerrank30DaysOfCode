class Difference:
    def __init__(self, a):
        self.__elements = a

#Complexity O(n) = n    
    def computeDifference(self):
        min,max = self.__elements[0],self.__elements[0]
        for i in self.__elements:
            if min>i:
                min = i
            elif max<i:
                max = i
        self.maximumDifference = max-min
                
            
            

        
# Complexity O(n) = n^2     
#        self.maximumDifference = 0
#        for i in self.__elements:
#            for j in self.__elements:
#                difference = abs(i-j)
#                if(difference > self.maximumDifference):
#                    self.maximumDifference = difference
                    
                    
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)