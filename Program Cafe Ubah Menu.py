"""
NAMA    : AZIIZAH OKI SHOFRINA
NIM     : 2109106004
KELAS   : INFORMATIKA A'21
"""

foodCategories = ["Makanan Kuah", "Makanan Goreng"]
foodMenus = [["Bakso", "Mie Ayam", "Seblak", "Gulai", "Rawon"],
                ["Nasi Goreng Ayam", "Nasi Goreng Seafood", "Mie Goreng"]]
foodPrices = [[10000, 13000, 15000, 15000, 15000],
                [12000, 15000, 12000]]

drinksCategories = ["Air Mineral", "Minuman Es", "Jus Buah"]
drinksMenus = [["Aqua", "Ades"],
                ["Es Teh", "Es Jeruk", "Es Campur"],
                ["Jus Alpukat", "Jus Apel", "Jus Mangga"]]
drinksPrices = [[3000, 3500],
                [5000, 8000, 10000],
                [12000, 12000, 12000]]

orderedFood = []
orderedFoodPrices = []

orderedDrinks = []
orderedDrinksPrices = []

import datetime as dt
from os import system as st
import getpass as gp
import sys
from typing import OrderedDict

# BERSIHKAN HALAMAN
def clear():
    st("cls")

# PILIH MODE
def welcome(warning): #NICE!
    clear()
    print("\n\n\n\n\n\n")
    print("  Selamat datang di K-Cafe Lokal!  ".center(100))

    print("\n\t ",f"{warning}".center(100), "\n")

    print("Pilih opsi berikut.".center(100), "\n")
    print("(1) Pemilik Cafe     (2) Pelanggan Cafe".center(100))

    mode = input("\n\t\t\t\t>>> ")

    if mode == "1":
        logIn("")

    elif mode == "2":
        customerMode()

    elif mode == "":
        welcome("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")

    else:
        welcome("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

unameCounter = [1]
pwCounter = [1]
# LOG IN (PEMILIK KAFE)
def logIn(warning): #NICE!
    clear()
    print("\n\n\n\n\n")

    print("Log In Pemilik Cafe".center(100))

    print("\n\t ", f"{warning}".center(100), "\n")

    # input username
    username = input("\t\t\t\t       Username\t: ")

    # jika username benar
    if username == "Keken":
        unameCounter.clear()
        unameCounter.append(1)

        # input password
        password = gp.getpass("\t\t\t\t       Password\t: ")

        # jika password benar
        if password == "123":
            pwCounter.clear()
            pwCounter.append(1)

            ownerMode("")

        # jika password salah 3 kali
        elif len(pwCounter) % 3 == 0:
            kickedOut()

        # jika password salah
        else:
            pwCounter.append(1)
            logIn("\033[1;31;40m Password salah! \033[0;37;40m")
            
    # jika username salah 3 kali
    elif len(unameCounter) % 3 == 0:
        kickedOut()

    # jika username salah
    else:
        unameCounter.append(1)
        logIn("\033[1;31;40m Username salah! \033[0;37;40m")
        
# MENU EDIT MENU
def ownerMode(warning):
    clear()
    print("\n\n\n\n\n\n")

    print("Selamat datang, Keken!".center(100))
    print("(Ketik '0' untuk log out)".center(100))
    print("\n\t ",f"{warning}".center(100), "\n")
    print("[1] Tambahkan Menu    [2] Ganti Menu    [3] Hapus Menu".center(100))
    opsi = input("\n\t\t\t\t>>> ")
    
    if opsi == "1":
        addMenus("")
    elif opsi == "2":
        replaceMenus("")
    elif opsi == "3":
        deleteMenus("")
    elif opsi == "0":
        welcome("")
    elif opsi == "":
        ownerMode("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")
    else:
        ownerMode("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")



# MENU TERDAFTAR
def printMenu(categoriesList, menusList, pricesList):
    indexMenus = 0
    indexPrices = 0
    indexCategories = 0
    for category in categoriesList:
        num = 0
        indexPrice = 0
        print(f"\tMenu {category}")

        if indexCategories == len(menusList):
            break

        else:
        
            for menu in menusList[indexMenus]:
                num += 1
                print(f"\t({num}) {menu} --- Rp{pricesList[indexMenus][indexPrice]}")
                indexPrice += 1

        print()
        indexMenus += 1
        indexPrices += 1
        indexCategories += 1
# TAMPILKAN MENU MAKANAN
def printFood():
    printMenu(foodCategories, foodMenus, foodPrices)
# TAMPILKAN MENU MINUMAN
def printDrinks():
    printMenu(drinksCategories, drinksMenus, drinksPrices)
            


# MENU TAMBAHKAN MENU
def addMenus(warning):
    clear()
    print("\n\n\n\n\n\n")
    print("  Tambahkan Menu Baru  ".center(100))

    print("\n\t ",f"{warning}".center(100), "\n")

    print("Pilih opsi berikut.".center(100), "\n")
    print("(A) Makanan     (B) Minuman".center(100))

    menu = input("\n\t\t\t\t>>> ")
    
    if menu.casefold() == "a":
        addFood()
    elif menu.casefold() == "b":
        addDrinks()
    elif menu == "":
        addMenus("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")
    else:
        addMenus("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

# FUNGSI TAMBAHKAN MENU
def addMenu(ForD, menuPrint, categoriesList, menusList, pricesList, warning):
    clear()
    print("\n\n")

    print(f"Tambahkan Menu {ForD} Baru".center(100))
    print(f"\n\tMenu {ForD} saat ini : ")
    menuPrint()

    print(f"\n\t{warning}\n")

     # fungsi menambahkan menu
    def add(warning):
        clear()
        print("\n\n")

        print(f"Tambahkan Menu {ForD} Baru".center(100))
        print(f"\n\tMenu {ForD} saat ini : ")
        menuPrint()

        print(f"\n\t{warning}\n")

        index = categoriesList.index(category)
        if len(menusList[index]) == 0:
            menusList[index].append(menu)
            pricesList[index].append(price)
            print("\n\tMenu berhasil ditambahkan!")
        else:
            try:
                num = int(input(f"\tDi urutan ke berapa Anda ingin menambahkan Menu {menu}? \n\t>>> "))
            except ValueError:
                add("\033[1;31;40m Harap masukkan angka! \033[0;37;40m")
            else:
                if num > len(menusList[index])+1:
                    add("\033[1;31;40m Urutan tidak memungkinkan! \033[0;37;40m")
                else:
                    if num == len(menusList[index])+1:
                        menusList[index].append(menu)
                        pricesList[index].append(price)

                    else:
                        menusList[index].insert(num-1, menu)
                        pricesList[index].insert(num-1, price)
                        print("\n\tMenu berhasil ditambahkan!")
                    
                    
    # fungsi menambahkan kategori
    def addCategories(category, warning):
        clear()
        print("\n\n")

        print(f"Tambahkan Menu Kategori Baru".center(100))
        print(f"\n\tMenu {ForD} saat ini : ")
        menuPrint()

        print(f"\n\t{warning}\n")
        try:
            num = int(input(f"\tDi urutan ke berapa Anda ingin menambahkan kategori Menu {category}? \n\t>>> "))
        except ValueError:
            addCategories(category, "\033[1;31;40m Harap masukkan angka! \033[0;37;40m")
        else:
            if num > len(categoriesList) + 1:
                addCategories(category, "\033[1;31;40m Urutan tidak memungkinkan! \033[0;37;40m")
            else:
                if num == len(categoriesList)+1:
                    categoriesList.append(category)
                else:
                    newMenu = []
                    newPrice = []
                    categoriesList.insert(num-1, category)
                    menusList.insert(num-1, newMenu)
                    pricesList.insert(num-1, newPrice)
                    print("\n\tKategori berhasil ditambahkan!")

                    newMenu.clear()
                    newPrice.clear()
            add("")

    # input menu
    menu = input(f"\t(+) {ForD} baru\t: ")
    menu = menu.title()

    for menus in menusList:
        # jika menu tidak diisi
        if menu == "":
            addMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Harap isi menu! \033[0;37;40m")
        # jika menu sudah ada
        elif menu in menus:
            addMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Menu sudah ada! \033[0;37;40m")
    
    # input harga
    try:
        price = int(input(f"\t(+) Harga\t\t: Rp"))
    except ValueError:
        addMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Masukkan angka pada harga! \033[0;37;40m")
    else:
        pass

    # input kategori
    category = input(f"\n\tPilih kategori menu untuk {menu} : ")
    category = category.title()
            
    # jika kategori sudah ada
    if category in categoriesList:
        add("")

    # jika kategori tidak diisi
    elif category == "":
        addMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Harap isi kategori! \033[0;37;40m")

    # jika kategori belum ada
    else:
        print("\n\tKategori belum ada sebelumnya. Apakah ingin menambahkan kategori baru?")
        YorN = input("\t(Ketik '1' untuk 'Ya') \n\t>>> ")

        if YorN == "1":
            addCategories(category, "")
        else:
            print(f"\n\tPenambahan menu {menu} dibatalkan.")
            input("\n\tKembali ke menu utama => ")
            ownerMode("")

    refresh("Ganti Menu", ForD, menuPrint)
    
# TAMBAHKAN MAKANAN
def addFood():
    addMenu("Makanan", printFood,foodCategories, foodMenus, foodPrices, "")
# TAMBAHKAN MINUMAN
def addDrinks():
    addMenu("Minuman", printDrinks, drinksCategories, drinksMenus, drinksPrices, "")



# MENU GANTI MENU
def replaceMenus(warning):
    clear()
    print("\n\n\n\n\n\n")
    print("Ganti Menu".center(100))

    print("\n\t ",f"{warning}".center(100), "\n")

    print("Pilih opsi berikut.".center(100))
    print()
    print("(A) Makanan     (B) Minuman".center(100))

    menu = input("\n\t\t\t\t>>> ")
    
    if menu.casefold() == "a":
        replaceFood()
    elif menu.casefold() == "b":
        replaceDrinks()
    elif menu == "":
        replaceMenus("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")
    else:
        replaceMenus("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

# FUNGSI GANTI MENU
def replaceMenu(ForD, menuPrint, categoriesList, menusList, pricesList, warning):
    clear()
    print("\n\n")

    print(f"Ganti Menu {ForD}".center(100))
    print(f"\n\tMenu {ForD} saat ini : ")
    menuPrint()

    print(f"\n\t{warning}\n")

    ubah = input(f"\tGanti : \n\t(A) Kategori Menu   (B) Menu {ForD}   (C) Harga {ForD}\n\t>>> ")

    # ubah nama kategori
    if ubah.casefold() == "a":
        category = input("\n\tKategori yang ingin diubah\n\t>>> ")
        category = category.title()

        # jika kategori tersedia
        if category in categoriesList:
            newCategory = input(f"\n\t{category} --> ")

            # jika kategori sudah ada
            if newCategory in categoriesList:
                replaceMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Nama kategori sudah ada! \033[0;37;40m")
            
            # jika kategori belum ada
            else:
                YorN = input(f"\n\tApakah Anda yakin ingin mengubah Menu {category} menjadi Menu {newCategory}? \n\t(Ketik '1' untuk ya)\n\t>>> ")
                if YorN == "1":
                    index = categoriesList.index(category)
                    categoriesList[index] = newCategory
                    print("\n\t Nama kategori berhasil diganti!")
                    refresh("Ganti Menu", ForD, menuPrint)
                else:
                    print("\n\tPerubahan dibatalkan.")
                    input("\n\tKembali ke menu utama =>")
                    ownerMode("")

        # jika kategori tidak tersedia          
        else:
            replaceMenu(ForD, menuPrint, categoriesList, menusList, pricesList, f"\033[1;31;40m Kategori menu tidak tersedia! \033[0;37;40m")

    # ubah nama menu
    elif ubah.casefold() == "b":
        menu = input(f"\n\tMenu {ForD} yang ingin diubah\n\t>>> ")
        menu = menu.title()

        for menus in menusList:
            # jika menu tersedia
            if menu in menus:
                newMenu = input(f"\n\t{menu} --> ")
                newMenu = newMenu.title()

                # jika nama menu sudah ada
                if newMenu in menus:
                    replaceMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Nama menu sudah ada! \033[0;37;40m")

                # jika nama menu belum ada
                else:
                    YorN = input(f"\n\tApakah Anda yakin ingin mengubah menu {menu} menjadi menu {newMenu}? \n\t(Ketik '1' untuk ya)\n\t>>> ")
                    if YorN == "1":
                        # ganti nama
                        index = menus.index(menu)
                        menus[index] = newMenu

                        print("\n\t Nama menu berhasil diganti!")
                        refresh("Ganti Menu", ForD, menuPrint)

                    else:
                        print("\n\tPerubahan dibatalkan.")
                        input("\n\tKembali ke menu utama =>")
                        ownerMode("")

        # jika menu tidak tersedia
        else:
            replaceMenu(ForD, menuPrint, categoriesList, menusList, pricesList, f"\033[1;31;40m Menu {ForD} tidak tersedia! \033[0;37;40m")
    
    # ubah harga
    elif ubah.casefold() == "c":
        menu = input(f"\n\tMenu {ForD} yang harganya ingin diubah\n\t>>> ")
        menu = menu.title()

        for menus in menusList:
            # jika menu tersedia
            if menu in menus:
                indexMenus = menusList.index(menus)
                indexMenu = menus.index(menu) 

                indexPrices = indexMenus
                indexPrice = indexMenu

                newPrice = input(f"\n\tRp{pricesList[indexPrices][indexPrice]} --> Rp")

                YorN = input(f"\n\tApakah Anda yakin ingin mengubah harga {menu} Rp{pricesList[indexPrices][indexPrice]} menjadi Rp{newPrice}? \n\t(Ketik '1' untuk ya)\n\t>>> ")
                if YorN == "1":

                    # ganti harga
                    pricesList[indexPrices][indexPrice] = newPrice
                    print("\n\t Harga menu berhasil diganti!")
                    refresh("Ganti Menu", ForD, menuPrint)

                else:
                    print("\n\tPerubahan dibatalkan.")
                    input("\n\tKembali ke menu utama =>")
                    ownerMode("")

        # jika menu tidak tersedia
        else:
            replaceMenu(ForD, menuPrint, categoriesList, menusList, pricesList, f"\033[1;31;40m Menu {ForD} tidak tersedia! \033[0;37;40m")

    # jika opsi tidak tersedia
    else:
        replaceMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")
# GANTI MENU MAKANAN
def replaceFood():
    replaceMenu("Makanan", printFood, foodCategories, foodMenus, foodPrices, "")
# GANTI MENU MINUMAN
def replaceDrinks():
    replaceMenu("Minuman", printDrinks, drinksCategories, drinksMenus, drinksPrices, "")



# MENU HAPUS MENU
def deleteMenus(warning):
    clear()
    print("\n\n\n\n\n\n")
    print("Hapus Menu".center(100))

    print("\n\t ",f"{warning}".center(100), "\n")

    print("Pilih opsi berikut.".center(100))
    print()
    print("(A) Makanan     (B) Minuman".center(100))

    menu = input("\n\t\t\t\t>>> ")
    
    if menu.casefold() == "a":
        deleteFood()
    elif menu.casefold() == "b":
        deleteDrinks()
    elif menu == "":
        deleteMenus("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")
    else:
        deleteMenus("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

# FUNGSI HAPUS MENU
def deleteMenu(ForD, menuPrint, categoriesList, menusList, pricesList, warning):
    clear()
    print("\n\n")

    print(f"Hapus Menu {ForD}".center(100))
    print(f"\n\tMenu {ForD} saat ini : ")
    menuPrint()

    print(f"\n\t{warning}\n")

    hapus = input(f"\tHapus : \n\t(A) Kategori Menu   (B) Menu {ForD}\n\t>>> ")

    # hapus nama kategori
    if hapus.casefold() == "a":
        category = input(f"\n\tKategori menu yang ingin dihapus\n\t>>> ")
        category = category.title()

        # jika kategori tersedia
        if category in categoriesList:
            YorN = input(f"\n\tJika kategori menu dihapus, maka seluruh menu di dalamnya juga akan ikut terhapus.\
            \n\tApakah Anda yakin ingin menghapus Menu {category}?\
            \n\t(Ketik '1' untuk ya)\
            \n\t>>> ")
    
            if YorN == "1":
                index = categoriesList.index(category)
                categoriesList.pop(index)
                menusList.pop(index)
                pricesList.pop(index)

                print(f"\n\t Menu {category} berhasil dihapus!")
                refresh("Hapus Menu", ForD, menuPrint)
            else:
                print("\n\tPerubahan dibatalkan.")
                input("\n\tKembali ke menu utama =>")
                ownerMode("")
                      
        # jika kategori tidak tersedia
        else:
            deleteMenu(ForD, menuPrint, categoriesList, menusList, pricesList, f"\033[1;31;40m Kategori menu tidak tersedia! \033[0;37;40m")

    # hapus nama menu
    elif hapus.casefold() == "b":
        menu = input(f"\n\tMenu {ForD} yang ingin dihapus\n\t>>> ")
        menu = menu.title()

        # untuk menus di menusList
        for menus in menusList:

            # jika menu tersedia
            if menu in menus:
                YorN = input(f"\n\tApakah Anda yakin ingin menghapus menu {menu}? \n\t(Ketik '1' untuk ya)\n\t>>> ")

                if YorN == "1":

                    indexMenus = menusList.index(menus)
                    indexMenu = menus.index(menu)

                    menus.pop(indexMenu)

                    for prices in pricesList:
                        indexPrices = indexMenus
                        indexPrice = indexMenu

                        pricesList[indexPrices].pop(indexPrice)

                        print(f"\n\t Menu {menu} berhasil dihapus!")
                        refresh("Hapus Menu", ForD, menuPrint)

                else:
                    print("\n\tPerubahan dibatalkan.")
                    input("\n\tKembali ke menu utama =>")
                    ownerMode("")

        # jika menu tidak tersedia
        else:
            deleteMenu(ForD, menuPrint, categoriesList, menusList, pricesList, f"\033[1;31;40m Menu {ForD} tidak tersedia! \033[0;37;40m")
   
    # jika opsi tidak tersedia
    else:
        deleteMenu(ForD, menuPrint, categoriesList, menusList, pricesList, "\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m") 
# HAPUS MENU MAKANAN
def deleteFood():
    deleteMenu("Makanan", printFood, foodCategories, foodMenus, foodPrices, "")
# HAPUS MENU MINUMAN
def deleteDrinks():
    deleteMenu("Minuman", printDrinks, drinksCategories, drinksMenus, drinksPrices, "")



# REFRESH HALAMAN
def refresh(fungsi, ForD, menuPrint):
    input("\n\tRefresh halaman untuk melihat menu terbaru => ")

    clear()
    print("\n\n")

    print(f"{fungsi} {ForD}".center(100))
    print(f"\n\tMenu {ForD} saat ini : ")
    menuPrint()

    input("\tKembali ke menu utama => ")
    ownerMode("")


def customerMode():
    pesan_makanan("")

def cafe():
    print("-------------------------------".center(100))
    print("         Selamat datang di K-Cafe Lokal         ".center(100, ":"))
    print("-------------------------------".center(100))

    print("\n")

    tanggal = dt.date.today()
    hari_ini = tanggal.strftime("%A")
    print(f"  ~ {hari_ini}, {tanggal} ~  ".center(100))


def pesan_makanan(warning):
    clear()
    cafe()
    printMenu(foodCategories, foodMenus, foodPrices)

    print(f"\t{warning}")
    pesan = input("\n\tApakah Anda ingin memesan makanan? \n\t(Ya / Tidak) \n\t>>> ")
    if pesan.casefold() == "ya" or\
        pesan.casefold() == "yes" or\
        pesan.casefold() == "y" or\
        pesan.casefold() == "ok" or\
        pesan.casefold() ==" k":

        makanan_dipesan("")

    elif pesan.casefold() == "tidak" or\
        pesan.casefold() == "no" or\
        pesan.casefold() == "n" or\
        pesan.casefold() == "g" or\
        pesan.casefold() == "gak" or\
        pesan.casefold() == "skip":

        pesan_minuman("")

    else:
        pesan_makanan("\033[1;31;40m Harap pilih (Ya / Tidak!) \033[0;37;40m")
        
def makanan_dipesan(warning):
    clear()
    cafe()
    printMenu(foodCategories, foodMenus, foodPrices)

    print(f"\t{warning}")

    makanan = input("\n\tKetik menu makanan yang diinginkan \n\t>>> ")
    makanan = makanan.title()

    for menus in foodMenus:
        if makanan in menus:

            orderedFood.append(makanan)

            for prices in foodPrices:
                indexPrices = foodMenus.index(menus)
                indexPrice = menus.index(makanan)

                orderedFoodPrices.append(foodPrices[indexPrices][indexPrice])

                lagi = input("\n\tKetik '1' untuk memesan makanan lagi \n\t>>> ")
                if lagi == "1":
                    makanan_dipesan("")
            
                else:
                    pesan_minuman("")
    else:
        makanan_dipesan("\033[1;31;40m Menu tidak tersedia! \033[0;37;40m")



def pesan_minuman(warning):
    clear()
    cafe()
    printMenu(drinksCategories, drinksMenus, drinksPrices)

    print(f"\t{warning}")
    pesan = input("\n\tApakah Anda ingin memesan minuman? \n\t(Ya / Tidak) \n\t>>> ")
    if pesan.casefold() == "ya" or\
        pesan.casefold() == "yes" or\
        pesan.casefold() == "y" or\
        pesan.casefold() == "ok" or\
        pesan.casefold() ==" k":

        minuman_dipesan("")

    elif pesan.casefold() == "tidak" or\
        pesan.casefold() == "no" or\
        pesan.casefold() == "n" or\
        pesan.casefold() == "g" or\
        pesan.casefold() == "gak" or\
        pesan.casefold() == "skip":

        struk("")

    else:
        pesan_minuman("\033[1;31;40m Harap pilih (Ya / Tidak!) \033[0;37;40m")

def minuman_dipesan(warning):
    clear()
    cafe()
    printMenu(drinksCategories, drinksMenus, drinksPrices)

    print(f"\t{warning}")

    minuman = input("\n\tKetik menu minuman yang diinginkan \n\t>>> ")
    minuman = minuman.title()

    for menus in drinksMenus:
        if minuman in menus:

            orderedDrinks.append(minuman)

            for prices in drinksPrices:
                indexPrices = drinksMenus.index(menus)
                indexPrice = menus.index(minuman)

                orderedDrinksPrices.append(drinksPrices[indexPrices][indexPrice])

                lagi = input("\n\tKetik '1' untuk memesan minuman lagi \n\t>>> ")
                if lagi == "1":
                    minuman_dipesan("")
            
                else:
                    struk("")

    else:
        minuman_dipesan("\033[1;31;40m Menu tidak tersedia! \033[0;37;40m")
    

def struk(warning):
    # jika memesan makanan atau minuman
    if len(orderedFood) != 0 or len(orderedDrinks) != 0:
        clear()
        print(f"\n\tSTRUK PESANAN \n\t{'='*13}")
        jumlah_makanan = len(orderedFood)
        numF = 1
        indexF = 0
        harga_makanan = 0
        # jika memesan makanan
        if len(orderedFood) != 0:
            print("\n\tMakanan yang dipesan : ")

            while numF <= jumlah_makanan:

                dipesan = orderedFood[indexF]
                harga = orderedFoodPrices[indexF]

                menu = f"\t{numF}. {dipesan}".ljust(30)

                print(menu + f"Rp{harga}")

                numF += 1
                indexF += 1
                harga_makanan += harga

            print(f"\t------------------------------------- +")
            print(f"Rp{harga_makanan}".rjust(44))

            if jumlah_makanan >= 2:
                harga_makanan = harga_makanan - (harga_makanan * 0.05)
                print(f"\n\tAnda mendapat diskon 5%! \n\tHarga makanan setelah diskon = {harga_makanan}")

        jumlah_minuman = len(orderedDrinks)
        numD = 1
        indexD = 0
        harga_minuman = 0
        # jika tidak memesan minuman
        if len(orderedDrinks) != 0:
            print("\n\tMinuman yang dipesan : ")

            while numD <= jumlah_minuman:

                dipesan = orderedDrinks[indexD]
                harga = orderedDrinksPrices[indexD]

                menu = f"\t{numD}. {dipesan}".ljust(30)

                print(menu + f"Rp{harga}")

                numD += 1
                indexD += 1
                harga_minuman += harga

            print("\t------------------------------------- +")
            print(f"Rp{harga_minuman}".rjust(44))

            if jumlah_minuman >= 3:
                harga_minuman = harga_minuman - (harga_minuman * 0.1)
                print(f"\n\tAnda mendapat diskon 10%! \n\tHarga minuman setelah diskon = Rp{harga_minuman}")

        total_harga = harga_makanan + harga_minuman

        emoney(total_harga, warning)

    # jika tidak memesan apa-apa
    else:
        kickedOut()



def emoney(nominal, warning):
    print(f"\n\t{warning}")

    pembayaran = input("\n\tApakah Anda ingin membayar dengan E-money? \n\t(Ya / Tidak) \n\t>>> ")
    if pembayaran.casefold() == "ya" or\
        pembayaran.casefold() == "yes" or\
        pembayaran.casefold() == "y" or\
        pembayaran.casefold() == "ok" or\
        pembayaran.casefold() ==" k":

        print(f"\n\tKarena Anda membayar dengan E-money, Anda mendapat diskon 5%!")
        if dt.datetime.today().weekday() < 5:
            print(f"\n\tHari ini adalah weekdays! Anda mendapat diskon 10% ~")
            nominal = nominal - (nominal * (0.05 + 0.1) )
        else:
            print("\n\tHari ini adalah weekend! Anda mendapat diskon 5% ~")
            nominal = nominal - (nominal * (0.05 + 0.05))
    elif pembayaran.casefold() == "tidak" or\
        pembayaran.casefold() == "no" or\
        pembayaran.casefold() == "n" or\
        pembayaran.casefold() == "g" or\
        pembayaran.casefold() == "gak" or\
        pembayaran.casefold() == "skip":

        if dt.datetime.today().weekday() < 5:
            nominal = nominal - (nominal * 0.1)
            print(f"\n\tHari ini adalah weekdays! Anda mendapat diskon 10% ~")
        else:
            nominal = nominal - (nominal * 0.05)
            print("\n\tHari ini adalah weekend! Anda mendapat diskon 5% ~")

    else:
        struk("\033[1;31;40m Harap pilih (Ya/Tidak)! \033[0;37;40m")
        
    print(f"\033[1;36;40m \n\tTotal harga yang Anda harus dibayar = Rp{nominal} \033[0;37;40m")
    input("\n\tLakukan pembayaran => ")
    end()


def end():
    clear()
    print("\n\n\n\n\n\n")
    print("Terima kasih telah mengunjungi K-Cafe Lokal ~".center(100))
    selesai = input("\n\t\t\t\t\tKeluar => ")

    sys.exit()

def kickedOut():
    clear()
    print("\n\n\n\n\n\n")
    print("\033[1;31;40m Anda telah dikeluarkan dari cafe! \033[0;37;40m".center(100))
    input("\n\t\t\t\tKeluar => ")
    sys.exit()



welcome("")



