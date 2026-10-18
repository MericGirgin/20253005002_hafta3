from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_metni_dolu():
    sonuc = envanter_metni(credits=True, engines=False, copilot=True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_bos():
    sonuc = envanter_metni(credits=False, engines=False, copilot=False)
    assert sonuc == ""


def test_hedef_menusu():
    hedefler = ["centauri", "sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen