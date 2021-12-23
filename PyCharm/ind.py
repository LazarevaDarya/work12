#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(5000)

m = int(input("Введите значение m: "))
n = int(input("Введите значение n: "))

def A(m, n):
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return A(m - 1, 1)
    if m > 0 and n > 0:
        return A(m - 1, A(m, n - 1))

print(A(m, n))


