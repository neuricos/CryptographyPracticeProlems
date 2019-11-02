import os

current_dir = os.path.dirname(os.path.abspath(__file__))

def getFactors(val):
    factors = []
    for i in range(2, val):
        if val % i == 0:
            factors.append(i)
    return factors


def modInverse(e, phi_n):
    d = 1
    while True:
        if e * d % phi_n == 1:
            return d
        d += 1


if __name__ == '__main__':
    c = None
    with open(f"{current_dir}/q3_crypt.txt") as f:
        c = f.readline().strip().split(" ")
        c = [int(e) for e in c]

    N = 33
    e = 3

    p, q = getFactors(N)
    print(f"p = {p}, q = {q}")

    phi_n = (p - 1) * (q - 1)
    print(f"phi(n) = {phi_n}")

    # Try to find d such that ed = 1 mod phi_n
    d = modInverse(e, phi_n)
    print(f"d = {d}")

    # decrypt c^d mod n = (m^e mod n)^d mod n = m
    m = []
    for v in c:
        m.append(v ** d % N)

    print()
    print("Plaintext:")
    print(m)
    print()

    # convert
    mp = [e + 64 for e in m]
    mp = [str(chr(e)) for e in mp]
    print(" ".join(mp))
    