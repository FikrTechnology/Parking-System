import os

userId = "admin"
passId = "admin"

attemp = 0
isFrom = ""

nopol_motor = []
nopol_mobil = []
rekap_kendaraan = []

karcisMotor = 2000
karcisMobil = 5000

def dateTime():
    import time

    dt = time.strftime('%D %H:%M')
    return dt


def time():
    import datetime as dt
    dt = dt.datetime.now()
    hour = '{:02d}'.format(dt.hour)
    # print(dt)
    return hour


def motorIn():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    dt = dateTime()

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("Date                 : ",dt)
    print("\n")

    nopolMotor = input("Input Nopol Motor    : ")

    try:
        hour = time()
        nopol_motor.append(nopolMotor + '-' + hour + '-' + dt)
        print(nopol_motor)
        show_menu()

    except ValueError:
        print("Inputan tidak sesuai")
        motorIn()
       

def mobilIn():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    dt = dateTime()

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("Date                 : ", dt)
    print("\n")

    nopolMobil = input("Input Nopol Mobil    : ")

    try:
        hour = time()
        nopol_mobil.append(nopolMobil + '-' + hour + '-' + dt)
        print(nopol_mobil)
        show_menu()

    except ValueError:
        print("Inputan tidak sesuai")
        mobilIn()


def motorOut():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    dt = dateTime()

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("Date                 : ", dt)
    print("\n")

    nopolMotor = input("Input Nopol Motor    : ")

    try:
        if len(nopol_motor) == 0:
            print("Data yang anda cari tidak di temukan")
            while True:
                questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                if questionQuit == 'Y' or questionQuit == 'y':
                    show_menu()
                elif questionQuit == 'N' or questionQuit == 'n':
                    motorOut()
                else:
                    print("Yang Anda Masukkan salah!!")

        for nopol in nopol_motor:

            nopolOut = nopol
            splitNopol = nopolOut.split('-')
            nomorKendaraan = splitNopol[0]
            jamMasukKendaraan = splitNopol[1]
            dateIn = splitNopol[2]

            if len(nopolMotor) == len(nomorKendaraan) and nomorKendaraan.__contains__(nopolMotor):
                # print('masuk sini 2')
                hour = time()

                totalJam = int(hour) - int(jamMasukKendaraan)
                biayaParkir = ''
                
                if totalJam == 0:
                    biayaParkir = karcisMotor
                else:
                    biayaParkir = karcisMotor + (karcisMotor * totalJam)
                
                
                print("=" * 100)
                print("\n")
                print("Nomor Kendaraan              : ", nomorKendaraan)
                print("Jam Masuk Kendaraan          : ", dateIn)
                print(" ")
                print("Jam Keluar Kendaraan         : ", dt)
                print("Total Biaya Parkir           : ", biayaParkir)
                print("\n")
                print("=" * 100)

                rekap_kendaraan.append(str(nomorKendaraan) + '-' + dateIn + '-' + dt + '-' + str(biayaParkir) + '-' + 'motor')
                nopol_motor.remove(nopolOut)
                
                while True:
                    questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                    if questionQuit == 'Y' or questionQuit == 'y':
                        show_menu()
                    elif questionQuit == 'N' or questionQuit == 'n':
                        motorOut()
                    else:
                        print("Yang Anda Masukkan salah!!")
            else:
                if len(nopol_motor) == 1:
                    motorOut()
                else:
                    pass

        while True:
            print("Nomor Polisi yang anda masukan tidak di temukan")

            questionQuit = input("Tekan Y untuk lanjut ke Input Mobil Keluar (Y/N) : ")
            if questionQuit == 'Y' or questionQuit == 'y':
                motorOut()
            elif questionQuit == 'N' or questionQuit == 'n':
                show_menu()
            else:
                print("Yang Anda Masukkan salah!!")

    except ValueError:
        print("Inputan tidak sesuai")
        motorOut()

def mobilOut():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    dt = dateTime()

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("Date                 : ", dt)
    print("\n")

    nopolMobil = input("Input Nopol Mobil    : ")

    try:
        if len(nopol_mobil) == 0:
            print("Data yang anda cari tidak di temukan")
            while True:
                questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                if questionQuit == 'Y' or questionQuit == 'y':
                    show_menu()
                elif questionQuit == 'N' or questionQuit == 'n':
                    mobilOut()
                else:
                    print("Yang Anda Masukkan salah!!")
            
        for nopol in nopol_mobil:
            # print(nopol)
            nopolOut = nopol
            splitNopol = nopolOut.split('-')
            nomorKendaraan = splitNopol[0]
            jamMasukKendaraan = splitNopol[1]
            dateIn = splitNopol[2]
            # print('nopolOut ', nopolOut)
            # print('nomor kendaraan ', nomorKendaraan)
            # print('jam masuk kendaraan ', jamMasukKendaraan)
            
                
            if len(nopolMobil) == len(nomorKendaraan) and nomorKendaraan.__contains__(nopolMobil):
                # print('masuk mobilOut')
                hour = time()
                # nopolOut = nopol
                # splitNopol = nopolOut.split('-')
                # nomorKendaraan = splitNopol[0]
                # jamMasukKendaraan = splitNopol[1]

                totalJam = int(hour) - int(jamMasukKendaraan)
                biayaParkir = ''
                
                if totalJam == 0:
                    biayaParkir = karcisMobil
                else:
                    biayaParkir = karcisMobil + (karcisMobil * totalJam)
                
                
                print("=" * 100)
                print("\n")
                print("Nomor Kendaraan              : ", nomorKendaraan)
                print("Jam Masuk Kendaraan          : ", dateIn)
                print(" ")
                print("Jam Keluar Kendaraan         : ", dt)
                print("Total Biaya Parkir           : ", biayaParkir)
                print("\n")
                print("=" * 100)

                rekap_kendaraan.append(str(nomorKendaraan) + '-' + dateIn + '-' + dt + '-' + str(biayaParkir) + '-' + 'mobil')
                nopol_mobil.remove(nopolOut)
                
                while True:
                    questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                    if questionQuit == 'Y' or questionQuit == 'y':
                        show_menu()
                    elif questionQuit == 'N' or questionQuit == 'n':
                        mobilOut()
                    else:
                        print("Yang Anda Masukkan salah!!")
            else:
                if len(nopol_mobil) == 1:
                    mobilOut()
                else:
                    pass

        while True:
            print("Nomor Polisi yang anda masukan tidak di temukan")

            questionQuit = input("Tekan Y untuk lanjut ke Input Mobil Keluar (Y/N) : ")
            if questionQuit == 'Y' or questionQuit == 'y':
                mobilOut()
            elif questionQuit == 'N' or questionQuit == 'n':
                show_menu()
            else:
                print("Yang Anda Masukkan salah!!")

    except ValueError:
        print("Inputan tidak sesuai")
        mobilOut()


