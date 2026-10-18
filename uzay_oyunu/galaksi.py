import json
from pathlib import Path
from typing import Any, Optional


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: Any,
) -> dict[str, Any]:
    """Haritayi olusturur ve dogrular."""
    if baslangic not in gezegenler:
        raise ValueError(f"Baslangic gezegeni '{baslangic}' gezegenler listesinde yok!")

    yakit: int = kwargs.get("yakit", 50)

    galaksi: dict[str, Any] = {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }

    for k, v in kwargs.items():
        if k != "yakit":
            galaksi[k] = v

    return galaksi


def galaksi_dosyasini_oku(dosya_yolu: Optional[str] = None) -> dict[str, Any]:
    """galaksi.json dosyasini okuyup galaksi_kur fonksiyonuna iletir."""
    if dosya_yolu is None:
        dosya_yolu = str(Path(__file__).parent / "galaksi.json")

    with open(dosya_yolu, "r", encoding="utf-8") as f:
        veri: dict[str, Any] = json.load(f)

    return galaksi_kur(**veri)
