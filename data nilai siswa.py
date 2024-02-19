# ----------------------------------------------------------------------------------------------------------------------
## DATA NILAI SISWA

daftar_nilai = [ 
    {
        'nis': 11001, 
        'nama': 'Muhammad raihan wajdi', 
        'sex': 'M', 
        'matematika': 100, 
        'fisika': 99,
        'kimia': 98
    },
    {   
        'nis': 11002, 
        'nama': 'Sania farah', 
        'sex': 'F', 
        'matematika': 95, 
        'fisika': 85,
        'kimia': 75
    },
    {
        'nis': 11003, 
        'nama': 'rizqa febrian', 
        'sex': 'F', 
        'matematika': 90, 
        'fisika': 88,
        'kimia': 86
    },
    {   
        'nis': 11004, 
        'nama': 'sunaryo bambang', 
        'sex': 'M', 
        'matematika': 85, 
        'fisika': 85,
        'kimia': 85
    },
]

daftar_nilai_update = daftar_nilai.copy()
nis = 0

# ----------------------------------------------------------------------------------------------------------------------
## FUNCTION 1: READ

def read_data():
    print('''
    --------------MENAMPILKAN DAFTAR NILAI SISWA-----------------

    1. Menampilkan Seluruh Daftar Nilai Siswa
    2. Menampilkan Daftar Nilai Seorang Siswa
    3. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-3): ')
    
    if option_sub == '1':
        if len(daftar_nilai_update) == 0:
            print('\n    *****Data tidak ditemukan!*****')
            read_data()
        else:
            print('\n    Daftar Nilai Siswa:')
            for i, daftar_update in enumerate(daftar_nilai_update):
                print(f"\t{i + 1}. NIS: {daftar_update['nis']}, Nama: {daftar_update['nama']}, Jenis Kelamin: {daftar_update['sex']}, Matematika: {daftar_update['matematika']}, Fisika: {daftar_update['fisika']}, Kimia: {daftar_update['kimia']}")
            read_data()
    elif option_sub == '2':
        if len(daftar_nilai_update) == 0:
            print('\n    *****Data tidak ditemukan!*****')
            read_data()
        else:
            input_nomor()
            for daftar_update in daftar_nilai_update:
                if daftar_update['nis'] == nis:
                    print(f"\n    Berikut data seorang siswa yang memiliki NIS {nis}:")
                    print(f"\t1. NIS: {daftar_update['nis']}, Nama: {daftar_update['nama']}, Jenis Kelamin: {daftar_update['sex']}, Matematika: {daftar_update['matematika']}, Fisika: {daftar_update['fisika']}, Kimia: {daftar_update['kimia']}")
                    break
            if daftar_update['nis'] != nis:
                print('\n    *****Data tidak ditemukan!*****')
            read_data()
    elif option_sub == '3':
        main_menu()
    else:
        print('\n    *****Opsi yang anda input salah!*****')
        read_data()

# ----------------------------------------------------------------------------------------------------------------------
## FUNCTION 2: CREATE

def create_data():
    print('''
    --------------MENAMBAHKAN DAFTAR NILAI SISWA---------------

    1. Menambahkan Nilai Siswa
    2. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-2): ')
    
    if option_sub == '1':
        input_nomor()
        for daftar_update in daftar_nilai_update:
            if daftar_update['nis'] == nis:
                print("\n    *****NIS telah terdapat di Daftar Nilai Siswa*****")
                break
        if daftar_update['nis'] != nis:
            tambah_nama = input('    Input nama siswa: ')
            while True:
                for word in tambah_nama.split():
                    if word.isalpha():
                        status = True
                    else:
                        status = False
                        break
                if len(tambah_nama) == 0 or status == False:
                    print ("    *****Data tidak boleh kosong & harus alfabet!*****")
                    tambah_nama = input ("    Input nama siswa: ")
                elif status == True:
                    break

            nama_baru_splitted = tambah_nama.split()
            cap_nama_baru = []
            if len(tambah_nama) > 30:
                for idx,val in enumerate (nama_baru_splitted):
                    if idx == 0 or idx == 1 or idx == 2:
                        cap_nama_baru.append((nama_baru_splitted[idx]).capitalize())
                    else :
                        cap_nama_baru.append((nama_baru_splitted[idx][0]).capitalize())
                tambah_nama = " ".join(cap_nama_baru)    
            else :
                tambah_nama = tambah_nama.title()

            tambah_sex = input('    Input jenis kelamin siswa (M/F): ').upper()
            while tambah_sex != 'M' and tambah_sex != 'F':
                print('    *****Jenis kelamin harus berbentuk M/F & tidak boleh kosong!*****')
                tambah_sex = input('    Input jenis kelamin siswa (M/F): ').upper()
            
            test_dict = {"matematika": 0, "fisika": 0, "kimia": 0}
            for i in test_dict:
                test_dict[i] = input(f'    input nilai {i} (0-100): ')
                while (test_dict[i].isdigit() != True):
                    print('    *****Nilai harus dalam bentuk digit & tidak boleh kosong!*****')
                    test_dict[i] = input(f'    input nilai {i} (0-100): ')
                test_dict[i] = int(test_dict[i])
                while test_dict[i] > 100 or test_dict[i] < 0:
                    print('    *****Nilai harus dalam range 0-100 & tidak boleh kosong*****')
                    test_dict[i] = input(f'    input nilai {i} (0-100): ')
                    while (test_dict[i].isdigit() != True):
                        print('    *****Nilai harus dalam bentuk digit! & tidak boleh kosong*****')
                        test_dict[i] = input(f'    input nilai {i} (0-100): ')
                    test_dict[i] = int(test_dict[i])

            option_save = input('\n    Apakah Anda yakin data akan disimpan? (Y/N): ').upper()

            if option_save == 'Y':
                daftar_nilai_update.append(
                {
                    'nis': nis, 
                    'nama': tambah_nama, 
                    'sex': tambah_sex, 
                    'matematika': test_dict["matematika"], 
                    'fisika': test_dict["fisika"],
                    'kimia': test_dict["kimia"]
                }
                )
                print('\n    *****Data tersimpan*****')
        create_data()
    elif option_sub == '2':
        main_menu()
    else:
        print('\n    *****Opsi yang anda input salah!*****')
        create_data()

