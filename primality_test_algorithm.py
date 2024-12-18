import tracking_usage as tu
import math
import pandas as pd

# Exercice 2.- La primalite d’un nombre.

# * Soit n ∈ N. Proposer trois algorithmes pour verifier si n est premier ou non.
# * Varier les valeurs de n et dresser le tableau de complexit´e pratique pour chacun des algorithmes.
# * Expoter les r´esultats en Excel et comprer les courbes des trois algorithmes.

def is_prime_1(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_2(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_prime_3(n):
    if n <= 1:
        return False
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return sieve[n]


a = open("complexite.csv", "w")
a.write("N, O1, O2, O3\n")
n = 10

for i in range(3, 10000):
    avg_time1 = sum(tu.track_time(lambda: is_prime_1(i)) for _ in range(n)) / n
    avg_time2 = sum(tu.track_time(lambda: is_prime_2(i)) for _ in range(n)) / n
    avg_time3 = sum(tu.track_time(lambda: is_prime_3(i)) for _ in range(n)) / n
    a.write(f"{i}, {avg_time1:.8f}, {avg_time2:.8f}, {avg_time3:.8f}\n")
   

