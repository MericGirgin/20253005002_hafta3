def gorev_kaydi(
    baslik: str,
    *adimlar: str,
    oncelik: str = "normal",
    **ekler: str,
) -> str:
    """Gorev basligi, adimlari ve ek bilgileri formatlar."""
    satirlar: list[str] = [f"[{oncelik.upper()}] {baslik}"]

    for index, adim in enumerate(adimlar, start=1):
        satirlar.append(f" {index}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f" {anahtar}: {deger}")

    return "\n".join(satirlar)


if __name__ == "__main__":
    # 1. Dogrudan cagri
    print(
        gorev_kaydi(
            "Kara deliğe atla",
            "Kredi kazan",
            "Pilot bul",
            "Hiperdrive al",
            oncelik="yüksek",
            sorumlu="Ayşe",
        )
    )

    print()

    # 2. Unpacking (* ve **) ile cagri
    adimlar_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}

    print(
        gorev_kaydi(
            "Kara deliğe atla",
            *adimlar_listesi,
            oncelik="yüksek",
            **ek_bilgiler,
        )
    )
