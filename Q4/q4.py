import os
import ctypes

current_dir = os.path.dirname(os.path.abspath(__file__))
ll = ctypes.cdll.LoadLibrary
lib = ll(current_dir + "/mod.so")

def printBanner(pNum):
    print()
    print(f"{'='*30} p{pNum} {'='*30}")


if __name__ == '__main__':
    p = 9497
    q = 7187
    e = 3

    printBanner(1)
    # N = p * q
    N = p * q
    print(f"N = {N}")

    printBanner(2)
    # Phi(N) = (p - 1) * (q - 1)
    phi_n = (p - 1) * (q - 1)
    print(f"Phi(N) = {phi_n}")

    printBanner(3)
    # Find the greatest common divisor between e and Phi(N)
    v = lib.gcd(e, phi_n)
    print(f"Greatest Common Divisor between e and Phi(N) = {v}")
    print("=> e is relatively prime to Phi(N)")

    printBanner(4)
    d = lib.modInverse(e, phi_n)
    print(f"d = {d}")  # d = 45492171

    printBanner(5)
    m = 13571357
    print(f"P = {m}")
    # c = m ** e % N
    c = lib.expMod(m, e, N)
    print(f"C = {c}")

    printBanner(6)
    # mp = c ** d % N
    mp = lib.expMod(c, d, N)
    print(f"P = Decrypt(C) = {mp}")

    printBanner(7)
    cp = 24682468
    print(f"C' = {cp}")
    pp = lib.expMod(cp, d, N)
    print(f"P' = Decrypt(C') = {pp}")

    printBanner(8)
    cpp = lib.expMod(pp, e, N)
    print(f"C' = Encrypt(P') = {cpp}")

