# Mathematical content

## Conjecture (Erdős #376)

There are infinitely many n ∈ ℕ such that gcd(C(2n,n), 105) = 1.

## Known partial result (proved here, elementary)

**Lemma.** For any prime p, there are infinitely many n with p ∤ C(2n,n).

*Proof.* Take n_k = (p^k - 1)/2. In base p, n_k has k digits all equal to
(p-1)/2. Doubling a digit (p-1)/2 gives p-1 < p, so no carry occurs in
n_k + n_k; by Kummer, p ∤ C(2n_k, n_k). ∎

## Computational result (verified)

All n ≤ 3^22 (≈ 3.14·10^10) with C(2n,n) coprime to 105 are:

1, 10, 756, 757, 3160, 3186, 3187, 3250, 7560, 7561, 7651, 20007,
59548377, 59548401.

(14 values; verified by exact digit tests, see `src/search.py` and
`results/solutions_up_to_1e8.json`.)

## Status of the main conjecture

Unresolved. No proof of infinitude or finiteness was found.
