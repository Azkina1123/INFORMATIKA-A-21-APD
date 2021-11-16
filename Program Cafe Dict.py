"""
NAMA    : AZIIZAH OKI SHOFRINA
NIM     : 2109106004
KELAS   : INFORMATIKA A'21
"""

makananKuah = {
    1 : {"Bakso" : 10000},
    2 : {"Sayur Sop" : 12000},
    3 : {"Mie Ayam" : 13000},
    4 : {"Soto" : 13000},
    5 : {"Seblak" : 15000},
    6 : {"Gulai" : 15000},
    7 : {"Rawon" : 15000},
    8 : {"Tongseng Ayam" : 20000}
    }

makananGoreng = {
    1 : {"Ayam Goreng Kremes" : 13000},
    2 : {"Ayam Penyet" : 13000},
    3 : {"Mie Goreng" : 12000},
    4 : {"Nasi Goreng Sosis" : 12000},
    5 : {"Nasi Goreng Ayam" : 12000},
    6 : {"Nasi Goreng Mawut" : 15000},
    7 : {"Nasi Goreng Udang" : 20000},
    8 : {"Nasi Goreng Kepiting" : 20000}
    }

food = [{"Makanan Kuah" : makananKuah}, {"Makanan Goreng" : makananGoreng}]

airMineral = {
    1 : {"Aqua" : 3000},
    2 : {"Ades" : 3500},
    3 : {"Le Mineral" : 3000},
    4 : {"Club" : 3000},
    5 : {"Vit" : 3500}
    }

minumanEs = {
    1 : {"Es Teh" : 5000},
    2 : {"Es Jeruk" : 8000},
    3 : {"Es Campur" : 10000}
    }

jusBuah = {
    1 : {"Jus Semangka" : 10000},
    2 : {"Jus Nanas" : 10000},
    3 : {"Jus Jambu" : 10000},
    4 : {"Jus Tomat" : 10000},
    5 : {"Jus Alpukat" : 12000},
    6 : {"Jus Apel" : 12000},
    7 : {"Jus Pir" : 12000},
    8 : {"Jus Mangga" : 12000}
    }

drink = [{"Air Mineral" : airMineral}, {"Minuman Es" : minumanEs}, {"Jus Buah" : jusBuah}]

orderedFood = {}

orderedDrink = {}


import datetime as dt
from os import system as st
import getpass as gp
import sys
# from typing import OrderedDict

# BERSIHKAN HALAMAN
def clear():
    st("cls")

