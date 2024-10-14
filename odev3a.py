#kullanıcıdan karakteri ve sayıyı alma
char = input("bir karakter giriniz:")
count = int(input("bir tamsayı giriniz:"))

#sayıyı negatif girerse reddetme
if(count<0):print("malesef negatif kez tekrarlayamıyoruz:)")

 #pozitif girerse yapılacak işlem
result = char * count

#sonucu ekrana verme
print(result)