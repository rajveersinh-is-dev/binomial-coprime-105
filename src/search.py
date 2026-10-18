"""Exact search for integers n such that binom(2n, n) is coprime to a given modulus.

By Kummer's theorem, a prime p does NOT divide binom(2n,n) iff every base-p
digit of n is strictly less than p/2 (no carry in n+n in base p).

For a modulus m, coprimality to m is equivalent to the condition for every
prime power dividing m (for squarefree m, for every prime dividing m).
"""
from __future__ import annotations




def base_digits(n, base):
    """Base digits.
    
    Args:
        n:
        base:
    
    Returns:
        The computed result
    
    """
    ds = []
    while n > 0:
        ds.append(n % base)
        n //= base
    return ds or [0]


def no_carry(n, p) -> bool:
    """True iff p does not divide C(2n,n)."""
    half = (p + 1) // 2  # digits must be < p/2, i.e. <= (p-1)//2
    limit = (p - 1) // 2 + 1  # first forbidden digit
    for d in base_digits(n, p):
        if d >= (p + 1) // 2:
            return False
    return True


def coprime_to_modulus(n, primes):
    """Coprime to modulus.
    
    Args:
        n:
        primes:
    
    Returns:
        The computed result
    
    """
    return all(no_carry(n, p) for p in primes)


def search(limit, primes):
    """Return all n in [1, limit] with C(2n,n) coprime to product(primes)."""
    out = []
    for n in range(1, limit + 1):
        if coprime_to_modulus(n, primes):
            out.append(n)
    return out


def search_via_base3(limit):
    """Faster search for the (3,5,7) case using base-3 digit enumeration."""
    out = []
    # enumerate numbers whose base-3 digits are 0 or 1 (necessary for p=3)
    # up to limit, by subsets of positions.
    maxpow = 0
    p = 1
    while p <= limit:
        maxpow += 1
        p *= 3
    for mask in range(1, 1 << maxpow):
        n = 0
        mm = mask
        pp = 1
        while mm:
            if mm & 1:
                n += pp
            mm >>= 1
            pp *= 3
        if n > limit:
            continue
        if no_carry(n, 5) and no_carry(n, 7):
            out.append(n)
    return sorted(set(out))


if __name__ == "__main__":
    primes = [3, 5, 7]
    L = 10**6
    res = search_via_base3(L)
    print(len(res))
    print(res)
