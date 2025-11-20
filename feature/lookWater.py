import time
import arts
import layout
from data import dk

def lookWater():
    def cek_item(nm):
        dk.cur.execute("SELECT * FROM user_inventory WHERE nama = ?", (nm,))
        return dk.cur.fetchone()

    def ambil_item(nm):
        it = cek_item(nm)
        if not it:
            return False
        jml = int(it[2])
        sisa = jml - 1
        if sisa > 0:
            dk.cur.execute("UPDATE user_inventory SET jumlah = ? WHERE nama = ?", (sisa, nm))
        else:
            dk.cur.execute("DELETE FROM user_inventory WHERE nama = ?", (nm,))
        dk.db.commit()
        return True

    def tambah_air():
        dk.cur.execute("SELECT * FROM user_foods WHERE nama = ?", ("Air bersih",))
        ada = dk.cur.fetchone()
        if ada:
            jml = int(ada[3]) + 1
            dk.cur.execute("UPDATE user_foods SET jumlah = ? WHERE nama = ?", (jml, "Air bersih"))
        else:
            dk.cur.execute(
                "INSERT INTO user_foods (nama, kekenyangan, jumlah) VALUES (?, ?, ?)",
                ("Air bersih", 10, 1)
            )
        dk.db.commit()

    print("Pilih metode pencarian air bersih:")
    print("1. Menyaring air kotor dengan alat")
    print("2. Sungai / air mengalir")
    print("3. Dari tumbuhan")

    pil = input("Masukkan nomor (q untuk keluar): ").strip()
    if pil.lower() == "q":
        return

    if not pil.isdigit():
        print(f"{layout.font.abang}Input salah{layout.font.clear()}")
        return

    pil = int(pil)
    if pil not in (1,2,3):
        print(f"{layout.font.abang}Pilihan tidak tersedia{layout.font.clear()}")
        return

    if pil == 1:
        alat = "Penyaring air"
        it = cek_item(alat)
        if not it:
            print(f"{layout.font.abang}Anda tidak punya {alat}{layout.font.clear()}")
            return

        print("Mengambil air...")
        time.sleep(3)
        print("Menyaring air...")
        time.sleep(4)

        if not ambil_item(alat):
            print(f"{layout.font.abang}Gagal memproses alat{layout.font.clear()}")
            return

        tambah_air()
        print("Anda mendapatkan Air bersih (+1).")

    if pil == 2:
        alat = "Potongan Bambu"
        it = cek_item(alat)
        if not it:
            print(f"{layout.font.abang}Anda tidak punya {alat}{layout.font.clear()}")
            return

        print("Mencari sumber air mengalir...")
        time.sleep(6)
        print("Mengambil air...")
        time.sleep(4)

        if not ambil_item(alat):
            print(f"{layout.font.abang}Gagal memproses Potongan Bambu{layout.font.clear()}")
            return

        tambah_air()
        print("Anda mendapatkan Air bersih (+1).")

    if pil == 3:
        alat1 = "Pisau batu"
        alat2 = "Potongan Bambu"

        it1 = cek_item(alat1)
        it2 = cek_item(alat2)

        if not it1 or not it2:
            print(f"{layout.font.abang}Butuh {alat1} dan {alat2} untuk metode ini{layout.font.clear()}")
            return

        print(f"{layout.font.kuneng}Hati-hati: hindari tumbuhan bergetah putih, pahit, atau berwarna mencolok karena bisa beracun.{layout.font.clear()}")
        print("Mencari tumbuhan berair...")
        time.sleep(8)
        print("Mengambil air...")
        time.sleep(5)

        if not ambil_item(alat1) or not ambil_item(alat2):
            print(f"{layout.font.abang}Gagal mengurangi alat dari inventory{layout.font.clear()}")
            return

        tambah_air()
        print("Anda mendapatkan Air bersih (+1).")

    try:
        layout.font.clear()
    except:
        pass