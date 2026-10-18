"""Görev 2, Görev 3 ve Görev 5 birim testleri."""

import json
from pathlib import Path
from uzay_oyunu.araclar import en_bagli_gezegenler, hamle_sayaci, sure_olc
from uzay_oyunu.kayit import gorev_kaydi
from uzay_oyunu.oyun import galaksi_kur


def test_gorev_kaydi_unpacking():
    adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ekler = {"sorumlu": "Ayşe"}
    cikti = gorev_kaydi(
        "Kara deliğe atla", *adimlar, oncelik="yüksek", **ekler
    )
    beklenen = (
        "[YÜKSEK] Kara deliğe atla\n"
        " 1. Kredi kazan\n"
        " 2. Pilot bul\n"
        " 3. Hiperdrive al\n"
        " sorumlu: Ayşe"
    )
    assert cikti == beklenen


def test_galaksi_kur():
    json_yolu = Path(__file__).parent.parent / "uzay_oyunu" / "galaksi.json"
    with open(json_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)

    # PDF'teki örnek: >>> g = galaksi_kur(**veri)
    g = galaksi_kur(**veri)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100

    # Varsayılan yakıt testi:
    g_varsayilan = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g_varsayilan["yakit"] == 50


def test_galaksi_kur_hatali_baslangic_hata():
    hata_olustu = False
    try:
        galaksi_kur(["dünya"], {"dünya": []}, "plüton")
    except ValueError:
        hata_olustu = True
    assert hata_olustu, "Başlangıç gezegeni haritada yokken ValueError fırlatılmalı!"


def test_hamle_sayaci_closure():
    sayac = hamle_sayaci()
    assert sayac() == 1
    assert sayac() == 2
    assert sayac() == 3


def test_en_bagli_gezegenler_lambda():
    json_yolu = Path(__file__).parent.parent / "uzay_oyunu" / "galaksi.json"
    with open(json_yolu, "r", encoding="utf-8") as f:
        veri = json.load(f)

    sirali = en_bagli_gezegenler(veri)
    assert sirali == ["sirius", "centauri", "dünya", "orion", "kara_delik"]


def test_sure_olc_bonus():
    cagrildi = False

    @sure_olc
    def topla(a, b):
        nonlocal cagrildi
        cagrildi = True
        return a + b

    assert topla(3, 4) == 7
    assert cagrildi
