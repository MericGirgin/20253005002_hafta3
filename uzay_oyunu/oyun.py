import json
from pathlib import Path
import sys
from typing import Any, Optional

proje_kok = str(Path(__file__).parent.parent)
if proje_kok not in sys.path:
    sys.path.insert(0, proje_kok)

try:
    from uzay_oyunu.akis import yakit_gostergesi
    from uzay_oyunu.araclar import hamle_sayaci
    from uzay_oyunu.galaksi import galaksi_dosyasini_oku, galaksi_kur
except ModuleNotFoundError:
    from akis import yakit_gostergesi
    from araclar import hamle_sayaci
    from galaksi import galaksi_dosyasini_oku, galaksi_kur


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    """Mevcut esyalara gore durum metnini uretir."""
    esyalar: list[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("hiperdrive")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: list[str]) -> str:
    """Gidilebilecek hedefleri numaralandirilmis liste metnine cevirir."""
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)


def travel(galaksi: Optional[dict[str, Any]] = None) -> int:
    """Oyuncunun uzay seyahati dongusu."""
    if galaksi is None:
        galaksi = galaksi_dosyasini_oku()

    sayac = hamle_sayaci()
    toplam_hamle: int = 0
    tuketim = galaksi.get("tuketim", 5)
    gosterge = yakit_gostergesi(galaksi["yakit"], tuketim=tuketim)

    credits: bool = False
    engines: bool = False
    copilot: bool = False

    while galaksi["yakit"] > 0:
        mevcut_konum: str = galaksi["konum"]

        envanter = envanter_metni(credits, engines, copilot)
        if envanter:
            print(envanter)

        if mevcut_konum == "kara_delik":
            print(f"Oyunu {toplam_hamle} hamlede bitirdin!")
            return toplam_hamle

        hedefler: list[str] = galaksi["baglantilar"].get(mevcut_konum, [])
        if not hedefler:
            print(f"{mevcut_konum} gezegeninden gidilecek rota kalmadi!")
            break

        print(hedef_menusu(hedefler))

        try:
            secim_str = input("Seciminiz (numara): ")
        except EOFError:
            break

        try:
            secim_no = int(secim_str)
            if 1 <= secim_no <= len(hedefler):
                yeni_hedef = hedefler[secim_no - 1]
            else:
                print("Gecersiz secim!")
                continue
        except ValueError:
            print("Lutfen bir sayi girin!")
            continue

        toplam_hamle = sayac()
        galaksi["konum"] = yeni_hedef

        try:
            galaksi["yakit"] = next(gosterge)
        except StopIteration:
            print("Yakıtın bitti, uzayda sürükleniyorsun…")
            break

        if yeni_hedef == "centauri":
            credits = True
        elif yeni_hedef == "sirius":
            copilot = True
        elif yeni_hedef == "orion":
            engines = True

    if galaksi["yakit"] <= 0:
        print("Yakıtın bitti, uzayda sürükleniyorsun…")

    return toplam_hamle


if __name__ == "__main__":
    travel()