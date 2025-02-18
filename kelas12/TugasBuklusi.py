#Program Pengolahan Data Sampah RW
print('A2 TUGAS KELOMPOK 2 XII-8')
print('Ridho')
print('Anthony')
print('Jiwa Crypto')
print('Topaz')
print('--------------------------------------------------')
print('PROGRAM PENGOLAHAN DATA SAMPAH')
print('==================================================')

Jumlah_RT = int (input('Masukkan Jumlah RT:'))
print('==================================================')
Data_Sampah = []
Total_Sampah = 0

#Perulangan Input RT dalam 1 RW
for i in range(Jumlah_RT):
    print('Data Sampah RT-', i+1)
    Sampah_Harian = float (input('Masukkan Jumlah Total(Kg) Sampah RT :'))
    Data_Sampah.append(Sampah_Harian)
    Total_Sampah += Sampah_Harian
    Rata_Sampah = Total_Sampah / Jumlah_RT
    
#menampilkan jumlah dan rata rata sampah
print ('=================================================')
print ('Jumlah Total Sampah dari Ke', Jumlah_RT, ' RT :', Total_Sampah, 'Kg')
print ('Rata-rata Total Sampah dari Ke', Jumlah_RT, ' RT :', Rata_Sampah, 'Kg')

#Kondisi menampilkan kategori
if Rata_Sampah >0 and Rata_Sampah <30:
    ket= 'SEDIKIT'
elif Rata_Sampah >=30 and Rata_Sampah <60:
    ket= 'SEDANG'
elif Rata_Sampah >=60 and Rata_Sampah <100:
    ket= 'BANYAK'
else:
    ket= 'BANYAK SEKALI'
    
#Cetak Kondisi
print('Kategori Jumlah Penggunaan Sampah Hari Ini :',ket)
print ('================================================')
