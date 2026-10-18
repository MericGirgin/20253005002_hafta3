import time
from collections.abc import Generator


def zamanlayici(aralik: float) -> Generator[float, None, None]:
    """Belirli zaman araliklariyla sinyal ureten uretec."""
    son_zaman = time.perf_counter()
    while True:
        simdi = time.perf_counter()
        if simdi - son_zaman >= aralik:
            yield simdi
            son_zaman = simdi


def tik_tak_programi(toplam_sure: float = 10.0):
    """10 saniye boyunca her 2 sn'de 'tik', her 5 sn'de 'tak' yazdirir."""
    tik = zamanlayici(2.0)
    tak = zamanlayici(5.0)

    baslangic = time.perf_counter()
    son_tik = baslangic
    son_tak = baslangic

    while time.perf_counter() - baslangic < toplam_sure:
        simdi = time.perf_counter()
        if simdi - son_tik >= 2.0:
            print("tik")
            son_tik = simdi
        if simdi - son_tak >= 5.0:
            print("tak")
            son_tak = simdi


# ACIKLAMA:
# Neden bu bir "mesgul bekleme" (busy-waiting)?
# Dongu icerisinde hicbir bekleme veya duraklatma yapilmadan surekli
# time.perf_counter() kontrol edilir. Bu durum islemciyi (CPU) surekli %100
# kapasitede calistirarak gereksiz yere enerji ve kaynak tuketir.
#
# time.sleep ile farki:
# time.sleep() isletim sistemine su talimati verir: "Bu thread'i su sure boyunca uyut".
# Isletim sistemi bu sure zarfinda CPU'yu baska program ve sureclere devreder;
# islemci bosa donmez, enerji tasarrufu saglanir.


if __name__ == "__main__":
    tik_tak_programi(10.0)
