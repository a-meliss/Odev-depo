# sabit bit deseni (0x55555555), 32 bitlik bir desen
xor_key = 0x55555555

number = int(input("bir tamsayı giriniz: "))

xor_islem = number ^ xor_key

print(f"şifrelenmiş sayı: {xor_islem}")

gerialma_islem = xor_islem ^ xor_key

print(f"orijinal sayı: {gerialma_islem}")
