liste= ["ayca", "fatma", "hayriye"]
liste.sort()
print(liste)

liste.reverse()
print(liste)

def fonksiyon(m):
    return abs(m-50)

sayi=[100, 52, 89, 36]
sayi.sort(key=fonksiyon)
print(sayi)