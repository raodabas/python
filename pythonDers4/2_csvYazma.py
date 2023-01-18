import csv

baslik=["sicaklik","nem","basinc"]
veri=[[36,45,7],[56,21,4]]

with open('sensor_veri.csv',
          'w', encoding='UTF8', newline='') as f:
    writer=csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)