def show_data():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("=" * 100)
    print(" "* 30, " Selamat Datang di Parkir UBSI Slipi ", " "*30)
    print("=" * 100)
    print("1. Tekan [1] untuk Data Motor masuk")
    print("2. Tekan [2] untuk Data Mobil masuk")
    print("3. Tekan [3] untuk Data Rekap Parkiran")
    print('\n')
    print("4. Tekan [99] Kembali ke Menu")
    print('\n')

    inpMenu = input("Silahkan Masukan Nomor Data yang ingin di Lihat : ")

    try:
        chooseData= int(inpMenu)

        if chooseData == 1:
            print(nopol_motor)
            while True:
                questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                if questionQuit == 'Y' or questionQuit == 'y':
                    show_menu()
                elif questionQuit == 'N' or questionQuit == 'n':
                    show_data()
                else:
                    print("Yang Anda Masukkan salah!!")
        elif chooseData == 2:
            print(nopol_mobil)
            while True:
                questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                if questionQuit == 'Y' or questionQuit == 'y':
                    show_menu()
                elif questionQuit == 'N' or questionQuit == 'n':
                    show_data()
                else:
                    print("Yang Anda Masukkan salah!!")
        elif chooseData == 3:
            print(rekap_kendaraan)
            while True:
                questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                if questionQuit == 'Y' or questionQuit == 'y':
                    show_menu()
                elif questionQuit == 'N' or questionQuit == 'n':
                    show_data()
                else:
                    print("Yang Anda Masukkan salah!!")
        elif chooseData == 99:
            show_menu()
        else:
            print("Inputan yang anda masukan tidak ada dalam list.")
            show_data()
    except ValueError:
        print("Inputan tidak sesuai")
        show_data()


def show_menu():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("=" * 100)
    print(" "* 30, " Selamat Datang di Parkir UBSI Slipi ", " "*30)
    print("=" * 100)
    print("\n")
    print("1. Tekan [1] untuk Motor masuk")
    print("2. Tekan [2] untuk Mobil masuk")
    print("3. Tekan [3] untuk Motor Keluar")
    print("4. Tekan [4] untuk Mobil Keluar")
    print("5. Tekan [5] untuk Menampilkan Data")
    print("")
    print("98. Tekan [98] untuk ganti Password Login")
    print("99. Tekan [99] untuk keluar ke login")
    print("\n")

    inpMenu = input("Silahkan Masukan Nomor sesuai Petunjuk diatas : ")

    try:
        chooseTransport = int(inpMenu)

        if chooseTransport == 1:
            motorIn()
        elif chooseTransport == 2:
            mobilIn()
        elif chooseTransport == 3:
            motorOut()
        elif chooseTransport == 4:
            mobilOut()
        elif chooseTransport == 5:
            show_data()
        elif chooseTransport == 98:
            changePass("menu")
        elif chooseTransport == 99:
            login()
        else:
            print("Inputan yang anda masukan tidak ada dalam list.")
            show_menu()
    except ValueError:
        print("Inputan tidak sesuai")
        show_menu()

def changePass(isFromWhere):
    global passId
    global isFrom

    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("=" * 100)
    print(" "* 30, " Selamat Datang di Parkir UBSI Slipi ", " "*30)
    print("=" * 100)
    print("\n")

    isFrom = isFromWhere

    passId = input("Silahkan Masukkan Password anda : ")

    try:
        if isFrom == "menu":
            show_menu()
        elif isFrom == "login":
            return passId

    except ValueError:
        print("Inputan tidak sesuai")
        changePass(isFrom)

    
def login():
    global userId
    global passId
    global attemp

    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("=" * 100)
    print(" "* 30, " Selamat Datang di Parkir UBSI Slipi ", " "*30)
    print("=" * 100)
    print("\n")
    username = input(" "* 30+ "Username    : ")
    password = input(" "* 30+ "Password    : ")

    try:
        if username == userId:
            if password == passId:
                print("Login Berhasil")
                show_menu()
            else:
                if attemp == 3 :
                    passId = ""
                    while True:
                        chooseInp = str(input("Password anda telah di Blokir, Tekan Y untuk mengganti Password!!   : ")).upper()
                        if chooseInp == "Y":
                            changePass("login")
                            break
                        elif chooseInp == "N":
                            login()
                        else:
                            print("Input yang anda masukkan tidak sesuai!!")
                    attemp = 0
                    login()
                else:
                    attemp += 1
                    print("Password anda tidak sesuai!!")
                    login()
        else:
            print("Username Salah")
            login()
    except ValueError:
        print("Inputan tidak sesuai")
        login()

if __name__ == "__main__":

    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    login()