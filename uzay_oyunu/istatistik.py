from functools import partial, reduce
from typing import Any


# 1. Soru: Gezegen adlarinin buyuk harfli listesi
def buyuk_harfli_gezegenler_map(galaksi: dict[str, Any]) -> list[str]:
    """map kullanarak gezegen adlarini buyuk harfe cevirir."""
    return list(map(lambda g: g.upper(), galaksi["gezegenler"]))


def buyuk_harfli_gezegenler_comp(galaksi: dict[str, Any]) -> list[str]:
    """Liste ureteci (comprehension) ile gezegen adlarini buyuk harfe cevirir."""
    return [g.upper() for g in galaksi["gezegenler"]]


# 2. Soru: En az iki baglantisi olan gezegenler
def en_az_iki_baglantili_filter(galaksi: dict[str, Any]) -> list[str]:
    """filter kullanarak en az 2 baglantisi olan gezegenleri suzer."""
    baglantilar = galaksi.get("baglantilar", {})
    return list(filter(lambda g: len(baglantilar.get(g, [])) >= 2, galaksi["gezegenler"]))


def en_az_iki_baglantili_comp(galaksi: dict[str, Any]) -> list[str]:
    """Liste ureteci ile en az 2 baglantisi olan gezegenleri suzer."""
    baglantilar = galaksi.get("baglantilar", {})
    return [g for g in galaksi["gezegenler"] if len(baglantilar.get(g, [])) >= 2]


# 3. Soru: Toplam baglanti sayisi
def toplam_baglanti_reduce(galaksi: dict[str, Any]) -> int:
    """reduce kullanarak toplam baglanti sayisini hesaplar."""
    baglantilar = galaksi.get("baglantilar", {})
    return reduce(lambda acc, g: acc + len(baglantilar.get(g, [])), galaksi["gezegenler"], 0)


def toplam_baglanti_sum(galaksi: dict[str, Any]) -> int:
    """sum ve jenerator ifadesi ile toplam baglanti sayisini hesaplar."""
    baglantilar = galaksi.get("baglantilar", {})
    return sum(len(baglantilar.get(g, [])) for g in galaksi["gezegenler"])


# functools.partial:
def yolculuk(kaynak: str, hedef: str, mesafe: int, hiz: int = 1) -> float:
    """Belirli bir hizda iki gezegen arasi seyahat suresini hesaplar."""
    return mesafe / hiz


# hiz=3 parametresi sabitlenmis yeni fonksiyon
hizli_yolculuk = partial(yolculuk, hiz=3)

# Okunabilirlik yorumu:
# Liste uretecleri (comprehension) ve sum() kullanimi, lambda fonksiyonlu
# map/filter/reduce yapilarina gore Python soz dizimine cok daha dogal,
# anlasilir ve okunaklidir (Pythonic yaklasim).


if __name__ == "__main__":
    ornek = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "sirius", "orion"],
            "sirius": ["dünya", "centauri", "orion", "kara_delik"],
            "orion": ["centauri"],
            "kara_delik": [],
        },
    }
    print(buyuk_harfli_gezegenler_map(ornek))
    print(en_az_iki_baglantili_filter(ornek))
    print(toplam_baglanti_reduce(ornek))
