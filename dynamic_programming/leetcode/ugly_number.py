from typing import List


def isUglyNumber(n: int) -> bool:
    """An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

    Given an integer n, return true if n is an ugly number.
    1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, 16
    Ugly number = 2**m * 3**n * 5**p
    """
    M = N = P = 0
    current = n
    tmp_bool = True
    while (current > 1) and tmp_bool:
        tmp_bool = False
        if current % 2 == 0:
            M += 1
            current /= 2
            tmp_bool = True
        if current % 3 == 0:
            N += 1
            current /= 3
            tmp_bool = True
        if current % 5 == 0:
            P += 1
            current /= 5
            tmp_bool = True
    return tmp_bool


def nthUglyNumber(N: int) -> list[int]:
    """An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
    Given an integer n, return the nth ugly number.
    """
    m = n = p = 0
    next_num = 1
    L = [1]
    while len(L) < N:
        next_num = min(L[m]*2, L[n]*3, L[p]*5)
        L.append(next_num)
        if next_num == L[m] * 2:
            m += 1
        if next_num == L[n] * 3:
            n += 1
        if next_num == L[p] * 5:
            p += 1
    return L


if __name__ == "__main__":
    print(nthUglyNumber(10))
