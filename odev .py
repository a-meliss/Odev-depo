import math
#kullanıcıdan yarıçapı ondalıklı sayı olarak alma
hesap = float(input("yarıçapı giriniz:"))

#çevre ve alan hesaplama
cevre = 2 * math.pi * hesap 
alan =  math.pi * hesap ** 2

#sonuçları ekrana yazdırma
print(f"dairenin çevresi: {cevre}")
print(f"dairenin alanı: {alan}")

