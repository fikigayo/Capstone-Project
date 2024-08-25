def main():
    while True:
        print("\n--- Data Karyawan Perusahaan ---")
        print("1. Tampilkan Data Karyawan")
        print("2. Tambah Data Karyawan")
        print("3. Ubah Data Karyawan")
        print("4. Hapus Data Karyawan")
        print("5. Exit\n")
        menu = input("Pilih Menu: ")
        
        if menu == '1':
            tampilkan_data_karyawan()
        elif menu == '2':
            tambah_data_karyawan()
        elif menu == '3':
            ubah_data_karyawan()
        elif menu == '4':
            hapus_data_karyawan()
        elif menu == '5':
            print("\nTerima kasih telah menggunakan program ini.")
            break
        else:
            print("\nMenu tidak Ada. Silakan coba lagi.")

data_karyawan = {
    'Id_karyawan': [1, 2, 3, 4],
    'nama': ['asep budianto', 'bambang pamungkas', 'eko patrio', 'susi susanti'],
    'status': [1, 0, 0, 1],
    'jabatan': ['manager', 'senior', 'junior', 'ceo'],
    'divisi': ['fron tend', 'back end', 'it support', 'data analyst'],
    'gaji': [16e6, 12e6, 5.5e6, 25e6]
}

def tampilkan_data_karyawan():
    print("\n--- Data Karyawan ---")
    print("1. Tampilkan Semua Data Karyawan")
    print("2. Cari Data Karyawan berdasarkan ID")
    print("3. Kembali\n")
    menu = input("Pilih Menu: ")
    
    if menu == '1':
        print(f"|{'ID':^5}|{'Nama':^20}|{'Status':^10}|{'Jabatan':^12}|{'Divisi':^15}|{'Gaji':^12}|")
        print(f"|{'-'*5}|{'-'*20}|{'-'*10}|{'-'*12}|{'-'*15}|{'-'*12}|")
        for i in range(len(data_karyawan['Id_karyawan'])):
            print(f"|{data_karyawan['Id_karyawan'][i]:^5}", end='')
            print(f"|{data_karyawan['nama'][i].title():<20}", end='')
            print(f"|{('Menikah' if data_karyawan['status'][i] else 'Lajang'):^10}", end='')
            print(f"|{data_karyawan['jabatan'][i].title():^12}", end='')
            print(f"|{data_karyawan['divisi'][i].title():^15}", end='')
            print(f"|{int(data_karyawan['gaji'][i]):>12}|")
    elif menu == '2':
        try:
            id_karyawan = int(input("Masukkan ID Karyawan: "))
            if id_karyawan in data_karyawan['Id_karyawan']:
                index = data_karyawan['Id_karyawan'].index(id_karyawan)
                print(f"\nNama: {data_karyawan['nama'][index]}")
                print(f"Status: {'Menikah' if data_karyawan['status'][index] else 'Lajang'}")
                print(f"Jabatan: {data_karyawan['jabatan'][index]}")
                print(f"Divisi: {data_karyawan['divisi'][index]}")
                print(f"Gaji: {data_karyawan['gaji'][index]}")
            else:
                print("ID Karyawan tidak ditemukan.")
        except ValueError:
            print("ID Karyawan harus berupa angka.")
    elif menu == '3':
        return
    else:
        print("Menu tidak valid.")
    

def tambah_data_karyawan():
    while True:
        print("\n--- Tambah Data Karyawan ---")
        try:
            id_karyawan = int(input("Masukkan ID Karyawan: "))
            if id_karyawan in data_karyawan['Id_karyawan']:
                print("Maaf ID Karyawan Sudah Ada")
                continue
            
            nama = input("Masukkan Nama: ")
            status = input("Masukkan Status Menikah (Y/N): ")
            status = 1 if status.lower() == 'y' else 0
            jabatan = input("Masukkan Jabatan: ")
            divisi = input("Masukkan Divisi: ")
            gaji = float(input("Masukkan Gaji: "))
            
            data_karyawan['Id_karyawan'].append(id_karyawan)
            data_karyawan['nama'].append(nama)
            data_karyawan['status'].append(status)
            data_karyawan['jabatan'].append(jabatan)
            data_karyawan['divisi'].append(divisi)
            data_karyawan['gaji'].append(gaji)
            
            print(f"\nData karyawan berhasil ditambahkan.\n")
            print(f"ID: {id_karyawan}")
            print(f"Nama: {nama}")
            print(f"Status: {'Menikah' if status else 'Lajang'}")
            print(f"Jabatan: {jabatan}")
            print(f"Divisi: {divisi}")
            print(f"Gaji: {gaji}")
            
            lanjutkan = input("Lanjutkan input data karyawan? (Y/N): ")
            if lanjutkan.lower() != 'y':
                break
        except ValueError:
            print("Input tidak valid. Silakan coba lagi.")

