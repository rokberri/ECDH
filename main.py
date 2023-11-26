from curve.elipse_curve import ElipseCurve
import numpy as np
from curve.point import Point
from diffi_hellman import diffi_hellman


def main():
    # для Fp
    # размер поля, простое число
    p = 37
    # для F2^m
    # простое число 
    m = 7
    # общие значения для обоих полей 
    # элептическая кривая, нужны будут ее коэфиценты
    c = ElipseCurve(a=-1,b=3,mod=37)
    # точка на кривой С, (генератор), большого порядка 
    G = Point(2,3,c.get_mod,curve=c)
    # порядок точки G
    N = G.get_rank()
    # сомножитель, общее число точек на кривой / n, h->max
    h = int(c.get_rang()/N)
    # несократимый многочлен степени m в бинарном представлении. Играет роль модуля при операциях
    f = 64
    
    print(diffi_hellman(G,c,m,f))
    print('EXIT')


if __name__ == '__main__':
    main()