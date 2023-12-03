def bezout(a, b):
    '''
    Расширенный алгоритм Евклида
    '''
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx*q
        y, yy = yy, y - yy*q
    return (x, y, a)


def sieve_eratosthenes(n):
    """
    Решето Эратосфена
    """
    a = range(n + 1)
    a = list(a)
    a[1] = 0
    result_list = []
    i = 2
    while i <= n:
        if a[i] != 0:
            result_list.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return result_list