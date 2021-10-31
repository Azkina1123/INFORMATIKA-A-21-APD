"""
NAMA    : AZIIZAH OKI SHOFRINA
NIM     : 2109106004
KELAS   : INFORMATIKA A'21
"""

food_dict = {"Bakso" : 10000, 
        "Mie Ayam" : 13000, 
        "Seblak" : 15000, 
        "Gulai" : 15000, 
        "Rawon" : 15000, 
        "Sayur Sop" : 13000}

drink_dict = {"Air Putih" : 3000, 
         "Es Teh" : 5000, 
         "Es Jeruk" : 8000, 
         "Es Campur" : 10000, 
         "Jus Buah" : 12000}

food_list = ["Bakso", "Mie Ayam", "Seblak", "Gulai", "Rawon", "Sayur Sop"]
drink_list = ["Air Putih", "Es Teh", "Es Jeruk", "Es Campur", "Jus Buah"]

food_dipesan = []
drink_dipesan = []


import datetime as dt
from os import system as st

def clear():
    st("cls")

def cafe():
    clear()
    print("-------------------------------".center(50))
    print("  Selamat datang di K-Cafe Lokal  ".center(50, ":"))
    print("-------------------------------".center(50))
    print("\nMakanan :\
            \n1). Bakso \t[ Rp10.000 ]\
            \n2). Mie Ayam \t[ Rp13.000 ]\
            \n3). Seblak \t[ Rp15.000 ]  \
            \n4). Gulai \t[ Rp15.000 ] \
            \n5). Rawon \t[ Rp15.000 ] \
            \n6). Sayur Sop \t[ Rp13.000 ]")

    print("\nMinuman :\
        \n1). Air Putih \t[ Rp3.000 ]\
        \n2). Es Teh \t[ Rp5.000 ]\
        \n3). Es Jeruk \t[ Rp8.000 ]\
        \n4). Es Campur \t[ Rp10.000 ]\
        \n5). Jus Buah \t[ Rp12.000 ]")


    print("\nDISKON!!!\
            \n3 Minuman/pembelian\t[ 10% ]\
            \n2 Makanan/pembelian\t[ 5% ]\
            \nPembayaran E-money\t[ 5% ]\
            \nWeekend (Sabtu-Minggu)\t[ 5% ]\
            \nWeekdays (Senin-Jumat)\t[ 10% ]\n")

    tanggal = dt.date.today()
    hari_ini = tanggal.strftime("%A")
    print(f"   {hari_ini}, {tanggal}   ".center(50, "~"))

def pesan_makanan():
    pesan = input("\nApakah Anda ingin memesan makanan? \n(Ya / Tidak) \n>>> ")
    if pesan.casefold() == "ya" or\
        pesan.casefold() == "yes" or\
        pesan.casefold() == "y" or\
        pesan.casefold() == "ok" or\
        pesan.casefold() ==" k":
        cafe()
        makanan_dipesan()

    elif pesan.casefold() == "tidak" or\
        pesan.casefold() == "no" or\
        pesan.casefold() == "n" or\
        pesan.casefold() == "g" or\
        pesan.casefold() == "gak" or\
        pesan.casefold() == "skip":
        cafe()
        pesan_minuman()

    else:
        cafe()
        print("\nHarap pilih (Ya / Tidak)!")
        pesan_makanan()
        
    
def pesan_minuman():
    pesan = input("\nApakah Anda ingin memesan minuman? \n(Ya / Tidak) \n>>> ")
    if pesan.casefold() == "ya" or\
        pesan.casefold() == "yes" or\
        pesan.casefold() == "y" or\
        pesan.casefold() == "ok" or\
        pesan.casefold() ==" k":
        cafe()
        minuman_dipesan()
    elif pesan.casefold() == "tidak" or\
        pesan.casefold() == "no" or\
        pesan.casefold() == "n" or\
        pesan.casefold() == "g" or\
        pesan.casefold() == "gak" or\
        pesan.casefold() == "skip":
        cafe()
        struk()
    else:
        cafe()
        print("Harap pilih (Ya / Tidak!)")
        pesan_minuman()


def pesan_lagi():
    lagi = input("\nApakah ingin memesan lagi? \n(Ya / Tidak) \n>>> ")
    if lagi.casefold() == "ya" or\
        lagi.casefold() == "yes" or\
        lagi.casefold() == "y" or\
        lagi.casefold() == "ok" or\
        lagi.casefold() ==" k":
        cafe()
        makanan_dipesan()
    elif lagi.casefold() == "tidak" or\
        lagi.casefold() == "no" or\
        lagi.casefold() == "n" or\
        lagi.casefold() == "g" or\
        lagi.casefold() == "gak" or\
        lagi.casefold() == "skip":
        cafe()
        pass
    else:
        cafe()
        print("Harap pilih (Ya / Tidak!)")
        pesan_lagi()
    

