import functools
import time
from typing import Any, Callable


def hamle_sayaci() -> Callable[[], int]:
    """Cagrilinca degeri 1 artan sayac fonksiyonu dondurur."""
    sayac: int = 0

    def artir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def en_bagli_gezegenler(galaksi: dict[str, Any]) -> list[str]:
    """Gezegenleri baglanti sayisina gore azalan, esitlikte alfabetik siralar."""
    baglantilar = galaksi.get("baglantilar", {})
    gezegenler = galaksi.get("gezegenler", list(baglantilar.keys()))

    return sorted(
        gezegenler,
        key=lambda g: (-len(baglantilar.get(g, [])), g),
    )


def sure_olc(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """Fonksiyonun calisma suresini ekrana yazdiran sarmalayici."""

    @functools.wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic: float = time.perf_counter()
        sonuc: Any = fonksiyon(*args, **kwargs)
        bitis: float = time.perf_counter()
        print(f"[{fonksiyon.__name__}] Calisma suresi: {bitis - baslangic:.6f} saniye")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    ornek_galaksi = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "dünya": ["centauri", "sirius"],
            "centauri": ["dünya", "sirius", "orion"],
            "sirius": ["dünya", "centauri", "orion", "kara_delik"],
            "orion": ["centauri"],
            "kara_delik": [],
        },
    }

    print(en_bagli_gezegenler(ornek_galaksi))

    en_bagli_sureli = sure_olc(en_bagli_gezegenler)
    en_bagli_sureli(ornek_galaksi)
