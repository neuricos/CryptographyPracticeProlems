/* Author: Devon Chen
 * Date: 11/2/2019
 */

/* gcc -o mod.so -shared -fPIC mod.c */

/* e * d % phi_n = 1 => d = ? */
int modInverse(int e, int phi_n)
{
    for (int d = 1; ; d++)
        if (e * d % phi_n == 1)
            return d;
}

/* b**e % d */
long expMod(int b, int e, int d)
{
    long c = 1;
    while (e-- != 0)
        c = c * b % d;
    return c;
}

int gcd(register int a, register int b)
{
    register int tmp;
    while (b) {
        tmp = a;
        a = b;
        b = tmp % b;
    }
    return a;
}
