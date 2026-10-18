import json
from itertools import islice, takewhile
from pathlib import Path
import pytest
from uzay_oyunu.akis import (
    ayristir,
    fibonacci,
    rota_sayaci,
    satirlari_oku,
    uzun_yolculuklar,
    yakit_gostergesi,
)


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
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]


def test_yakit_gostergesi_stop_iteration():
    g = yakit_gostergesi(50, 25)
    assert next(g) == 25
    assert next(g) == 0
    with pytest.raises(StopIteration):
        next(g)


# --- Görev 3 Testleri ---
def test_seyir_defteri_boru_hatti():
    dosya_yolu = str(Path(__file__).parent.parent / "veri" / "seyir.txt")

    toplam = sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu)))
    assert toplam == 88

    kayitlar = ayristir(satirlari_oku(dosya_yolu))
    uzunlar = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert uzunlar == ["sirius", "centauri", "orion", "kara_delik"]


# --- Görev 4 Testleri ---
def test_rota_sayaci():
    json_yolu = Path(__file__).parent.parent / "uzay_oyunu" / "galaksi.json"
    with open(json_yolu, "r", encoding="utf-8") as f:
        galaksi = json.load(f)

    say = rota_sayaci(galaksi["baglantilar"])
    # 0 adımda sadece başlangıç konumu vardır (1 rota)
    assert say("dünya", 0) == 1
    # 1 adımda dünya'nın bağlantı sayısı kadar rota vardır (2 rota)
    assert say("dünya", 1) == len(galaksi["baglantilar"]["dünya"])
    # Büyük adımda pozitif bir değer döner ve önbellek dolar
    assert say("dünya", 10) > 0
    assert say("dünya", 20) > 0
    info = say.cache_info()
    assert info.hits > 0
