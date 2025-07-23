import random

print("Taş-Kağıt-Makas Oyununa Hoş Geldin!")
print("Seçenekler: tas, kagit, makas")

# Oyuncunun seçimi
oyuncu_secim = input("Seçiminizi yazın: ").lower()

# Bilgisayarın seçimi
secenekler = ["tas", "kagit", "makas"]
bilgisayar_secim = random.choice(secenekler)
print("Bilgisayarın seçimi:", bilgisayar_secim)

# Kazananı belirle
if oyuncu_secim == bilgisayar_secim:
    print("Berabere!")
elif (oyuncu_secim == "tas" and bilgisayar_secim == "makas") or \
     (oyuncu_secim == "kagit" and bilgisayar_secim == "tas") or \
     (oyuncu_secim == "makas" and bilgisayar_secim == "kagit"):
    print("Kazandın!")
elif (oyuncu_secim == "tas" and bilgisayar_secim == "kagit") or \
     (oyuncu_secim == "kagit" and bilgisayar_secim == "makas") or \
     (oyuncu_secim == "makas" and bilgisayar_secim == "tas"):
    print("Kaybettin!")
else:
    print("Hatalı Cevap Tekrar Dene.")