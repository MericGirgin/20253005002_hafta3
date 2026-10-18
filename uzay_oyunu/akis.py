from collections.abc import Generator, Iterable


def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayi dizisi ureteci."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:
    """Her next() cagrisinda yakiti tuketim kadar azaltip uretir, 0'a inince durur."""
    kalan = yakit
    while kalan > 0:
        kalan = max(0, kalan - tuketim)
        yield kalan
        if kalan == 0:
            break


def satirlari_oku(yol: str) -> Generator[str, None, None]:
    """Dosyayi satir satir okur; bos ve '#' ile baslayan satirlari atlar."""
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz


def ayristir(satirlar: Iterable[str]) -> Generator[tuple[str, str, int], None, None]:
    """Satirlardan (kaynak, hedef, yakit) demeti uretir."""
    for satir in satirlar:
        sol, sag = satir.split("->")
        kaynak = sol.strip()
        hedef, yakit_str = sag.strip().split()
        yield (kaynak, hedef, int(yakit_str))


def uzun_yolculuklar(
    kayitlar: Iterable[tuple[str, str, int]], esik: int
) -> Generator[tuple[str, str, int], None, None]:
    """Yakiti esikten buyuk olan kayitlari suzer."""
    for k in kayitlar:
        if k[2] > esik:
            yield k
