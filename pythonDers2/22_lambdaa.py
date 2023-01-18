def fonksiyon(l):
    return lambda a:a*l
kat_al=fonksiyon(6)
print(kat_al(7))
kat_al=fonksiyon(6)
print(kat_al(6))