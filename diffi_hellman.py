from curve.point import Point
from curve.elipse_curve import ElipseCurve
from random import randint


def diffi_hellman(G:Point,curve:ElipseCurve,p:int,m:int,f):
    if 4*pow(int(curve.get_a),3)+27*(pow(int(curve.get_b),2)) % p==0:
        print(4*pow(int(curve.get_a),3)+27*(pow(int(curve.get_b),2)) % p)
        raise ValueError("Bad curve")
    # сделать метод автоматичкского выбора точки G на соновании N
    N = G.get_rank()
    h = int(curve.get_rang()/N)


    A_private_key = get_private_key(N)
    A_public_key = G * A_private_key

    B_private_key = get_private_key(N)
    B_public_key = G * B_private_key

    A_secret_key = B_public_key * A_private_key
    B_secret_key = A_public_key * B_private_key
    if A_secret_key == B_secret_key:
        return A_secret_key
    else:
        raise ValueError("Something went wrong")

def get_private_key(N:int)-> int:
    """
    Метод для получения N
    """
    return randint(1,N)