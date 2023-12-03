from curve.elipse_curve import ElipseCurve
from utils.utils import bezout


class Point():
    def __init__(self, x:int, y:int, mode=23, curve=ElipseCurve(a=0,b=0, mod=23)) -> None:
        self.__x = x
        self.__y = y
        self.__mod = mode
        self.__curve = curve

    @property
    def get_coord(self):
        return (self.__x,self.__y)
    
    @property
    def get_all_info(self):
        return {'X':self.__x,
                'Y':self.__y,
                'MOD':self.__mod,
                'CURVE':self.__curve.__str__()}
    
    def __str__(self) -> str:
        if self.__x == float('inf') and self.__y == float('inf'):
            return 'O'
        return '('+str(self.__x)+';'+str(self.__y)+')'
   
    @classmethod
    def inv_mod(cls,a,b):
        x, y, g = bezout(a, b)
        if g != 1:
            raise ValueError('The modular inverse does not exist')
        else:
            return x % b
    
    def __add__(self, other): 
        # для случая сложения с бесконечной точкой
        ZERO = Point(float('inf'),float('inf'),self.__mod,curve=self.__curve)
        if ZERO.__eq__(other):
            return self 
        elif self.__eq__(ZERO):
            return other 
        # если точки симметричны по Ох
        if self.__y == (-1 * other.__y):
            return ZERO
        # если точки одинаковые
        if self.__eq__(other):
            try:
                alpha = (3*pow(self.__x,2) + self.__curve.get_a) * Point.inv_mod(2 * self.__y, self.__mod)
            except ValueError:
                return ZERO
        else:
        # если точки разные
            try:
                alpha = (other.__y - self.__y) * Point.inv_mod((other.__x - self.__x), self.__mod)
            except ValueError:
                return ZERO
        x_new = (pow(alpha,2) - self.__x - other.__x) % self.__mod
        y_new = (alpha*(self.__x - x_new) - self.__y) % self.__mod
        
        return Point(x_new, y_new, self.__mod, self.__curve)
    
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __mul__(self, other):
        R = Point(float('inf'),float('inf'),self.__mod,curve=self.__curve)
        for i in range(other):
            R+=self
        return R
    
    def get_rank(self):
        ZERO = Point(float('inf'),float('inf'),self.__mod,curve=self.__curve)
        N = self.__curve.shoups_method()
        n = [ el for el in range(1,N+1,1) if N%el==0]
        for r in n:
            if (self * r)==(ZERO):
                return r

