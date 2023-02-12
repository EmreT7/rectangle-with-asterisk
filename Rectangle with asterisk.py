# Dikdörtgen oluşturma

W = int(input("Genişlik: "))
H = int(input("Yükseklik: "))

ust_alt_satir = ""
for i in range(W):
    ust_alt_satir += "*"

ara_satir = ""
for i in range(W):
    if i == 0 or i == W - 1:
        ara_satir += "*"
    else:
        ara_satir += " "

for i in range(H):
    if i == 0 or i == H - 1:
        print(ust_alt_satir)
    else:
        print(ara_satir)