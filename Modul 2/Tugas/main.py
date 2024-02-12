expenses = [
    {'tanggal': '2023-07-25', 'deskripsi': 'Makan Siang', 'jumlah': 50000},
    {'tanggal': '2023-07-25', 'deskripsi': 'Transportasi', 'jumlah': 25000},
    {'tanggal': '2023-07-26', 'deskripsi': 'Belanja', 'jumlah': 100000},
]

def  add_expense_interactively():
    date = input("Masukkan tanggal pengeluaran (YYYY-MM-DD):")
    description = input("Masukkan deskripsi pengeluaran:")
    amount = int(input("Masukkan jumlah pengeluaran:"))
    new_expenses = add_expense('2023-07-26', 'Makan Malam', 75000)
    print("Pengeluaran berhasil ditambahkan.")
    return new_expenses

def calculate_total_expenses():
    total = sum(expense['jumlah'] for expense in expenses)
    return total
total_expenses = calculate_total_expenses('2023-07-25')
print(f"Total pengeluaran pada tanggal 2023-07-25: {total_expenses}")


def view_expenses_by_date():
    date = input("Masukkan tanggal (YYYY-MM-DD): ")
    expenses_on_date = get_expenses_by_date('2023-07-26')
    print(f"Pengeluaran pada tanggal 2023-07-26:")
    for expense in expenses_on_date:
        print(f"{expense['deskripsi']} - {expense['jumlah']}")

def view_expenses_report():
    print("\nLaporan Pengeluaran Harian:")
    report = generate_expenses_report()
    print("\nLaporan Pengeluaran Harian:")
    print(report)

def display_menu():
    print("\n===== Aplikasi Pencatat Pengeluaran Harian =====")
    print("1. Tambah Pengeluaran")
    print("2. Total Pengeluaran Harian")
    print("3. Lihat Pengeluaran berdasarkan Tanggal")
    print("4. Lihat Laporan Pengeluaran Harian")
    print("5. Keluar")
# TODO 6 ubah fungsi berikut ke dalam bentuk lambda
def get_user_input(command):
    return int(input(command))
def main():
    global expenses
    while True:
        display_menu()
        choice = get_user_input("Pilih menu (1/2/3/4/5): ")

        if choice == 1:
            expenses = add_expense_interactively(expenses)
        elif choice == 2:
            total_expenses = calculate_total_expenses(expenses)
            print(f"\nTotal Pengeluaran Harian: Rp {total_expenses}")
        elif choice == 3:
            view_expenses_by_date(expenses)
        elif choice == 4:
            view_expenses_report(expenses)
        elif choice == 5:
            print("Terima kasih telah menggunakan aplikasi kami.")

            break
        else:
            print("Pilihan tidak valid. Silahkan pilih menu yang benar.")
if __name__ == "__main__":
    main()
