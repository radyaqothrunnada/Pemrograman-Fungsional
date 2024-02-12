class Peserta:
    def __init__(self, id, nama, nilai):
        self.id = id
        self.nama = nama
        self.nilai = nilai
        self.hasil_akhir = "Lolos" if nilai >= 75 else "Tidak Lolos"

# Inisialisasi daftar peserta
daftar_peserta = []

# Fungsi untuk admin menginput data peserta
def input_data_peserta():
    nama = input("Masukkan nama peserta: ")
    nilai = int(input("Masukkan nilai peserta: "))
    peserta = Peserta(len(daftar_peserta), nama, nilai)
    daftar_peserta.append(peserta)
    print("Data peserta berhasil ditambahkan.")

# Fungsi untuk admin mengedit nilai peserta
def edit_nilai_peserta(id_peserta, nilai_baru):
    if 0 <= id_peserta < len(daftar_peserta):
        daftar_peserta[id_peserta].nilai = nilai_baru
        daftar_peserta[id_peserta].hasil_akhir = "Lolos" if nilai_baru >= 75 else "Tidak Lolos"
        print("Nilai peserta berhasil diubah.")
    else:
        print("ID peserta tidak valid.")

# Fungsi untuk peserta melihat nilai dan hasil akhir mereka sendiri
def lihat_nilai_dan_hasil(id_peserta):
    if 0 <= id_peserta < len(daftar_peserta):
        peserta = daftar_peserta[id_peserta]
        print(f"Nama: {peserta.nama}")
        print(f"Nilai: {peserta.nilai}")
        print(f"Hasil Akhir: {peserta.hasil_akhir}")
    else:
        print("ID peserta tidak valid.")

# Contoh penggunaan:
while True:
    print("\nMenu:")
    print("1. Admin - Input Data Peserta")
    print("2. Admin - Edit Nilai Peserta")
    print("3. Peserta - Lihat Nilai dan Hasil")
    print("4. Keluar")
    pilihan = input("Pilih menu (1/2/3/4): ")

    if pilihan == "1":
        input_data_peserta()
    elif pilihan == "2":
        id_peserta = int(input("Masukkan ID peserta yang ingin diubah nilainya: "))
        nilai_baru = int(input("Masukkan nilai baru: "))
        edit_nilai_peserta(id_peserta, nilai_baru)
    elif pilihan == "3":
        id_peserta = int(input("Masukkan ID peserta: "))
        lihat_nilai_dan_hasil(id_peserta)
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang sesuai.")
