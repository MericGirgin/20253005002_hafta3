# Kapsam (Scope) ve LEGB Kuralı İncelemesi

Bu raporda Python'ın değişken arama kuralı olan **LEGB (Local, Enclosing, Global, Built-in)** ve derste işlenen 3 kapsam örneği açıklanmıştır.

---

## 1. Örnek: Global Değişken Okuma

### Kod
```python
x = 10

def f():
    print(x)

f()
```

- **Tahmin:** `10`
- **Gerçek Sonuç:** `10`
- **Nedeni (LEGB):**
  Fonksiyon çalıştırıldığında `f()` yerelinde (Local) `x` bulunamaz. Bir üst kapsayıcı fonksiyon (Enclosing) olmadığı için doğrudan **Global** kapsama bakılır. Globalde tanımlı olan `x = 10` değeri okunur ve ekrana yazdırılır.

---

## 2. Örnek: UnboundLocalError Tuzağı

### Kod
```python
x = 10

def f():
    print(x)
    x = 20

f()
```

- **Tahmin:** `UnboundLocalError`
- **Gerçek Sonuç:** `UnboundLocalError: local variable 'x' referenced before assignment`
- **Nedeni:**
  Python bir fonksiyon derlenirken fonksiyon gövdesinde atama yapılıp yapılmadığına bakar (`x = 20`).
  - Gövdede atamayı gördüğü anda o değişkeni fonksiyonun tamamı için **Local (yerel)** olarak etiketler.
  - İlk satırdaki `print(x)` çalıştığında, `x` yerel etiketlendiği için Python artık globaldeki `10` değerine bakmaz.
  - Yerel `x` ise henüz o satırda bir değere bağlanmamıştır (assignment henüz gerçekleşmemiştir). Bu yüzden Python `UnboundLocalError` hatası fırlatır.

---

## 3. Örnek: Enclosing Kapsam ve `nonlocal`

### Kod
```python
def dis():
    sayac = 5

    def ic():
        nonlocal sayac
        sayac += 1
        return sayac

    return ic

say = dis()
print(say())
print(say())
```

- **Tahmin:** `6` ve `7`
- **Gerçek Sonuç:** `6` ve `7`
- **Nedeni:**
  İçteki fonksiyon dış fonksiyonun yerel değişkenini değiştirmek (`sayac += 1`) istediğinde:
  - Eğer `nonlocal` yazılmazsa, `sayac = sayac + 1` ifadesindeki atama nedeniyle Python `sayac`'ı iç fonksiyonun yerel değişkeni sayar ve 2. örnekteki gibi `UnboundLocalError` verir.
  - `nonlocal sayac` yazıldığında değişkenin **Enclosing** (bir üst kapsayıcı) fonksiyondan geldiği belirtilir ve her çağrıda durumu güncellenerek korunur (Closure).