# ----------------------------------------------------------------------------------------------------------------------
## FUNCTION 3: UPDATE

def update_data():
    print('''
    --------------MENGUBAH DAFTAR NILAI SISWA---------------

    1. Mengubah Nilai Siswa
    2. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-2): ')
    
    if option_sub == '1':
        input_nomor()
        nomor_initial = nis
        temp = ''
        for daftar_update in daftar_nilai_update:
            if daftar_update['nis'] == nomor_initial:
                print(f"\t1. NIS: {daftar_update['nis']}, Nama: {daftar_update['nama']}, Jenis Kelamin: {daftar_update['sex']}, Matematika: {daftar_update['matematika']}, Fisika: {daftar_update['fisika']}, Kimia: {daftar_update['kimia']}")
                
                option_continue = input('\n    Apakah akan melanjutkan update data? (Y/N): ').upper()
                if option_continue == 'Y':
                    temp = input('    Input kolom yang akan di update [NIS, Nama, Sex, Matematika, Fisika, Kimia]: ').lower()
                    if temp in daftar_nilai_update[0].keys():
                        if temp == 'nis':
                            input_nomor()
                            nomor_baru = nis

                            nomor_sudah_ada = [daftar_update['nis'] for daftar_update in daftar_nilai_update]
                            while nomor_baru in nomor_sudah_ada:
                                print("\n    *****NIS telah terdapat di Daftar Nilai Siswa*****")
                                input_nomor()
                                nomor_baru = nis
                        else:
                            nomor_baru = input(f'    Input {temp} yang baru: ')
                            if temp == 'nama':
                                while True:
                                    for word in nomor_baru.split():
                                        if word.isalpha():
                                            status = True
                                        else :
                                            status = False
                                            break
                                    if len(nomor_baru) == 0 or status == False:
                                        print ("    *****Data tidak boleh kosong & harus alfabet!*****")
                                        nomor_baru = input ("    Input nama siswa: ")
                                    elif status == True:
                                        break

                                nama_baru_splitted = nomor_baru.split()
                                cap_nama_baru = []
                                if len(nomor_baru) > 30:
                                    for idx,val in enumerate (nama_baru_splitted):
                                        if idx == 0 or idx == 1 or idx == 2:
                                            cap_nama_baru.append((nama_baru_splitted[idx]).capitalize())
                                        else :
                                            cap_nama_baru.append((nama_baru_splitted[idx][0]).capitalize())
                                    nomor_baru = " ".join(cap_nama_baru)
                                else :
                                    nomor_baru = nomor_baru.title()
                            elif temp == 'sex':
                                nomor_baru = nomor_baru.upper()
                                while nomor_baru != 'M' and nomor_baru != 'F':
                                    print('    *****Jenis kelamin harus M/F!*****')
                                    nomor_baru = input(f'    Input {temp} baru: ')
                            else:
                                while (nomor_baru.isdigit() != True):
                                    print('    *****Nilai harus dalam bentuk digit & tidak boleh kosong!*****')
                                    nomor_baru = input(f'    Input {temp} baru: ')
                                nomor_baru = int(nomor_baru)
                                while nomor_baru > 100 or nomor_baru < 0:
                                    print('    *****Nilai harus dalam range 0-100 & tidak boleh kosong*****')
                                    nomor_baru = input(f'    Input {temp} baru: ')
                                    while (nomor_baru.isdigit() != True):
                                        print('    *****Nilai harus dalam bentuk digit & tidak boleh kosong!*****')
                                        nomor_baru = input(f'    Input {temp} baru: ')
                                    nomor_baru = int(nomor_baru)

                        update = input('\n    Apakah Anda yakin data akan diupdate? (Y/N): ').upper()
                        if update == 'Y':
                            daftar_update[temp] = nomor_baru
                            print('    *****Data Terupdate!*****')
                    else:
                        print('\n    *****Opsi yang anda input salah!*****')
                break
        if temp != 'nis':
            if daftar_update['nis'] != nomor_initial:
                print('\n    *****Data tidak ditemukan!*****')
        update_data()
    elif option_sub == '2':
        main_menu()
    else:
        print('\n    *****Opsi yang anda input salah!*****')
        update_data()

# ----------------------------------------------------------------------------------------------------------------------
## FUNCTION 4: DELETE

def delete_data():
    print('''
    --------------MENGHAPUS DAFTAR NILAI SISWA---------------

    1. Menghapus Daftar Nilai Siswa
    2. Kembali ke Main Menu
    ----------------------------------------------------
    ''')
    
    option_sub = input('    Input sub-menu (1-2): ')
    
    if option_sub == '1':
        input_nomor()
        for index, daftar_update in enumerate(daftar_nilai_update):
            if daftar_update['nis'] == nis:
                option_delete = input('\n    Apakah Anda yakin data akan dihapus? (Y/N): ').upper()
                if option_delete == 'Y':
                    del daftar_nilai_update[index]
                    print('\n    *****Data dihapus!*****')
                break
        if daftar_update['nis'] != nis:
            print('\n    *****Data tidak ditemukan!*****')
        delete_data()
    elif option_sub == '2':
        main_menu()
    else:
        print('\n    *****Opsi yang anda input salah!*****')
        delete_data()

# ----------------------------------------------------------------------------------------------------------------------
## FUNCTION 5: QUIT PROGRAM

def quit_program():
    print('\n*****Terima kasih & Sampai jumpa lagi!*****')
    quit()

# ----------------------------------------------------------------------------------------------------------------------
## FUNCTION THAT CALL REPEATLY

def input_nomor():
    while True:
        global nis
        nis = input('\n    Input Nomor Induk Siswa (NIS): ')
        if nis.isdigit() == True:
            nis = int(nis)
            break
        print('\n    *****NIS tidak boleh kosong & harus dalam bentuk digit!*****')

# -----------------------------------------------------------------------------------------------------------------------
## MAIN MENU

def main_menu():
    print('''
--------------------------------------------------------
Selamat Datang di Daftar Nilai Siswa Sekolah Purwadhika !

Main Menu List:
1. Menampilkan Daftar Nilai Siswa
2. Menambah Daftar Nilai Siswa
3. Mengubah Daftar Nilai Siswa
4. Menghapus Daftar Nilai Siswa
5. Keluar dari Program Daftar Nilai Siswa
--------------------------------------------------------
    ''')

    option_main = input('Input Main Menu (1-5): ')
    
    if option_main == '1':
        read_data()
    elif option_main == '2':
        create_data()
    elif option_main == '3':
        update_data() 
    elif option_main == '4':
        delete_data() 
    elif option_main == '5':
        quit_program() 
    else:
        print('\n    *****Opsi yang anda input salah!*****')
        main_menu()

# -----------------------------------------------------------------------------------------------------------------------
## Call main_menu function
main_menu()