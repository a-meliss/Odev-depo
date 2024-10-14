#kullanıcıdan onluk tamsayı girişi al
tamsayı_gir = int(input("lütfen bir tamsayı giriniz: "))

#bin() ile sayıyı ikilik sisteme çeviriyoruz
binari_donusum = bin(tamsayı_gir)

# bin çıktısı '0b' önceki ile gelir, bunu çıkartıyoruz
print(f"girdiğiniz sayının ikilik (binary karşılığı: ) {binari_donusum[2:]}")