list_angka = [20, 10,  20, 60]

def klarifikasi_angka = lambda x: x if x > 0, else x < 0
    
def pencarian_angka(list_angka, find):
    for num in list_angka:
        if num == find:
         return "found"
    return "not found"
