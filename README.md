# İleri Python Programlama – Hafta 3 Lab Ödevi
**Fonksiyonlar Derinlemesine**

- **Öğrenci:** Ahmet Meriç Girgin
- **Öğrenci Numarası:** 20253005002
- **Ders:** İleri Python Programlama
- **Öğretim Üyesi:** Dr. Öğr. Üyesi Murat Emeç

---

## Görevler ve Yapılan İşler

### 1. Görev 1 – Saf Fonksiyonlar Çıkar (20 Puan)
- `uzay_oyunu/oyun.py` içinde `envanter_metni` ve `hedef_menusu` saf fonksiyonları yazıldı.
- `print` yapılmadan metin `return` edildi.
- `tests/test_fonksiyonlar.py` birim testleri hazırlandı.

### 2. Görev 2 – Esnek Parametreler (15 Puan)
- `uzay_oyunu/kayit.py` içinde `gorev_kaydi(baslik, *adimlar, oncelik="normal", **ekler)` fonksiyonu yazıldı.
- `oncelik` keyword-only parametre olarak tanımlandı.
- `main` bloğunda doğrudan çağrı ve `*` ile `**` unpacking çağrıları örneklendirildi.

### 3. Görev 3 – Galaksiyi Veri Dosyasından Kur (25 Puan)
- Oyun haritası `uzay_oyunu/galaksi.json` dosyasına taşındı.
- `uzay_oyunu/galaksi.py` içinde `galaksi_kur` fonksiyonu yazıldı (başlangıç kontrolü ve `kwargs.get('yakit', 50)`).
- `travel()` içindeki hedefler dinamik olarak `galaksi["baglantilar"]` üzerinden çekildi.

### 4. Görev 4 – Tuzaklar ve Kapsam (20 Puan)
- `tests/test_tuzaklar.py` içinde `depo=[]` mutable default argument tuzağını gösteren test ve `None` kalıbıyla düzeltilmiş fonksiyon yazıldı.
- `kapsam.md` dosyasında LEGB kuralı ve `UnboundLocalError` detaylıca açıklandı.

### 5. Görev 5 – Closure ve Lambda (20 Puan) + Bonus (+10 Puan)
- `uzay_oyunu/araclar.py` içinde:
  - `hamle_sayaci()`: `nonlocal` kullanan closure sayaç yazıldı ve `travel()` içine entegre edildi.
  - `en_bagli_gezegenler(galaksi)`: `sorted()` ve `key=lambda` ile gezegenler bağlantı sayısına ve alfabetik sıraya göre sıralandı.
  - `sure_olc(fonksiyon)`: Bonus olarak çalışma süresini ölçen decorator yazıldı.

---

## Testleri Çalıştırma

Tüm testleri çalıştırmak için:
```bash
uv run pytest
```
