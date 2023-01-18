"""
kendisine gönderilen sayılardan sadece palindrom olanları toplayan
diğerlerini de bu toplamdan çıkaran ve geri döndüren kodu yaz
"""
def polinDRAM(*dram):
    toplam=0
    for sayi in dram:
        if str(sayi)==str(sayi)[::1]:
            toplam+=sayi
        else:
            toplam-=sayi
    return toplam
print(polinDRAM(10, 5, 7, 96))