def makanan_dipesan():
    
    makanan = input("\nPilih nomor pada menu makanan. \n>>> ")
    if makanan ==  "1" or\
        makanan == "2" or\
        makanan == "3" or\
        makanan == "4" or\
        makanan == "5" or\
        makanan == "6":
        cafe()
            
        index = int(makanan) - 1
        dipesan = food_list[index]
        food_dipesan.append(dipesan)
        pesan_lagi()

    else:
        cafe()
        print("\nMenu tidak tersedia. \nHarap pilih kembali!")
        makanan_dipesan()

    pesan_minuman()


def minuman_dipesan():
    
    minuman = input("\nPilih nomor pada menu minuman.\n>>> ")
    if minuman ==  "1" or\
        minuman == "2" or\
        minuman == "3" or\
        minuman == "4" or\
        minuman == "5":
        cafe()
            
        index = int(minuman) - 1
        dipesan = drink_list[index]
        drink_dipesan.append(dipesan)

        pesan_lagi()

    else:
        cafe()
        print("\nMenu tidak tersedia. \nHarap pilih kembali!")
        minuman_dipesan()
    

def struk():
    print(f"\nSTRUK PESANAN \n{'='*13}")

    if len(food_dipesan) != 0 or len(drink_dipesan) != 0:
        jumlah_makanan = len(food_dipesan)
        num_f = 1
        index_f = 0
        harga_makanan = 0
        if len(food_dipesan) != 0:
            print("\nMakanan : ")
            while num_f <= jumlah_makanan:
                dipesan = food_dipesan[index_f]
                print(f"{num_f}. {dipesan}\t\t Rp{food_dict[dipesan]}")
                num_f += 1
                index_f += 1
                harga_makanan += food_dict[dipesan]
            print(f"----------------------------------- +\n   \t\t\t Rp{harga_makanan}")

            if jumlah_makanan >= 2:
                harga_makanan = harga_makanan - (harga_makanan * 0.05)
                print(f"Anda mendapat diskon 5%! \nHarga setelah diskon = {harga_makanan}")

        jumlah_minuman = len(drink_dipesan)
        num_d = 1
        index_d = 0
        harga_minuman = 0
        if len(drink_dipesan) != 0:
            print("\nMinuman : ")
            while num_d <= jumlah_minuman:
                dipesan = drink_dipesan[index_d]
                print(f"{num_d}. {dipesan}\t\t Rp{drink_dict[dipesan]}")
                num_d += 1
                index_d += 1
                harga_minuman += drink_dict[dipesan]
            print(f"----------------------------------- +\n   \t\t\t Rp{harga_minuman}")

            if jumlah_minuman >= 3:
                harga_minuman = harga_minuman - (harga_minuman * 0.1)
                print(f"Anda mendapat diskon 10%! \nHarga setelah diskon = Rp{harga_minuman}")

        total_harga = harga_makanan + harga_minuman
        print(f"\nTotal harga yang harus dibayar = Rp{int(total_harga)}")

        pembayaran = input("\nApakah Anda ingin membayar dengan E-money? \n(Ya / Tidak) \n>>> ")
        if pembayaran == "ya" or pembayaran == "Ya":
            print(f"\nKarena Anda membayar dengan E-money, \nAnda mendapat diskon 5%!")
            if dt.datetime.today().weekday() < 5:
                print(f"\nHari ini adalah weekdays! \nAnda mendapat diskon 10% ~")
                total_harga = total_harga - (total_harga * (0.05 + 0.1) )
            else:
                print("\nHari ini adalah weekend! \nAnda mendapat diskon 5% ~")
                total_harga = total_harga - (total_harga * (0.05 + 0.05))
        else:
            if dt.datetime.today().weekday() < 5:
                total_harga = total_harga - (total_harga * 0.1)
                print(f"\nHari ini adalah weekdays! \nAnda mendapat diskon 10% ~")
            else:
                total_harga = total_harga - (total_harga * 0.05)
                print("\nHari ini adalah weekend! \nAnda mendapat diskon 5% ~")

        print(f"\nTotal harga yang harus dibayar = Rp{total_harga}")

    else:
        print("\nAnda tidak memesan apa-apa.")

    next = input("\nLanjutkan => ")
    end()

def end():
    cafe()
    ulang = input("\nApakah Anda ingin melakukan pembelian di cafe lagi? \n(Ya / Tidak) \n>>> ")
    if ulang.casefold() == "ya" or\
        ulang.casefold() == "yes" or\
        ulang.casefold() == "y" or\
        ulang.casefold() == "ok" or\
        ulang.casefold() ==" k":
        cafe()
        pesan_makanan()
    elif ulang.casefold() == "tidak" or\
        ulang.casefold() == "no" or\
        ulang.casefold() == "n" or\
        ulang.casefold() == "g" or\
        ulang.casefold() == "gak" or\
        ulang.casefold() == "skip":
        cafe()
        print("\nTerima kasih telah mengunjungi K-Cafe Lokal ~")
        selesai = input("")

        import sys
        sys.exit()

    else:
        cafe()
        print("Harap masukkan (\nYa / Tidak)!")
        end()


cafe()
pesan_makanan()
struk()



