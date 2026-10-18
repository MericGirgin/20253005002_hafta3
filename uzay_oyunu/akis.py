from collections.abc import Generator


def fibonacci() -> Generator[int, None, None]:
    """Sonsuz Fibonacci sayi dizisi ureteci."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
