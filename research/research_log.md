# Research log

## Attempts

1. Direct CRT construction for a single prime: works; infinite family
   n=(p^k-1)/2.

2. For two primes (3,5): computational search finds 771 solutions up to 3^18;
   growth suggests infinitely many, but no explicit infinite family found.

3. For three primes (3,5,7): computational search up to 3^22 finds 14
   solutions, largest 59,548,401 (and 59,548,401+24). No new solutions
   appear between 10^8 and 3^22. This neither proves finiteness nor infinitude.

4. Attempted to lift the single-prime construction via CRT across prime powers:
   requires the quotient (3^k-1)/(2·5^m) to have small base-5 digits; not
   established.

5. Attempted to use Bloom–Croot for small bases: their technical condition
   fails for 3,5,7.

## Conclusion

No new theorem was established. The problem remains open. The computational
data are consistent with either a finite set (with largest solution around
6·10^7) or a very sparse infinite set.
