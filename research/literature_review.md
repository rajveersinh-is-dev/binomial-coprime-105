# Literature review

## Known results

- Kummer's theorem: for a prime p, p ∤ C(2n,n) iff no carry occurs when
  adding n+n in base p, i.e. every base-p digit of n is < p/2.

- For a single prime p, infinitely many n with p ∤ C(2n,n) exist:
  take n = (p^k - 1)/2; all base-p digits are (p-1)/2.

- Erdős and Graham conjectured (problem #376) that for 105 = 3·5·7 there
  are infinitely many n with C(2n,n) coprime to 105.

- Granville's heuristic and the Dartmouth note suggest that for three primes
  the answer may be finite or infinite depending on a logarithmic condition;
  the heuristic sum for (3,5,7) is ≈0.974 < 1, predicting infinitely many.

- Bloom–Croot (2025, arXiv:2509.02835): for r bases g_i that are
  multiplicatively independent and weights κ_i with
  Σ log_{g_i}(g_i/ceil(κ_i g_i)) < 1, there should be infinitely many n
  whose base-g_i digits are < κ_i g_i. They prove a weaker version
  (all but ε log n digits small) when the bases are large enough
  (≥ 10^94 for r=3, κ=1/2). The small bases 3,5,7 are not covered.

## Precise gap

No unconditional proof or disproof is known for the triple (3,5,7).
The weak (Bloom–Croot) result does not apply, and the full digit condition
for all positions remains open.