# PILIH MODE
def welcome(warning): 
    clear()
    print("\n\n\n\n\n\n")
    print("  Selamat datang di K-Cafe Lokal!  ".center(100))
    

    print("\n\t ",f"{warning}".center(100), "\n")

    print("Pilih opsi berikut.".center(100))
    print("(Ketik '0' untuk keluar)".center(100), "\n")
    print("(1) Pemilik Cafe     (2) Pelanggan Cafe".center(100))

    mode = input("\n\t\t\t\t>>> ")

    if mode == "1":
        logIn("")

    elif mode == "2":
        customerMode()

    elif mode == "0":
        end()

    elif mode == "":
        welcome("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")

    else:
        welcome("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

unameCounter = [1]
pwCounter = [1]
# LOG IN (PEMILIK KAFE)
def logIn(warning): 
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
def printMenu(menuList):
    for categories in menuList:
        for category, menus in categories.items():
            print(f"\t{category}")

            for key, value in menus.items():
                print(f"\t{key}. ", end="")
                for menu, price in value.items():
                    print(f"{menu} --- Rp{price}")
            print()
# TAMPILKAN MENU MAKANAN
def printFood():
    printMenu(food)
# TAMPILKAN MENU MINUMAN
def printDrink():
    printMenu(drink)
            

def searchCategory(menuList):
    list_category = []        
    for categories in menuList:
        for category in categories.keys():
            list_category.append(category)
    return list_category
def searchMenu(menuList):
    list_menu = []
    for i in menuList:
        for value in i.values():
            for menus in value.values():
                for menu in menus.keys():
                    list_menu.append(menu)
    return list_menu
    

# MENU TAMBAHKAN MENU
def addMenus(warning):
    clear()
    print("\n\n\n\n\n\n")
    print("  Tambahkan Menu Baru  ".center(100))

    print("\n\t ", f"{warning}".center(100), "\n")

    print("Pilih opsi berikut.".center(100), "\n")
    print("(A) Makanan     (B) Minuman".center(100))

    menu = input("\n\t\t\t\t>>> ")
    
    if menu.casefold() == "a":
        addFood()
    elif menu.casefold() == "b":
        adddrink()
    elif menu == "":
        addMenus("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")
    else:
        addMenus("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

# FUNGSI TAMBAHKAN MENU
def addMenu(ForD, menuPrint, menuList,  warning):
    clear()
    print("\n\n")

    print(f"Tambahkan Menu {ForD} Baru".center(100))
    print(f"\n\tMenu {ForD} saat ini : ")
    menuPrint()

    print(f"\n\t{warning}\n")

    # input menu
    inputMenu = input(f"\t(+) {ForD} baru\t: ")
    inputMenu = inputMenu.title()

    # jika menu tidak diiisi
    if inputMenu == "":
        addMenu(ForD, menuPrint, menuList,   "\033[1;31;40m Harap isi menu! \033[0;37;40m")
    # jika menu sudah ada
    elif inputMenu in searchMenu(menuList):
        addMenu(ForD, menuPrint, menuList,   "\033[1;31;40m Menu sudah ada! \033[0;37;40m")
    else:
        pass
    
    # input harga
    try:
        inputPrice = int(input(f"\t(+) Harga\t\t: Rp"))
    except ValueError:
        addMenu(ForD, menuPrint, menuList,  "\033[1;31;40m Masukkan angka pada harga! \033[0;37;40m")
    else:
        pass

    # input kategori
    inputCategory = input(f"\n\tPilih kategori menu untuk {inputMenu} : ")
    inputCategory = inputCategory.title()

     # fungsi menambahkan menu
    def add(warning):
        clear()
        print("\n\n")

        print(f"Tambahkan Menu {ForD} Baru".center(100))
        print(f"\n\tMenu {ForD} saat ini : ")
        menuPrint()

        print(f"\n\t{warning}\n")
        
        try:
            num = int(input(f"\tDi urutan ke berapa Anda ingin menambahkan Menu {inputMenu}? \n\t>>> "))
        except ValueError:
            add("\033[1;31;40m Harap masukkan angka! \033[0;37;40m")
        else:
            index = searchCategory(menuList).index(inputCategory)

            newMenu = {}
            newMenu.update({inputMenu : inputPrice})

            category = menuList[index]
            menuDict = category[inputCategory.title()]
            if num > len(menuDict)+1:
                add("\033[1;31;40m Urutan tidak memungkinkan! \033[0;37;40m")
            else:
                if num == len(menuDict)+1:
                    menuDict.update({num : newMenu})
                else:
                    jumlah = len(menuDict)

                    while num <= jumlah:
                        menuDict.update({jumlah+1 : menuDict[jumlah]})
                        jumlah -= 1

                    menuDict.update({num : newMenu})

                print("\n\tMenu berhasil ditambahkan!")
                refresh("Ganti Menu", ForD, menuPrint)
                        
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
            if num > len(menuList) + 1:
                addCategories(category, "\033[1;31;40m Urutan tidak memungkinkan! \033[0;37;40m")
            else:
                newCategory = {}
                newMenus = {}
                newMenu = {}

                newMenu[inputMenu] = inputPrice
                newMenus[1] = newMenu
                newCategory[inputCategory] = newMenus
                if num == len(menuList)+1:
                    menuList.append(newCategory)
                else:
                    menuList.insert(num-1, newCategory)
                
                print("\n\tKategori dan menu berhasil ditambahkan!")
                refresh("Ganti Menu", ForD, menuPrint)
                1
    # jika kategori sudah ada
    if inputCategory in searchCategory(menuList):
        add("")

    # jika kategori tidak diisi
    elif inputCategory == "":
        addMenu(ForD, menuPrint, menuList,  "\033[1;31;40m Harap isi kategori! \033[0;37;40m")

    # jika kategori belum ada
    else:
        print("\n\tKategori belum ada sebelumnya. Apakah ingin menambahkan kategori baru?")
        YorN = input("\t(Ketik '1' untuk 'Ya') \n\t>>> ")

        if YorN == "1":
            addCategories(inputCategory, "")
        else:
            print(f"\n\tPenambahan menu {inputMenu} dibatalkan.")
            input("\n\tKembali ke menu utama => ")
            ownerMode("")
# TAMBAHKAN MAKANAN
def addFood():
    addMenu("Makanan", printFood, food, "")
# TAMBAHKAN MINUMAN
def adddrink():
    addMenu("Minuman", printDrink, drink,"")


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
        replacedrink()
    elif menu == "":
        replaceMenus("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")
    else:
        replaceMenus("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

# FUNGSI GANTI MENU
def replaceMenu(ForD, menuPrint, menuList, warning):
    clear()
    print("\n\n")

    print(f"Ganti Menu {ForD}".center(100))
    print(f"\n\tMenu {ForD} saat ini : ")
    menuPrint()

    print(f"\n\t{warning}\n")

    ubah = input(f"\tGanti : \n\t(A) Kategori Menu   (B) Menu {ForD}   (C) Harga {ForD}\n\t>>> ")

    # ubah nama kategori
    if ubah.casefold() == "a":
        inputCategory = input("\n\tKategori yang ingin diubah\n\t>>> ")
        inputCategory = inputCategory.title()

        keys = []
        for i in menuList:
            for key in i.keys():
                keys.append(key)

        # jika kategori tersedia
        if inputCategory in keys:
            newCategory = input(f"\n\t{inputCategory} --> ")
            newCategory = newCategory.title()

            # jika nama kategori sudah ada
            if newCategory in keys:
                replaceMenu(ForD, menuPrint,  "\033[1;31;40m Nama kategori sudah ada! \033[0;37;40m")
            
            # jika nama kategori belum ada
            else:
                YorN = input(f"\n\tApakah Anda yakin ingin mengubah Menu {inputCategory} menjadi Menu {newCategory}? \n\t(Ketik '1' untuk ya)\n\t>>> ")
                if YorN == "1":
                    index = keys.index(inputCategory)
                    category = menuList[index]

                    for key, value in category.items():
                        cadangan = value.copy()
                        category.clear()
                        category.update({newCategory : cadangan})
                    print("\n\t Nama kategori berhasil diganti!")
                    refresh("Ganti Menu", ForD, menuPrint)
                else:
                    print("\n\tPerubahan dibatalkan.")
                    input("\n\tKembali ke menu utama =>")
                    ownerMode("")

        # jika kategori tidak tersedia          
        else:
            replaceMenu(ForD, menuPrint, menuList, f"\033[1;31;40m Kategori menu tidak tersedia! \033[0;37;40m")

    # ubah nama menu
    elif ubah.casefold() == "b":
        inputMenu = input(f"\n\tMenu {ForD} yang ingin diubah\n\t>>> ")
        inputMenu = inputMenu.title()

        # jika menu tersedia
        if inputMenu in searchMenu(menuList):
            newMenu = input(f"\n\t{inputMenu} --> ")
            newMenu = newMenu.title()

            # jika nama menu sudah ada
            if newMenu in searchMenu(menuList):
                replaceMenu(ForD, menuPrint, menuList, "\033[1;31;40m Nama menu sudah ada! \033[0;37;40m")

            # jika nama menu belum ada
            else:
                YorN = input(f"\n\tApakah Anda yakin ingin mengubah menu {inputMenu} menjadi menu {newMenu}? \n\t(Ketik '1' untuk ya)\n\t>>> ")
                if YorN == "1":

                    for i in menuList:
                        for value in i.values():
                            for num, menus in value.items():
                                for menu, price in menus.items():
                                    if menu == inputMenu:
                                        cadangan = {newMenu : price}
                                        value[num] = cadangan

                    print("\n\t Nama menu berhasil diganti!")
                    refresh("Ganti Menu", ForD, menuPrint)

                else:
                    print("\n\tPerubahan dibatalkan.")
                    input("\n\tKembali ke menu utama =>")
                    ownerMode("")

                    # jika menu tidak tersedia
        else:
            replaceMenu(ForD, menuPrint, menuList, f"\033[1;31;40m Menu {ForD} tidak tersedia! \033[0;37;40m")
    
    # ubah harga
    elif ubah.casefold() == "c":
        inputMenu = input(f"\n\tMenu {ForD} yang harganya ingin diubah\n\t>>> ")
        inputMenu = inputMenu.title()


        list_menu = []
        for i in menuList:
            for value in i.values():
                for menus in value.values():
                    for menu in menus.keys():
                        list_menu.append(menu)

        # jika menu tersedia
        if inputMenu in list_menu:
            for i in menuList:
                for value in i.values():
                    for num, menus in value.items():
                        for menu, price in menus.items():
                            if menu == inputMenu:
                                try :
                                    newPrice = int(input(f"\n\tRp{price} --> Rp"))
                                except ValueError:
                                    replaceMenu(ForD, menuPrint, menuList, f"\033[1;31;40m Masukkan angka pada harga! \033[0;37;40m")
                                else:
                                    YorN = input(f"\n\tApakah Anda yakin ingin mengubah harga {inputMenu} Rp{price} menjadi Rp{newPrice}? \n\t(Ketik '1' untuk ya)\n\t>>> ")
                                    if YorN == "1":
                                        for i in menuList:
                                            for value in i.values():
                                                for num, menus in value.items():
                                                    for menu, price in menus.items():
                                                        if menu == inputMenu:
                                                            cadangan = {menu : newPrice}
                                                            value[num] = cadangan
                                        print("\n\t Harga menu berhasil diganti!")
                                        refresh("Ganti Menu", ForD, menuPrint)

                                    else:
                                        print("\n\tPerubahan dibatalkan.")
                                        input("\n\tKembali ke menu utama =>")
                                        ownerMode("")

        # jika menu tidak tersedia
        else:
            replaceMenu(ForD, menuPrint, menuList, f"\033[1;31;40m Menu {ForD} tidak tersedia! \033[0;37;40m")

    # jika opsi tidak tersedia
    else:
        replaceMenu(ForD, menuPrint, menuList, "\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")
# GANTI MENU MAKANAN
def replaceFood():
    replaceMenu("Makanan", printFood, food, "")
# GANTI MENU MINUMAN
def replacedrink():
    replaceMenu("Minuman", printDrink, drink, "")



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
        deletedrink()
    elif menu == "":
        deleteMenus("\033[1;31;40m Harap pilih opsi terlebih dahulu! \033[0;37;40m")
    else:
        deleteMenus("\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m")

# FUNGSI HAPUS MENU
def deleteMenu(ForD, menuPrint, menuList, warning):
    clear()
    print("\n\n")

    print(f"Hapus Menu {ForD}".center(100))
    print(f"\n\tMenu {ForD} saat ini : ")
    menuPrint()

    print(f"\n\t{warning}\n")

    hapus = input(f"\tHapus : \n\t(A) Kategori Menu   (B) Menu {ForD}\n\t>>> ")

    # hapus nama kategori
    if hapus.casefold() == "a":
        inputCategory = input(f"\n\tKategori menu yang ingin dihapus\n\t>>> ")
        inputCategory = inputCategory.title()

        # jika kategori tersedia
        if inputCategory in searchCategory(menuList):
            YorN = input(f"\n\tJika kategori menu dihapus, maka seluruh menu di dalamnya juga akan ikut terhapus.\
            \n\tApakah Anda yakin ingin menghapus Menu {inputCategory}?\
            \n\t(Ketik '1' untuk ya)\
            \n\t>>> ")
    
            if YorN == "1":
                index = searchCategory(menuList).index(inputCategory)
                for i in menuList:
                    for category in i.keys():
                        if inputCategory == category:
                            menuList.remove(i)
                        

                print(f"\n\t Menu {category} berhasil dihapus!")
                refresh("Hapus Menu", ForD, menuPrint)
            else:
                print("\n\tPerubahan dibatalkan.")
                input("\n\tKembali ke menu utama =>")
                ownerMode("")
                      
        # jika kategori tidak tersedia
        else:
            deleteMenu(ForD, menuPrint, menuList, f"\033[1;31;40m Kategori menu tidak tersedia! \033[0;37;40m")

    # hapus nama menu
    elif hapus.casefold() == "b":
        inputMenu = input(f"\n\tMenu {ForD} yang ingin dihapus\n\t>>> ")
        inputMenu = inputMenu.title()

        # jika menu tersedia
        if inputMenu in searchMenu(menuList):
            YorN = input(f"\n\tApakah Anda yakin ingin menghapus menu {inputMenu}? \n\t(Ketik '1' untuk ya)\n\t>>> ")

            if YorN == "1":

                for i in menuList:
                    for value in i.values():
                        for num, menus in value.items():
                            for menu, price in menus.items():
                                if menu == inputMenu:
                                    while num < len(value):
                                        menu_pengganti = num+1
                                        value.update({num : value[menu_pengganti]})
                                        num+=1
                                        
                                    else:
                                        value.pop(num)

                                    print(f"\n\t Menu {inputMenu} berhasil dihapus!")
                                    refresh("Hapus Menu", ForD, menuPrint)

            else:
                print("\n\tPerubahan dibatalkan.")
                input("\n\tKembali ke menu utama =>")
                ownerMode("")

        # jika menu tidak tersedia
        else:
            deleteMenu(ForD, menuPrint, menuList, f"\033[1;31;40m Menu {ForD} tidak tersedia! \033[0;37;40m")
   
    # jika opsi tidak tersedia
    else:
        deleteMenu(ForD, menuPrint, menuList, "\033[1;31;40m Opsi tidak tersedia! \033[0;37;40m") 
# HAPUS MENU MAKANAN
def deleteFood():
    deleteMenu("Makanan", printFood, food, "")
# HAPUS MENU MINUMAN
def deletedrink():
    deleteMenu("Minuman", printDrink, drink, "")


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


# PESAN DAN DIPESAN
def pesan_makanan(warning):
    clear()
    cafe()
    printMenu(food)

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
    printMenu(food)

    print(f"\t{warning}")

    makanan = input("\n\tKetik menu makanan yang diinginkan \n\t>>> ")
    makanan = makanan.title()

    for i in food:
        for value in i.values():
            for menus in value.values():
                for menu, price in menus.items():
                    if makanan == menu:
                        orderedFood.update({makanan : price})
                        lagi = input(f"\n\tKetik '1' untuk memesan makanan lagi \n\t>>> ")
                        if lagi == "1":
                            makanan_dipesan("")
                        else:
                            pesan_minuman("")
    else:
        makanan_dipesan("\033[1;31;40m Menu tidak tersedia! \033[0;37;40m")

def pesan_minuman(warning):
    clear()
    cafe()
    printMenu(drink)

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
    printMenu(drink)

    print(f"\t{warning}")

    minuman = input("\n\tKetik menu minuman yang diinginkan \n\t>>> ")
    minuman = minuman.title()

    for i in drink:
        for value in i.values():
            for menus in value.values():
                for menu, price in menus.items():
                    if minuman == menu:
                        orderedDrink.update({minuman : price})
                        lagi = input(f"\n\tKetik '1' untuk memesan minuman lagi \n\t>>> ")
                        if lagi == "1":
                            minuman_dipesan("")
                        else:
                            struk("")
    else:
        minuman_dipesan("\033[1;31;40m Menu tidak tersedia! \033[0;37;40m")
    

def struk(warning):
    # jika memesan makanan atau minuman
    if len(orderedFood) != 0 or len(orderedDrink) != 0:
        clear()
        print(f"\n\tSTRUK PESANAN \n\t{'='*13}")
        jumlah_makanan = len(orderedFood)
        numF = 1
        indexF = 0
        harga_makanan = 0
        # jika memesan makanan
        if len(orderedFood) != 0:
            print("\n\tMakanan yang dipesan : ")

            num = 1
            for menu, price in orderedFood.items():
                menu = f"\t{num}. {menu}".ljust(30)
                print(menu + f"Rp{price}")
                harga_makanan += price

            print(f"\t------------------------------------- +")
            print(f"Rp{harga_makanan}".rjust(44))

            if jumlah_makanan >= 2:
                harga_makanan = harga_makanan - (harga_makanan * 0.05)
                print(f"\n\tAnda mendapat diskon 5%! \n\tHarga makanan setelah diskon = {harga_makanan}")

        jumlah_minuman = len(orderedDrink)
        numD = 1
        indexD = 0
        harga_minuman = 0
        # jika tidak memesan minuman
        if len(orderedDrink) != 0:
            print("\n\tMinuman yang dipesan : ")

            num = 1
            for menu, price in orderedDrink.items():
                menu = f"\t{num}. {menu}".ljust(30)
                print(menu + f"Rp{price}")
                harga_minuman += price

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

if __name__ == "__main__":
    while True:
        welcome("")



