parite="AVAXUSDT"  # input("parite giriniz :")
bas_tarih="2023-04-07"  #  input("başlangıç tarihi :")
bit_tarih="2023-04-08"  # input("bitiş tarihi :")

sorgu="SELECT*FROM parite WHERE " \
      "(otime BETWEEN '"+bas_tarih+"' " \
      "AND '"+bit_tarih+"') " \
      "AND parite='"+parite+"'"
cursor.execute(sorgu)
sonuc=cursor.fetchall()
liste_x=[]
liste_y=[]
for mum in sonuc:
    #print(mum)
    #print(mum[1])
    liste_y.append(mum[6])
    liste_x.append(mum[2])
plt.plot(liste_x, liste_y)
plt.show()
bag.close()