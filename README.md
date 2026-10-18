# İleri Python Programlama – Lab Ödevleri

- **Öğrenci:** Ahmet Meriç Girgin
- **Öğrenci Numarası:** 20253005002
- **Ders:** İleri Python Programlama
- **Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç

---

## Hafta 4: Üreteçler ve functools

### Görev 4: Önbellekli Rota Sayacı Performans Ölçümü (adim = 20)

`rota_sayisi("dünya", 20)` çağrısı için `@lru_cache` önbellek performans karşılaştırması:

- **Önbelleksiz Sürüm Süresi:** `7.318025` saniye
- **Önbellekli Sürüm Süresi:** `0.000116` saniye (~63.000 kat daha hızlı)
- **cache_info() Çıktısı:** `CacheInfo(hits=92, misses=98, maxsize=None, currsize=98)`

---

## Hafta 3: Fonksiyonlar Derinlemesine

### Görevler ve Yapılan İşler
1. **Görev 1 (Saf Fonksiyonlar):** `envanter_metni` ve `hedef_menusu` saf fonksiyonları yazıldı.
2. **Görev 2 (Esnek Parametreler):** `gorev_kaydi` fonksiyonunda `*adimlar`, keyword-only `oncelik` ve `**ekler` uygulandı.
3. **Görev 3 (Galaksi JSON):** Harita `galaksi.json` dosyasına taşındı ve `galaksi_kur` fonksiyonu yazıldı.
4. **Görev 4 (Tuzaklar ve Kapsam):** `depo=[]` tuzağı test edildi ve `None` kalıbıyla düzeltildi; `kapsam.md` raporu hazırlandı.
5. **Görev 5 (Closure & Lambda):** `hamle_sayaci` closure'ı, `key=lambda` ile sıralama ve `sure_olc` decorator'ü eklendi.

---

## Testleri Çalıştırma

Tüm testleri çalıştırmak için:
```bash
uv run pytest
```
