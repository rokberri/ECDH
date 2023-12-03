from curve.elipse_curve import ElipseCurve
import numpy as np
from curve.point import Point
from diffi_hellman import diffi_hellman
from utils.utils import bezout, sieve_eratosthenes
from random import choice



def get_G(curve:ElipseCurve):
    """
    Метод автоматического выбора генератора G(точка на прямой)
    """
    G = Point(float('inf'),float('inf'),curve.get_mod,curve=curve)
    ZERO = G
    points = curve.get_coordinates()
    N = curve.shoups_method()   
    n = [ el for el in range(1,N+1,1) if N%el==0]
    n = max(set(n) & set(sieve_eratosthenes(N)))
    h = N/n
    while G.__eq__(ZERO)== True:
        rand_point = choice(points)
        R = Point(rand_point[0],rand_point[1],curve.get_mod,curve)
        G = R * int(h)
    return G

def main():
    # для Fp
    # размер поля, простое число
    p = 37
    # для F2^m
    # простое число 
    m = 7
    # общие значения для обоих полей 
    # элептическая кривая, нужны будут ее коэфиценты
    c = ElipseCurve(a=-1,b=3,mod=p)
    # точка на кривой С, (генератор), большого порядка 
    G = Point(2,3,c.get_mod,curve=c)
    # порядок точки G
    N = G.get_rank()
    # сомножитель, общее число точек на кривой / n, h->max
    h = int(c.get_rang()/N)
    # несократимый многочлен степени m в бинарном представлении. Играет роль модуля при операциях
    f = 64
    try:
        print(diffi_hellman(G,c,p,m,f))
    except ValueError:
        print("Bad curve")
    print('EXIT')

def testing():
    c = ElipseCurve(a=-1,b=3,mod=37)
    print(get_G(c))

if __name__ == '__main__':
    # main()
    testing()