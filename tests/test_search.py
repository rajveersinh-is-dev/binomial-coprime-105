import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from search import no_carry, coprime_to_modulus, search_via_base3, base_digits


def test_kummer_single_prime():
    # p=3: n=1 -> C(2,1)=2 not div by 3
    assert no_carry(1, 3) is True
    # n=2 -> C(4,2)=6 divisible by 3
    assert no_carry(2, 3) is False


def test_base_digits():
    assert base_digits(0, 3) == [0]
    assert base_digits(5, 3) == [2, 1]  # 5 = 12_3


def test_search_small():
    # n=1 should be coprime to 105
    res = search_via_base3(10)
    assert 1 in res
    assert 10 in res


def test_known_solution():
    # 59548377 is a known solution
    assert coprime_to_modulus(59548377, [3, 5, 7]) is True
