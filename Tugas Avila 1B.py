# ==============================================================================
# Nama : Avila Yousifa Artya
# NIM  : 12450122836
# ==============================================================================

class NodePegawai:
    def __init__(self, id_pegawai: str, nama: str, jabatan: str):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.jabatan = jabatan
        self.children = []  # List untuk menyimpan bawahan langsung (General Tree)

    def __str__(self):
        return f"[{self.id_pegawai}] {self.jabatan} - {self.nama}"


class OrganisasiTree:
    def __init__(self, root_node: NodePegawai = None):
        self.root = root_node

    def search_node(self, keyword: str, current_node: NodePegawai = None) -> NodePegawai:
        """Mencari node pegawai berdasarkan Nama, Jabatan, atau ID (DFS)."""
        if self.root is None:
            return None
        if current_node is None:
            current_node = self.root

        kata_kunci = keyword.lower()
        if (kata_kunci in current_node.jabatan.lower() or 
            kata_kunci in current_node.nama.lower() or 
            kata_kunci == current_node.id_pegawai.lower()):
            return current_node

        for child in current_node.children:
            hasil = self.search_node(keyword, child)
            if hasil is not None:
                return hasil
        return None

    def insert_node(self, target_atasan: str, node_baru: NodePegawai) -> bool:
        """Menyisipkan pegawai baru di bawah atasan tertentu."""
        if self.root is None:
            self.root = node_baru
            return True

        atasan = self.search_node(target_atasan, self.root)
        if atasan is not None:
            atasan.children.append(node_baru)
            return True
        return False

    def preorder_traversal(self, node: NodePegawai = None, hasil: list = None) -> list:
        """Pre-order: Root -> Children (Kiri ke Kanan)"""
        if hasil is None:
            hasil = []
            node = self.root
        if node is None:
            return hasil

        hasil.append(node.jabatan)
        for child in node.children:
            self.preorder_traversal(child, hasil)
        return hasil

    def inorder_traversal(self, node: NodePegawai = None, hasil: list = None) -> list:
        """In-order (General Tree): First Child -> Root -> Remaining Children"""
        if hasil is None:
            hasil = []
            node = self.root
        if node is None:
            return hasil

        if len(node.children) > 0:
            self.inorder_traversal(node.children[0], hasil)

        hasil.append(node.jabatan)

        for child in node.children[1:]:
            self.inorder_traversal(child, hasil)
        return hasil

    def postorder_traversal(self, node: NodePegawai = None, hasil: list = None) -> list:
        """Post-order: Children (Kiri ke Kanan) -> Root"""
        if hasil is None:
            hasil = []
            node = self.root
        if node is None:
            return hasil

        for child in node.children:
            self.postorder_traversal(child, hasil)
        hasil.append(node.jabatan)
        return hasil

    def cetak_hierarki(self, node: NodePegawai = None, prefix: str = "", is_last: bool = True, is_root: bool = True):
        """Menampilkan visualisasi struktur pohon organisasi di terminal."""
        if self.root is None:
            print("Struktur organisasi masih kosong.")
            return
        if is_root:
            node = self.root
            print(f"\n{node.jabatan} ({node.nama})")
        else:
            connector = "└── " if is_last else "├── "
            print(f"{prefix}{connector}{node.jabatan} ({node.nama})")

        new_prefix = prefix if is_root else prefix + ("    " if is_last else "│   ")
        jumlah_anak = len(node.children)
        for i, child in enumerate(node.children):
            apakah_terakhir = (i == jumlah_anak - 1)
            self.cetak_hierarki(child, new_prefix, apakah_terakhir, is_root=False)


