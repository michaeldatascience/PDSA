import math
class Triangle:
    def _maximum(a,b,c):
        list = [a,b,c]
        return max(list)

    def __init__(self, A, B, C):
        (self.sideA, self.sideB, self.sideC) = (A,B,C)

    def Is_valid(self):
        if (self.sideA + self.sideB) > self.sideC and (self.sideA + self.sideC) > self.sideB and (self.sideB + self.sideC) > self.sideA:
            return "Valid"
        else:
            return "Invalid"
        
    def Side_Classification(self):
        if self.Is_valid() == "Valid":
            result = "None"
            if self.sideA==self.sideB==self.sideC:
                result = "Equilateral"
            
            if (self.sideA == self.sideB and self.sideC!= self.sideA) or (self.sideA == self.sideC and self.sideB!= self.sideA) or (self.sideB == self.sideC and self.sideA!= self.sideB):
                result = "Isosceles"

            if (self.sideA!=self.sideB and self.sideB!= self.sideC):
                result = "Scalene"
        else:
            return "Invalid"
        
        return result

    def Angle_Classification(self):
            result = "None"
            if self.Is_valid() == "Valid":
                list = [self.sideA,self.sideB,self.sideC]                
                hypotenuse= max(list)
                list.remove(hypotenuse)
                side1 = list[0]
                side2 = list[1]

                if side1**2 + side2**2 > hypotenuse**2:
                    result = "Acute"
                elif side1**2 + side2**2 == hypotenuse**2:
                    result = "Right"
                elif side1**2 + side2**2 < hypotenuse**2:
                    result = "Obtuse"
            else:
                result = "Invalid"

            return result
    
    def Area(self):
        result = 0
        if self.Is_valid() == "Valid":
            S = (self.sideA+self.sideB+self.sideC)/2
            Area = math.sqrt(S * (S-self.sideA ) * (S-self.sideB) * (S-self.sideC)  )
            return Area
        else:
            return "Invalid"
        



a=10
b=3
c=5
T=Triangle(a,b,c)
print(T.Is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())