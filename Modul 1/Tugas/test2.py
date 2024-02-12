# Data campuran yang akan dipisahkan
data_campuran = [105, 3.1, "Hello", 737, "python", 2.7, "World", 412, 5.5, "AI"]

# Inisialisasi variabel untuk menyimpan data sesuai ketentuan
data_float = ()
data_string = []
data_int = {}

# Iterasi melalui data campuran
for item in data_campuran:
    if isinstance(item, float):
        data_float += (item,)
    elif isinstance(item, str):
        data_string.append(item)
    elif isinstance(item, int):
        # Pisahkan angka satuan, puluhan, dan ratusan
        satuan = item % 10
        puluhan = (item // 10) % 10
        ratusan = item // 100
        data_int[item] = {
            "Ratusan": ratusan,
            "Puluhan": puluhan,
            "Satuan": satuan
        }

# Menampilkan hasil pemisahan
print("Data Float (tuple):", data_float)
print("Data String (list):", data_string)
print("Data Int (dictionary):", data_int)
