"""
Nama    : Aziizah Oki Shofrina
NIM     : 2109106004
Kelas   : Informatika A'21
"""

print("-"*60)
print("  Data Mahasiswa  ".center(60, "|"))
print("-"*60, "\n")

biodata = {"Nama Lengkap": "",
            "NIM" : "",
            "IPK" : "",
            "Program Studi" : "",
            "Fakultas" : "",
            "No. HP" : "",
            "Alamat" : ""}

data_masuk = []

def start():
    menu = input("Apa yang ingin Anda lakukan sekarang?\
            \n1. Mengisi data mahasiswa\
            \n2. Tampilkan data mahasiswa\
            \n3. Keluar dari program\
            \n(1 / 2 / 3)\
            \n>>> ")

    if menu == "1":
        isi_data()
    elif menu == "2":
        tampilkan_data()
    elif menu == "3":
        print()
        keluar()
    else:
        print("\nPilihan tidak tersedia. \nHarap pilih (1 / 2 / 3)!\n")
        start()

def isi_data():
    bio = biodata.copy()

    nama = input("\nNama Lengkap : ")
    nim = int(input("NIM : "))
    ipk = float(input("IPK : "))
    prodi = input("Program Studi : ")
    fakultas = input("Fakultas : ")
    phone = int(input("No. HP : "))
    alamat = input("Alamat : ")

    bio["Nama Lengkap"] = nama
    bio["NIM"] = nim
    bio["IPK"] = ipk
    bio["Program Studi"] = prodi
    bio["Fakultas"] = fakultas
    bio["No. HP"] = phone
    bio["Alamat"] = alamat

    data_masuk.append(bio)

    print()
    start()

def tampilkan_data():
    num = 1
    index = 0
    jumlah = len(data_masuk)

    if jumlah == 0:
        print("\nBelum ada data mahasiswa yang dimasukkan.\nHarap masukkan data terlebih dahulu!")
    
    while num <= jumlah:
        print("\n-----------------------")
        print(f"Data Mahasiswa ke-{num}".center(23))
        print("-----------------------")

        data = data_masuk[index]
        for key, value in data.items():
            print(f"{key} : {value}")
        num += 1
        index += 1
    
    print()
    start()

def keluar():
    stop = input("Apakah Anda ingin menghentikan program? \n(Ya / Tidak) \n>>> ")
    if stop == "ya" or stop == "Ya":
        print("\nProgram dihentikan ~\n")
        exit()
    elif stop == "tidak" or stop == "Tidak":
        print("\nProgram dilanjutkan ~\n")
        start()
    else:
        print("\nHarap pilih (Ya / Tidak)!\n")
        keluar()

start()