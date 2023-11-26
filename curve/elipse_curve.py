import math 


class ElipseCurve():
    """
    y2 = x3 + Ax + B 
    """
    def __init__(self,a=0,b=0, mod=23) -> None:
        self.__a = a
        self.__b = b
        self.__mod = mod
        
    @property
    def get_coef(self)->list:
        return (self.__a,self.__b,self.__c)\
    @property
    def get_a(self)->float:
        return self.__a
    @property
    def get_b(self)->float:
        return self.__b
    @property
    def get_mod(self)->float:
        return self.__mod
    def __str__(self) -> str:
        return f"y^2 = x^3 + ({self.__a})x + {self.__b}"

    def get_coordinates(self):
        coordinates_on_curve = list()
        for x in range(self.__mod):
            y_sqrt = (pow(x,3) + (self.__a*x) + self.__b) % self.__mod
            for y in range(self.__mod):
                if pow(y,2)%self.__mod == y_sqrt:
                    coordinates_on_curve.append((x,y))
        
        return coordinates_on_curve
    
    def get_rang(self)->int:
        return len(self.get_coordinates())+1
    
    def shoups_method(self):
        count = 1 
        for x in range(self.get_mod):
            y_sq = (x**3 + self.__a*x + self.__b) % self.get_mod
            for y in range(self.get_mod):
                if (y*y) % self.get_mod == y_sq:
                    count += 1
        return count