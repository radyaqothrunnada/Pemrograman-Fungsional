data_barang = ("Pensil", 1500, "Buku", 5000, "Penggaris", 2000)

def pisahkan_data(data):
    nama_barang = []
    harga_barang = []
    for i in range(0, len(data), 2):
        nama_barang.append(data[i])
    for i in range(1, len(data), 2):
        harga_barang.append(data[i])
    return nama_barang, harga_barang

def gabungkan_list_ke_dict(nama_barang, harga_barang):
    result_dict = {}
    for i in range(len(nama_barang)):
        result_dict[nama_barang[i]] = harga_barang[i]
    return result_dict

print("Langkah 1:")
print(data_barang)

nama_barang, harga_barang = pisahkan_data(data_barang)
print("\nLangkah 2:")
print("Nama Barang:", nama_barang)
print("Harga Barang:", harga_barang)

dict_barang_harga = gabungkan_list_ke_dict(nama_barang, harga_barang)
print("\nLangkah 3:")
print(dict_barang_harga)

