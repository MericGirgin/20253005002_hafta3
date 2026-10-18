from collections.abc import Generator


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
