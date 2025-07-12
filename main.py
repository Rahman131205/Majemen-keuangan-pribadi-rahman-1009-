import csv
from datetime import datetime

# File database
FILE_NAME = 'keuangan.csv'

# Inisialisasi file CSV jika belum ada
def inisialisasi_file():
    try:
        with open(FILE_NAME, mode='r') as file:
            pass
    except FileNotFoundError:
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Tanggal', 'Jenis', 'Kategori', 'Deskripsi', 'Jumlah'])

def tambah_data():
    tanggal = input("Masukkan tanggal (YYYY-MM-DD): ")
    jenis = input("Jenis (Pemasukan/Pengeluaran): ")
    kategori = input("Kategori: ")
    deskripsi = input("Deskripsi: ")
    jumlah = input("Jumlah: ")

    with open(FILE_NAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tanggal, jenis, kategori, deskripsi, jumlah])
    print("Data berhasil ditambahkan.")

def lihat_data():
    with open(FILE_NAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        print("\nData Keuangan:")
        for i, row in enumerate(reader, start=1):
            print(f"{i}. {row}")

def edit_data():
    lihat_data()
    index = int(input("Pilih nomor data yang ingin diedit: "))
    with open(FILE_NAME, mode='r') as file:
        reader = list(csv.reader(file))

    header = reader[0]
    data = reader[1:]

    if 0 < index <= len(data):
        new = []
        for i, val in zip(['Tanggal', 'Jenis', 'Kategori', 'Deskripsi', 'Jumlah'], data[index - 1]):
            new_val = input(f"{i} [{val}]: ") or val
            new.append(new_val)
        data[index - 1] = new

        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        print("Data berhasil diperbarui.")
    else:
        print("Index tidak valid.")

def hapus_data():
    lihat_data()
    index = int(input("Pilih nomor data yang ingin dihapus: "))
    with open(FILE_NAME, mode='r') as file:
        reader = list(csv.reader(file))

    header = reader[0]
    data = reader[1:]

    if 0 < index <= len(data):
        data.pop(index - 1)
        with open(FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        print("Data berhasil dihapus.")
    else:
        print("Index tidak valid.")

def laporan_bulanan():
    bulan = input("Masukkan bulan (01-12): ")
    tahun = input("Masukkan tahun (YYYY): ")
    total_masuk, total_keluar = 0, 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Tanggal'][0:7] == f"{tahun}-{bulan}":
                if row['Jenis'].lower() == 'pemasukan':
                    total_masuk += int(row['Jumlah'])
                else:
                    total_keluar += int(row['Jumlah'])
    print(f"\nLaporan Bulanan {bulan}/{tahun}:")
    print(f"Total Pemasukan : Rp{total_masuk}")
    print(f"Total Pengeluaran: Rp{total_keluar}")

def laporan_tahunan():
    tahun = input("Masukkan tahun (YYYY): ")
    total_masuk, total_keluar = 0, 0

    with open(FILE_NAME, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Tanggal'][0:4] == tahun:
                if row['Jenis'].lower() == 'pemasukan':
                    total_masuk += int(row['Jumlah'])
                else:
                    total_keluar += int(row['Jumlah'])
    print(f"\nLaporan Tahunan {tahun}:")
    print(f"Total Pemasukan : Rp{total_masuk}")
    print(f"Total Pengeluaran: Rp{total_keluar}")

def menu():
    inisialisasi_file()
    while True:
        print("\n=== Menu Manajemen Keuangan ===")
        print("1. Tambah Data")
        print("2. Lihat Semua Data")
        print("3. Edit Data")
        print("4. Hapus Data")
        print("5. Laporan Bulanan")
        print("6. Laporan Tahunan")
        print("7. Keluar")
        
        pilihan = input("Pilih menu (1-7): ")

        if pilihan == '1':
            tambah_data()
        elif pilihan == '2':
            lihat_data()
        elif pilihan == '3':
            edit_data()
        elif pilihan == '4':
            hapus_data()
        elif pilihan == '5':
            laporan_bulanan()
        elif pilihan == '6':
            laporan_tahunan()
        elif pilihan == '7':
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    menu()

