from itertools import islice, takewhile
import pytest
from uzay_oyunu.akis import fibonacci, yakit_gostergesi


# --- Görev 1 Testleri ---
def test_fibonacci_next():
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


def test_fibonacci_islice():
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(islice(fibonacci(), 12)) == beklenen


def test_fibonacci_takewhile():
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert list(takewhile(lambda x: x < 100, fibonacci())) == beklenen


def test_fibonacci_tek_kullanimlik():
    g = fibonacci()
    ilk = list(islice(g, 5))
    ikinci = list(islice(g, 5))
    assert ilk != ikinci
    assert ilk == [0, 1, 1, 2, 3]
    assert ikinci == [5, 8, 13, 21, 34]


# --- Görev 2 Testleri ---
def test_yakit_gostergesi_ornek():
    # PDF örneği: list(yakit_gostergesi(100, 30)) -> [70, 40, 10, 0]
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_gostergesi_stop_iteration():
    g = yakit_gostergesi(50, 25)
    assert next(g) == 25
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)
