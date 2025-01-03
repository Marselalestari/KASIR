# Daftar produk dan harga
produk = {
    1: {'nama': 'Apel', 'harga': 5000},
    2: {'nama': 'Pisang', 'harga': 3000},
    3: {'nama': 'Jeruk', 'harga': 4000}
}

# Fungsi untuk menampilkan daftar produk
def tampilkan_produk():
    print("Daftar Produk:")
    for kode, info in produk.items():
        print(f"{kode}. {info['nama']} - Rp {info['harga']}")

# Fungsi untuk mencetak struk
def cetak_struk(pembelian, total_harga, pembayaran, kembalian):
    print("\n--- Struk Pembelian ---")
    for produk_id, jumlah in pembelian.items():
        nama_barang = produk[produk_id]['nama']
        harga_barang = produk[produk_id]['harga']
        total_item = harga_barang * jumlah
        print(f"{nama_barang} x{jumlah} = Rp {total_item}")
    print(f"\nTotal Harga : Rp {total_harga}")
    print(f"Pembayaran : Rp {pembayaran}")
    print(f"Kembalian   : Rp {kembalian}")
    print("\n--- Terima Kasih ---")

# Fungsi utama untuk memilih produk, jumlah, dan pembayaran
def pilih_produk():
    tampilkan_produk()  # Menampilkan daftar produk
    pembelian = {}  # Menyimpan pembelian pengguna
    
    while True:
        try:
            # Meminta input pengguna untuk memilih produk
            pilihan = int(input("Pilih produk (1/2/3): "))
            if pilihan in produk:
                # Meminta jumlah barang yang dibeli
                jumlah = int(input(f"Masukkan jumlah {produk[pilihan]['nama']} yang akan dibeli: "))
                if jumlah <= 0:
                    print("Jumlah harus lebih dari 0. Coba lagi.")
                else:
                    # Menyimpan pembelian
                    pembelian[pilihan] = pembelian.get(pilihan, 0) + jumlah
                    
                    # Menghitung total harga berdasarkan produk yang dibeli
                    total_harga = sum(produk[kode]['harga'] * jumlah for kode, jumlah in pembelian.items())
                    print(f"\nAnda memilih {produk[pilihan]['nama']} sebanyak {jumlah} dengan total harga Rp {total_harga}")
                    
                    # Meminta input pembayaran
                    while True:
                        try:
                            pembayaran = int(input(f"Masukkan jumlah pembayaran: Rp "))
                            if pembayaran < total_harga:
                                print("Pembayaran tidak cukup. Harap masukkan jumlah yang lebih besar.")
                            else:
                                kembalian = pembayaran - total_harga
                                # Cetak struk pembelian
                                cetak_struk(pembelian, total_harga, pembayaran, kembalian)
                                break  # Menghentikan loop pembayaran
                        except ValueError:
                            print("Input tidak valid. Harap masukkan angka.")
                    break  # Menghentikan loop setelah transaksi selesai
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")

# Menjalankan program
pilih_produk()
