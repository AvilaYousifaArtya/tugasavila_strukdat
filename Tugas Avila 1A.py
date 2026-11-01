import time


# DEFINISI OBJEK DATA (PRODUK)

class Produk:
    def __init__(self, id_produk: str, nama: str, kategori: str, harga: float, stok: int):
        self.id_produk = id_produk
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok

    def __str__(self):
        return f"[{self.id_produk}] {self.nama} | Kategori: {self.kategori} | Rp{self.harga:,.0f} | Stok: {self.stok}"



# IMPLEMENTASI ADT 1: HASH TABLE (PYTHON DICT) - UTAMA

class InventarisHash:
    def __init__(self):
        self.data_produk = {}

    def tambah_produk(self, produk: Produk) -> bool:
        if produk.id_produk in self.data_produk:
            return False
        self.data_produk[produk.id_produk] = produk
        return True

    def cari_produk(self, id_produk: str):
        return self.data_produk.get(id_produk, None)

    def hapus_produk(self, id_produk: str) -> bool:
        if id_produk in self.data_produk:
            del self.data_produk[id_produk]
            return True
        return False

    def tampilkan_semua(self):
        if not self.data_produk:
            print("Inventaris kosong.")
            return
        for produk in self.data_produk.values():
            print(produk)



# IMPLEMENTASI ADT 2: ARRAY-BASED LIST (PEMBANDING)

class InventarisList:
    def __init__(self):
        self.data_produk = []

    def tambah_produk(self, produk: Produk) -> bool:
        self.data_produk.append(produk)
        return True

    def cari_produk(self, id_produk: str):
        for produk in self.data_produk:
            if produk.id_produk == id_produk:
                return produk
        return None

    def hapus_produk(self, id_produk: str) -> bool:
        for i, produk in enumerate(self.data_produk):
            if produk.id_produk == id_produk:
                del self.data_produk[i]
                return True
        return False



# IMPLEMENTASI ADT 3: LINKED LIST (PEMBANDING)

class Node:
    def __init__(self, produk: Produk):
        self.produk = produk
        self.next = None

class InventarisLinkedList:
    def __init__(self):
        self.head = None

    def tambah_produk(self, produk: Produk) -> bool:
        node_baru = Node(produk)
        node_baru.next = self.head
        self.head = node_baru
        return True

    def cari_produk(self, id_produk: str):
        current = self.head
        while current:
            if current.produk.id_produk == id_produk:
                return current.produk
            current = current.next
        return None

    def hapus_produk(self, id_produk: str) -> bool:
        current = self.head
        prev = None
        while current:
            if current.produk.id_produk == id_produk:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False


# FUNGSI PENGUKURAN PERFORMA (BENCHMARK)

