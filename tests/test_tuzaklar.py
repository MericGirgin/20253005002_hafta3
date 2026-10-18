from typing import Optional


def hatali_yakit_ekle(miktar: int, depo: list = []):
    depo.append(miktar)
    return depo


def yakit_ekle(miktar: int, depo: Optional[list[int]] = None) -> list[int]:
    """None kalibi ile duzeltilmis yakit ekleme fonksiyonu."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_hatali_fonksiyon_tuzagi():
    hatali_yakit_ekle(10)
    assert hatali_yakit_ekle(20) == [10, 20]


def test_duzeltilmis_yakit_ekle():
    assert yakit_ekle(10) == [10]
    assert yakit_ekle(20) == [20]
