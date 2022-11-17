import os

nopol_motor = []
nopol_mobil = []
karcisMotor = 2000
karcisMobil = 5000


def time():
    import datetime as dt
    dt = dt.datetime.now()
    hour = '{:02d}'.format(dt.hour)
    print(dt)
    return hour


def motorIn():
    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("\n")

    nopolMotor = input("Input Nopol Motor  : ")

    try:
        hour = time()
        nopol_motor.append(nopolMotor + '-' + hour)
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

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("\n")

    nopolMobil = input("Input Nopol Mobil  : ")

    try:
        hour = time()
        nopol_mobil.append(nopolMobil + '-' + hour)
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

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("\n")

    nopolMotor = input("Input Nopol Motor  : ")

    try:
        if len(nopol_motor) == 0:
            print("Data yang anda cari tidak di temukan")
            while True:
                questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                if questionQuit == 'Y' or questionQuit == 'y':
                    show_menu()
                elif questionQuit == 'N' or questionQuit == 'n':
                    break
                else:
                    print("Yang Anda Masukkan salah!!")

        for nopol in nopol_motor:

            nopolOut = nopol
            splitNopol = nopolOut.split('-')
            nomorKendaraan = splitNopol[0]
            jamMasukKendaraan = splitNopol[1]

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
                print("Jam Masuk Kendaraan (Hour)   : ", jamMasukKendaraan)
                print(" ")
                print("Jam Keluar Kendaraan (Hour)  : ", hour)
                print("Total Biaya Parkir           : ", biayaParkir)
                print("\n")
                print("=" * 100)

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

    print("=" * 100)
    print(" "* 40, " Input Data Kendaraan ", " "*40)
    print("=" * 100)
    print("\n")

    nopolMobil = input("Input Nopol Mobil  : ")

    try:
        if len(nopol_mobil) == 0:
            print("Data yang anda cari tidak di temukan")
            while True:
                questionQuit = input("Tekan Y untuk lanjut ke Menu (Y/N) : ")
                if questionQuit == 'Y' or questionQuit == 'y':
                    show_menu()
                elif questionQuit == 'N' or questionQuit == 'n':
                    break
                else:
                    print("Yang Anda Masukkan salah!!")
            
        for nopol in nopol_mobil:
            # print(nopol)
            nopolOut = nopol
            splitNopol = nopolOut.split('-')
            nomorKendaraan = splitNopol[0]
            jamMasukKendaraan = splitNopol[1]
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
                print("Jam Masuk Kendaraan (Hour)   : ", jamMasukKendaraan)
                print(" ")
                print("Jam Keluar Kendaraan (Hour)  : ", hour)
                print("Total Biaya Parkir           : ", biayaParkir)
                print("\n")
                print("=" * 100)

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
    print("3. Tekan [3] Kembali ke Menu")

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
        else:
            print("Inputan yang anda masukan tidak ada dalam list.")
            show_menu()
    except ValueError:
        print("Inputan tidak sesuai")
        show_menu()
    


if __name__ == "__main__":

    sistem_operasi = os.name

    match sistem_operasi:
        case "posix": os.system("clear")
        case "nt": os.system("cls")

    show_menu()