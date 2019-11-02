import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def expMod(g, v, n):
    return g**v % n


if __name__ == '__main__':
    p = 29
    g = 2
    print(f"p = {p}, g = {g}")

    x = 4  # Alice
    y = 6  # Bob
    print(f"Alice: x = {x}")
    print(f"Bob: y = {y}")

    # Alice sends g^x % p
    gx = expMod(g, x, p)

    # Bob sends g^y % p
    gy = expMod(g, y, p)

    # Shared key g^(x * y) % p
    gxy = expMod(g, x * y, p)

    print(f"Alice send: {gx}")
    print(f"Bob send: {gy}")
    print(f"They will agree on: {gxy}")
