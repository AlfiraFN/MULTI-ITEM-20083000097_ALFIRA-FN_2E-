# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 23:03:48 2021

@author: aulia
"""

ulang="y"
while ulang=="y" or ulang =="Y":
    #Siapkan variabel
    print("===========================")
    print(" APLIKASI 5a")
    print(" CEK KELULUSAN")
    print("===========================")
    m=1
    #Cek nilai, jika n > 60, nilai antara 0-100 sts Lulus selain itu Ulang
    while m>0 and m<=100:
        n = input("Masukan Nilai = ")
        m = int(n)
        if m>=0 and m<=100:
            if m>60:
                sts = "Lulus"
            else:
                sts = "Ulang"
            print (sts)

            ulang=input("Ingin Mengecek Kembali? y/t =")
            if ulang=="t" or ulang =="T":
                break
        
        else: 
            pesan="Masukan Kembali Angka Usia Antara 0-100"
            print(pesan)
            print()