def bangun_data_awal_uin_suska() -> OrganisasiTree:
    """Membangun struktur organisasi sesuai gambar skenario soal nomor 11."""
    tree = OrganisasiTree(NodePegawai("UIN01", "Prof. Dr. Hairunas, M.Ag.", "Rektor (Root)"))

    # Level 1: Bawahan langsung Rektor
    tree.insert_node("Rektor (Root)", NodePegawai("UIN02", "Ketua Senat", "Senat Universitas"))
    tree.insert_node("Rektor (Root)", NodePegawai("UIN03", "Dr. Hj. Helmiati, M.Ag.", "Wakil Rektor I (Bidang Akademik)"))
    tree.insert_node("Rektor (Root)", NodePegawai("UIN04", "Dr. H. Mas'ud Zein, M.Pd.", "Wakil Rektor II (Bidang Administrasi Umum & Keuangan)"))
    tree.insert_node("Rektor (Root)", NodePegawai("UIN05", "Prof. Drs. Promadi, M.A., Ph.D.", "Wakil Rektor III (Bidang Kemahasiswaan & Kerja Sama)"))
    tree.insert_node("Rektor (Root)", NodePegawai("FST01", "Dr. Hartono, M.Pd.", "Dekan Fakultas Sains dan Teknologi"))

    # Level 2: Bawahan Dekan FST
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", NodePegawai("FST02", " Wakil Dekan 1", "Wakil Dekan I (Bidang Akademik & Kelembagaan)"))
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", NodePegawai("FST03", "Wakil Dekan 2", "Wakil Dekan II (Bidang AUPK)"))
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", NodePegawai("FST04", "Wakil Dekan 3", "Wakil Dekan III (Bidang Kemahasiswaan)"))
    tree.insert_node("Dekan Fakultas Sains dan Teknologi", NodePegawai("TIF01", "Kaprodi TIF", "Ketua Program Studi Teknik Informatika"))

    # Level 3: Bawahan Ketua Prodi Teknik Informatika
    tree.insert_node("Ketua Program Studi Teknik Informatika", NodePegawai("TIF02", "Sekprodi TIF", "Sekretaris Program Studi"))
    tree.insert_node("Ketua Program Studi Teknik Informatika", NodePegawai("TIF03", "Kalab Komputer", "Kepala Laboratorium Komputer"))
    tree.insert_node("Ketua Program Studi Teknik Informatika", NodePegawai("TIF04", "Koordinator", "Koordinator Dosen"))

    # Level 4: Bawahan Kepala Laboratorium Komputer
    tree.insert_node("Kepala Laboratorium Komputer", NodePegawai("LAB01", "Tim Asisten", "Asisten Laboratorium"))
    tree.insert_node("Kepala Laboratorium Komputer", NodePegawai("LAB02", "Staf Teknisi", "Teknisi Laboratorium"))

    # Level 4: Bawahan Koordinator Dosen
    tree.insert_node("Koordinator Dosen", NodePegawai("DOS01", "Dosen PA", "Dosen Pembimbing Akademik"))
    tree.insert_node("Koordinator Dosen", NodePegawai("DOS02", "Dosen Pengampu", "Dosen Pengampu Mata Kuliah"))

    # Level 5: Bawahan Dosen Pembimbing Akademik
    tree.insert_node("Dosen Pembimbing Akademik", NodePegawai("MHS01", "Avila Yousifa Artya", "Mahasiswa Bimbingan (Leaf)"))

    return tree


def main():
    org_tree = bangun_data_awal_uin_suska()

    while True:
        print("\n=====================================================================")
        print("   SISTEM MANAJEMEN SILSILAH ORGANISASI UIN SUSKA RIAU (TREE ADT)    ")
        print("=====================================================================")
        print("1. Tampilkan Visualisasi Struktur Organisasi (Tree)")
        print("2. Tambah Pegawai / Jabatan Baru (insert_node)")
        print("3. Cari Data Pegawai / Jabatan (search_node)")
        print("4. Tampilkan Hasil Pre-order, In-order, dan Post-order Traversal")
        print("0. Keluar")
        pilihan = input("Pilih menu (0-4): ").strip()

        if pilihan == "1":
            org_tree.cetak_hierarki()

        elif pilihan == "2":
            atasan = input("Masukkan Nama/Jabatan Atasan : ").strip()
            id_p   = input("Masukkan ID Pegawai Baru     : ").strip()
            nama   = input("Masukkan Nama Pegawai Baru   : ").strip()
            jab    = input("Masukkan Jabatan Baru        : ").strip()
            berhasil = org_tree.insert_node(atasan, NodePegawai(id_p, nama, jab))
            if berhasil:
                print(f"[SUKSES] Jabatan '{jab}' berhasil ditambahkan di bawah '{atasan}'.")
            else:
                print(f"[GAGAL] Atasan '{atasan}' tidak ditemukan di dalam Tree!")

        elif pilihan == "3":
            keyword = input("Masukkan Nama / Jabatan / ID yang dicari: ").strip()
            hasil = org_tree.search_node(keyword)
            if hasil:
                print(f"\n[DITEMUKAN] -> {hasil}")
                if hasil.children:
                    bawahan = ", ".join([c.jabatan for c in hasil.children])
                    print(f"Bawahan Langsung ({len(hasil.children)}): {bawahan}")
                else:
                    print("Status Simpul: Leaf Node (Tidak memiliki bawahan)")
            else:
                print(f"[TIDAK DITEMUKAN] Data '{keyword}' tidak ada di dalam Tree.")

        elif pilihan == "4":
            print("\n--- 1. PRE-ORDER TRAVERSAL ---")
            for idx, item in enumerate(org_tree.preorder_traversal(), 1):
                print(f"{idx}. {item}")

            print("\n--- 2. IN-ORDER TRAVERSAL ---")
            for idx, item in enumerate(org_tree.inorder_traversal(), 1):
                print(f"{idx}. {item}")

            print("\n--- 3. POST-ORDER TRAVERSAL ---")
            for idx, item in enumerate(org_tree.postorder_traversal(), 1):
                print(f"{idx}. {item}")

        elif pilihan == "0":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()