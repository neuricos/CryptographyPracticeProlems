import os

script_dir = os.path.dirname(os.path.abspath(__file__))

def getBytes(fname):
    bs = []
    with open(fname, 'r') as f:
        for l in f.readlines():
            bs += [int(e, 16) for e in l.strip().split(" ")]
    return bs


def xorBlock(l1, l2):
    return [l1[i] ^ l2[i] for i in range(len(l1))]


if __name__ == '__main__':
    c1 = getBytes(script_dir + "/q5_c1.txt")
    c2 = getBytes(script_dir + "/q5_c2.txt")
    p1 = getBytes(script_dir + "/q5_p1.txt")

    row_len = int(len(c1) / 3)

    # XOR the second block of c1 and that of c2
    # we will get p1 XOR p2
    # Same for the third block
    p1_xor_p2_blk1 = xorBlock(c1[row_len:2*row_len], c2[row_len:2*row_len])
    p1_xor_p2_blk2 = xorBlock(c1[2*row_len:], c2[2*row_len:])
    
    p1_blk1 = p1[0:row_len]
    p1_blk2 = p1[row_len:]

    p2_blk1 = xorBlock(p1_xor_p2_blk1, p1_blk1)
    p2_blk2 = xorBlock(p1_xor_p2_blk2, p1_blk2)

    print("Plaintext of P2:")

    print(" ".join(["{:02x}".format(e) for e in p2_blk1]))
    print(" ".join(["{:02x}".format(e) for e in p2_blk2]))
    print()

    print("Ascii representation of P2:")

    # Convert to ascii
    print(" ".join([str(chr(e)) for e in p2_blk1]))
    print(" ".join([str(chr(e)) for e in p2_blk2]))
    # print(p1_xor_p2_blk1)
    # print(p1_xor_p2_blk2)