def ubah_data_karyawan():
    try:
        id_karyawan = int(input("\nMasukkan ID Karyawan yang ingin diubah: "))
        if id_karyawan in data_karyawan['Id_karyawan']:
            index = data_karyawan['Id_karyawan'].index(id_karyawan)
            while True:
                print("\n--- Ubah Data Karyawan ---")
                print("1. Ubah Nama")
                print("2. Ubah Status")
                print("3. Ubah Jabatan")
                print("4. Ubah Divisi")
                print("5. Ubah Gaji")
                print("6. Kembali")
                menu = input("Pilih Menu: ")
                
                if menu == '1':
                    nama_baru = input("Masukkan Nama Baru: ")
                    konfirmasi = input("Yakin ingin mengubah nama? (Y/N): ")
                    if konfirmasi.lower() == 'y':
                        data_karyawan['nama'][index] = nama_baru
                        print(f"Nama {data_karyawan['nama'][index]} berhasil diubah menjadi {nama_baru}.")
                elif menu == '2':
                    status_baru = input("Masukkan Status Menikah (Y/N): ")
                    status_baru = 1 if status_baru.lower() == 'y' else 0
                    konfirmasi = input("Yakin ingin mengubah status? (Y/N): ")
                    if konfirmasi.lower() == 'y':
                        data_karyawan['status'][index] = status_baru
                        print(f"Status berhasil diubah menjadi {'Menikah' if status_baru else 'Lajang'}.")
                elif menu == '3':
                    jabatan_baru = input("Masukkan Jabatan Baru: ")
                    konfirmasi = input("Yakin ingin mengubah jabatan? (Y/N): ")
                    if konfirmasi.lower() == 'y':
                        data_karyawan['jabatan'][index] = jabatan_baru
                        print(f"Jabatan {data_karyawan['jabatan'][index]} berhasil diubah menjadi {jabatan_baru}.")
                elif menu == '4':
                    divisi_baru = input("Masukkan Divisi Baru: ")
                    konfirmasi = input("Yakin ingin mengubah divisi? (Y/N): ")
                    if konfirmasi.lower() == 'y':
                        data_karyawan['divisi'][index] = divisi_baru
                        print(f"Divisi {data_karyawan['divisi'][index]} berhasil diubah {divisi_baru}.")
                elif menu == '5':
                    try:
                        gaji_baru = float(input("\nMasukkan Gaji Baru: "))
                        konfirmasi = input("Yakin ingin mengubah gaji? (Y/N): ")
                        if konfirmasi.lower() == 'y':
                            data_karyawan['gaji'][index] = gaji_baru
                            print(f"Gaji {data_karyawan['gaji'][index]} berhasil diubah menjadi {gaji_baru}.")
                    except ValueError:
                        print("\nGaji harus berupa angka.")
                elif menu == '6':
                    break
                else:
                    print("Menu tidak valid.")
        else:
            print("ID Karyawan tidak ditemukan.")
    except ValueError:
        print("ID Karyawan harus berupa angka.")

def hapus_data_karyawan():
    try:
        id_karyawan = int(input("\nMasukkan ID Karyawan yang ingin dihapus: "))
        if id_karyawan in data_karyawan['Id_karyawan']:
            index = data_karyawan['Id_karyawan'].index(id_karyawan)
            konfirmasi = input(f"\nYakin ingin menghapus data karyawan {id_karyawan} dengan nama {data_karyawan['nama'][index].title()}? (Y/N): ")
            temp_nama_karyawan = data_karyawan['nama'][index]
            if konfirmasi.lower() == 'y':
                data_karyawan['Id_karyawan'].pop(index)
                data_karyawan['nama'].pop(index)
                data_karyawan['status'].pop(index)
                data_karyawan['jabatan'].pop(index)
                data_karyawan['divisi'].pop(index)
                data_karyawan['gaji'].pop(index)
                print(f"\nData karyawan {id_karyawan} dengan nama {temp_nama_karyawan.title()} berhasil dihapus.")
            else:
                print("\nPenghapusan dibatalkan.")
        else:
            print("\nID Karyawan tidak ditemukan.")
    except ValueError:
        print("\nID Karyawan harus berupa angka.")

if __name__ == '__main__':
    main()