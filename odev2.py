import math
#kullanıcıdan dik uzunlukları alma
a = float(input("ilk kenarin uzunluğunu giriniz:"))
b = float(input("ikinci kenarin uzunluğunu giriniz:"))

#hipotenüs hesaplama
c = math.sqrt(a**2 + b**2)

#sonucu ekrana yazdırma 
print (f"hipotenus uzunluğu: {c}")

print(f"cevre: {a+b+c}")
print(f"alan: {a*b/2}")