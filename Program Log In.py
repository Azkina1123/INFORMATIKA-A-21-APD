"""
NAMA    : AZIIZAH OKI SHOFRINA
NIM     : 2109106004
KELAS   : INFORMATIKA A'21
"""

admin = {"Username" : "Azkina1123",
        "Password" : "AyamGurih"}

username_masuk = []
password_masuk = []

import sys
import getpass as gp
from os import system as st

def clear():
    st("cls")

def start():
    # TITLE
    clear()
    print("---------------".center(40))
    print("  Program Log In  ".center(40, "|"))
    print("---------------".center(40), "\n")
    while True:
        # PRROGRAM
        print("Selamat datang!")
        opsi = input("Apa yang ingin Anda lakukan?\
            \n1). Log In\
            \n2). Sign Up\
            \n3). Keluar dari Program\
            \n(1 / 2 / 3)\
            \n>>> ")

        if opsi == "1":
            # LOG IN
            hitung_uname = 0
            clear()

            while True:
                # INPUT USERNAME
                print(f"{'-'*10}\n{' Log In '.center(10)}\n{'-'*10}")
                
                username = input("\nUsername : ")
                hitung_uname += 1

                if username in username_masuk:
                    # REGULAR ACCOUNT -------------------------------------------------------------
                   
                    index_uname = username_masuk.index(username)
                    index_pw = index_uname
                    hitung_pw = 0

                    while True:
                        # INPUT PASSWORD (REGULAR)
                    
                        hitung_pw += 1
                        password = gp.getpass("Password : ")

                        if password in password_masuk[index_pw] :
                            clear()

                            print(f"Selamat datang, {username}!\n")

                            while True:
                                # MASUK REGULAR
                                do = input("Apa yang ingin Anda lakukan sekarang?\
                                        \n1). Edit Akun\
                                        \n2). Log Out\
                                        \n3). Keluar dari Program\
                                        \n>>> ")
                                
                                if do == "1":
                                    # EDIT AKUN REGULAR
                                    clear()

                                    print(f"{'-'*15}\n{' Edit Akun '.center(15)}\n{'-'*15}")
                                    
                                    print("\nJika tidak ingin mengedit, ketik 'skip'!")
                                    edit_uname = input(f"Username : {username} --> ")
                                    if edit_uname == "Skip" or\
                                            edit_uname == "skip":
                                            pass
                                    else:
                                        username_masuk[index_uname] = edit_uname
                                        
                                    edit_pw = input(f"Password : {password} --> ")
                                    if edit_pw == "Skip" or\
                                        edit_pw == "skip":
                                        pass
                                    else:
                                        password_masuk[index_pw] = edit_pw

                                    print("\nAkun Anda telah diperbarui!")
                                    print(f"Username : {username_masuk[index_uname]}")
                                    print(f"Password : {password_masuk[index_pw]}")

                                    back = input("\nKembali => ")

                                    clear()

                                elif do == "2":
                                    # LOG OUT
                                    clear()
                                    
                                    print("\nAnda telah log out ~")

                                    back = input("\nPergi ke lobi => ")

                                    start()

                                elif do == "3":
                                    # KELUAR
                                    clear()

                                    while True:
                                        stop = input("\nApakah Anda yakin ingin keluar dari program? \n (Ya/ Tidak)\n>>> ")
                                        if stop == "Ya" or stop == "ya":
                                            print("\nSelamat tinggal ~")
                                            input("Keluar => ")
                                            sys.exit()
                                        elif stop == "Tidak" or stop == "tidak":
                                            clear()
                                            print("Selamat datang kembali ~\n")
                                            break
                                        else:
                                            clear()
                                            print("\nHarap masukkan (Ya / Tidak)!")
                                            continue

                                else:
                                    # OPSI TIDAK TERSEDIA
                                    clear()

                                    print("\nOpsi tidak tersedia. Harap pilih kembali.")
                                    continue

                        elif hitung_pw >= 3:
                            # GAGAL LOG IN (REGULAR)
                            clear()
                            print("Login gagal! \nPastikan Anda adalah benar pemilik akun!")
                            back = input("\nPergi ke lobi => ")
                            start()

                        else:
                            # PASSWORD SALAH (REGULAR)
                            clear()

                            print("Password salah! \nHarap masukkan kembali.\n")
                            print(f"{'-'*10}\n{' Log In '.center(10)}\n{'-'*10}")
                            print(f"\nUsername : {username}")
                            continue

                elif username == admin["Username"]:
                    # ADMIN ACCOUNT -------------------------------------------------------------
                    hitung_pw = 0

                    while True:
                        # INPUT PASSWORD (ADMIN)
                    
                        hitung_pw += 1
                        password = gp.getpass("Password : ")
                        
                        if password == admin["Password"]:
                            clear()

                            while True:
                                print(f"Selamat datang, {username}! \nSekarang Anda berada dalam mode admin.\n")
                                # MASUK ADMIN
                                do = input("Apa yang ingin Anda lakukan sekarang?\
                                        \n1). Edit Akun Admin\
                                        \n2). Tampilkan Akun yang Terdaftar\
                                        \n3). Log Out\
                                        \n4). Keluar dari Program\
                                        \n>>> ")
                                
                                if do == "1":
                                    # EDIT AKUN ADMIN
                                    clear()

                                    print("\nJika tidak ingin mengedit, ketik 'skip'!")
                                    for key, value in admin.items():
                                        edit = input(f"{key} : {value} --> ")
                                        
                                        if edit == "Skip" or edit == "skip":
                                            pass
                                        else:
                                            admin[key] = edit

                                    print("\nAkun Anda telah diperbarui!")
                                    for key, value in admin.items():
                                        print(f"{key} : {value}")

                                    back = input("\nKembali => ")

                                    clear()
                                
                                elif do == "2":
                                    # DATA AKUN TERDAFTAR
                                    clear()

                                    jumlah = len(username_masuk)
                                    print(f"Terdapat {jumlah} akun yang terdaftar dalam program!")
                                    index = 0
                                    num = 1

                                    while num <= jumlah:
                                        print(f"{num}. {username_masuk[index]}")
                                        num += 1
                                        index += 1

                                    back = input("\nKembali => ")

                                    clear()

                                elif do == "3":
                                    # LOG OUT (ADMIN)
                                    clear()

                                    print("\nAnda telah log out ~")
                                    back = input("\nPergi ke lobi => ")

                                    start()

                                elif do == "4":
                                    # KELUAR 
                                    clear()

                                    while True:
                                        stop = input("\nApakah Anda yakin ingin keluar dari program? \n (Ya/ Tidak)\n>>> ")
                                        if stop == "Ya" or stop == "ya":
                                            print("\nSelamat tinggal ~")
                                            input("Keluar => ")
                                            sys.exit()
                                        elif stop == "Tidak" or stop == "tidak":
                                            clear()
                                            print("Selamat datang kembali ~\n")
                                            break
                                        else:
                                            clear()
                                            print("\nHarap masukkan (Ya / Tidak)!")
                                            continue
                                else:
                                    clear()
                                    print("\nOpsi tidak tersedia. Harap pilih kembali.\n")
                                    continue

                        elif hitung_pw >= 3:
                            # GAGAL LOG IN (ADMIN)
                            clear()
                            
                            print("Login gagal! \nPastikan Anda adalah benar pemilik akun!\n")
                            back = input("\nPergi ke lobi => ")
                            start()

                        else:
                            # PASSWORD SALAH (ADMIN)
                            clear()

                            print("Password salah! \nHarap masukkan kembali.\n")
                            print(f"{'-'*10}\n{' Log In '.center(10)}\n{'-'*10}")
                            print(f"\nUsername : {username}")
                            continue
                    
                
                elif hitung_uname == 3:
                    # GAGAL LOG IN
                    clear()

                    print("\nLogin gagal!\nPastikan akun Anda telah terdaftar sebelumnya!\n")
                    break

                else:
                    # USERNAME SALAH
                    clear()
                    print("\nUsername salah! \nHarap masukkan kembali.\n")
                    continue

        elif opsi == "2":
            # SIGN UP
            clear()

            print(f"{'-'*11}\n{' Sign Up '.center(11)}\n{'-'*11}")

            input_uname = input("\nUsername : ")
            input_pw = gp.getpass("Password : ")

            username_masuk.append(input_uname)
            password_masuk.append(input_pw)

            print("\nSelamat, Anda telah berhasil membuat akun!\nSilahkan kembali ke lobi untuk log in.")

            back = input("\nPergi ke lobi => ")

            clear()
        elif opsi == "3":
            # KELUAR
 
            clear()
            while True:
                stop = input("\nApakah Anda yakin ingin keluar dari program? \n (Ya/ Tidak)\n>>> ")
                if stop == "Ya" or stop == "ya":
                    print("\nSelamat tinggal ~")
                    input("Keluar => ")
                    sys.exit()
                elif stop == "Tidak" or stop == "tidak":
                    clear()
                    print("Selamat datang kembali ~\n")
                    break
                else:
                    clear()
                    print("\nHarap masukkan (Ya / Tidak)!")
                    continue
        else:
            # OPSI TIDAK TERSEDIA
            clear()
            print("\nOpsi tidak tersedia. Harap pilih kembali.\n")
            continue

start()