def jalankan_benchmark(jumlah_data=50000):
    print(f"\n--- Memulai Pengukuran Kompleksitas ({jumlah_data:,} Data Produk) ---")
    inv_hash = InventarisHash()
    inv_list = InventarisList()
    inv_ll = InventarisLinkedList()

    # 1. Pengukuran Penyisipan (Insert)
    start = time.perf_counter()
    for i in range(jumlah_data):
        inv_hash.tambah_produk(Produk(f"PRD{i}", f"Produk {i}", "Umum", 10000, 10))
    waktu_insert_hash = time.perf_counter() - start

    start = time.perf_counter()
    for i in range(jumlah_data):
        inv_list.tambah_produk(Produk(f"PRD{i}", f"Produk {i}", "Umum", 10000, 10))
    waktu_insert_list = time.perf_counter() - start

    start = time.perf_counter()
    for i in range(jumlah_data):
        inv_ll.tambah_produk(Produk(f"PRD{i}", f"Produk {i}", "Umum", 10000, 10))
    waktu_insert_ll = time.perf_counter() - start

    # Target uji: elemen paling akhir diakses (Worst-case untuk List & Linked List)
    target_list_hash = f"PRD{jumlah_data - 1}"
    target_ll = "PRD0"

    # 2. Pengukuran Pencarian (Search)
    start = time.perf_counter()
    inv_hash.cari_produk(target_list_hash)
    waktu_cari_hash = time.perf_counter() - start

    start = time.perf_counter()
    inv_list.cari_produk(target_list_hash)
    waktu_cari_list = time.perf_counter() - start

    start = time.perf_counter()
    inv_ll.cari_produk(target_ll)
    waktu_cari_ll = time.perf_counter() - start

    # 3. Pengukuran Penghapusan (Delete)
    start = time.perf_counter()
    inv_hash.hapus_produk(target_list_hash)
    waktu_hapus_hash = time.perf_counter() - start

    start = time.perf_counter()
    inv_list.hapus_produk(target_list_hash)
    waktu_hapus_list = time.perf_counter() - start

    start = time.perf_counter()
    inv_ll.hapus_produk(target_ll)
    waktu_hapus_ll = time.perf_counter() - start

    print(f"{'Operasi':<22} | {'Hash Table (dict)':<20} | {'Array List (list)':<20} | {'Linked List':<20}")
    print("-" * 88)
    print(f"{'Insert Semua Data':<22} | {waktu_insert_hash:.6f} detik      | {waktu_insert_list:.6f} detik      | {waktu_insert_ll:.6f} detik")
    print(f"{'Search 1 Produk (ID)':<22} | {waktu_cari_hash:.6f} detik      | {waktu_cari_list:.6f} detik      | {waktu_cari_ll:.6f} detik")
    print(f"{'Delete 1 Produk (ID)':<22} | {waktu_hapus_hash:.6f} detik      | {waktu_hapus_list:.6f} detik      | {waktu_hapus_ll:.6f} detik")
    print("-" * 88)



# MENU COMMAND LINE INTERFACE (CLI)

def main():
    inventaris = InventarisHash()
    inventaris.tambah_produk(Produk("P001", "Laptop Gaming ASUS", "Elektronik", 15000000, 12))
    inventaris.tambah_produk(Produk("P002", "Mouse Wireless Logitech", "Aksesoris", 250000, 50))

    while True:
        print("\n=== SISTEM MANAJEMEN INVENTARIS E-COMMERCE (HASH TABLE ADT) ===")
        print("1. Daftarkan Produk Baru (Insert)")
        print("2. Cari Produk berdasarkan ID (Search)")
        print("3. Hapus Produk dari Peredaran (Delete)")
        print("4. Tampilkan Seluruh Produk")
        print("5. Jalankan Benchmark Perbandingan (Dict vs List vs Linked List)")
        print("0. Keluar")
        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            id_p = input("Masukkan ID Produk : ").strip()
            nama = input("Nama Produk        : ").strip()
            kat  = input("Kategori           : ").strip()
            try:
                harga = float(input("Harga (Rp)         : "))
                stok  = int(input("Jumlah Stok        : "))
                if inventaris.tambah_produk(Produk(id_p, nama, kat, harga, stok)):
                    print(f"[SUKSES] Produk '{nama}' berhasil didaftarkan.")
                else:
                    print(f"[GAGAL] ID Produk '{id_p}' sudah terdaftar!")
            except ValueError:
                print("[ERROR] Harga dan stok harus berupa angka!")

        elif pilihan == "2":
            id_p = input("Masukkan ID Produk yang dicari: ").strip()
            start = time.perf_counter()
            produk = inventaris.cari_produk(id_p)
            durasi = time.perf_counter() - start
            if produk:
                print(f"[DITEMUKAN dalam {durasi:.6f} detik] -> {produk}")
            else:
                print(f"[TIDAK DITEMUKAN] Produk dengan ID '{id_p}' tidak ada.")

        elif pilihan == "3":
            id_p = input("Masukkan ID Produk yang akan dihapus: ").strip()
            start = time.perf_counter()
            berhasil = inventaris.hapus_produk(id_p)
            durasi = time.perf_counter() - start
            if berhasil:
                print(f"[SUKSES] Produk '{id_p}' dihapus dalam {durasi:.6f} detik.")
            else:
                print(f"[GAGAL] Produk dengan ID '{id_p}' tidak ditemukan.")

        elif pilihan == "4":
            print("\n--- Daftar Produk Saat Ini ---")
            inventaris.tampilkan_semua()

        elif pilihan == "5":
            jalankan_benchmark(50000)

        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()