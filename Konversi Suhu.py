"""
Nama    : Aziizah Oki Shofrina
NIM     : 2109106004
Kelas   : Informatika A'21
"""

print(f"\n{'~'*52}\n{'  KONVERSI SUHU  '.center(52, '|')}\n{'~'*52}")

def program():
    choices = input("\
        \n1. Farenheit ke Celcius\
        \n2. Kelvin ke Celcius\
        \n3. Reamur ke Celcius\
        \n(1 / 2 / 3)\
        \n>>> ")

    if choices == "1":
        print(f"\n{'*'*52}\n{'Farenheit ke Celcius'.center(52)}\n{'*'*52}")
    
        farenheit = float(input("Suhu (F) = "))
        celcius = 5/9 * (farenheit - 32)
        print(f"{farenheit} F = {celcius} C")

    elif choices == "2":
        print(f"\n{'*'*52}\n{'Kelvin ke Celcius'.center(52)}\n{'*'*52}")

        kelvin = float(input("\nSuhu (K) = "))
        celcius = kelvin - 273
        print(f"{kelvin} K = {celcius} C")

    elif choices == "3":
        print(f"\n{'*'*52}\n{'Reamur ke Celcius'.center(52)}\n{'*'*52}")

        reamur = float(input("\nSuhu (R) = "))
        celcius = 5/4 * reamur
        print(f"{reamur} R = {celcius} C")

    else:
        print("\nPilihan tidak tersedia. Harap pilih (1 / 2 / 3)!")
        program()

    ulang()

def ulang():
    repeat = input("\nApakah ingin mengulang program? \n(Ya / Tidak) \n>>> ")
    if repeat == "Ya" or repeat == "ya":
        print("\nProgram dilanjutkan ~")
        program()

    elif repeat == "Tidak" or repeat == "tidak":
        print("\nProgram dihentikan ~")

    else:
        print("\nHarap pilih (Ya / Tidak) saja!")
        ulang()
        
program()


