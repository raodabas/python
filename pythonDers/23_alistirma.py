"""
    klavyeden girilen 5 sayıyı listeye at
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca göre sırala
    listeyi buna göre yazdıran programı yaz
"""
liste=[]
for i in range(0,6):
    liste.append(eval(input()))

def siralamFonksiyon(a):
    return a*a-10

liste.sort(key=siralamFonksiyon)
print(liste)