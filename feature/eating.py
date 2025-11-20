import arts
from data import dk
import time
import layout

def eating():
    def tampil_mknan():
        layout.font.clear()
        print("Pilih makanan atau minuman")
        dk.cur.execute("SELECT * FROM user_foods")
        lst = dk.cur.fetchall()
        no = 1
        print("◆ ▬▬▬▬ ❴ PILIHAN ❵ ▬▬▬▬ ◆")
        for d in lst:
            print(f"{no}. {d[1]}   Kenyang/lega:{d[2]}%   Jml:{d[3]}")
            no += 1
        
        print("◆ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ◆")
        return lst

    def pilih_mknan(lst):
        try:
            p = int(input("Masukkan nomor: "))
            if p < 1 or p > len(lst):
                print(f"{layout.font.abang}Pilihan tidak ada!")
                return None
            return lst[p-1]
        except:
            print(f"{layout.font.abang}Masukkan angka!")
            return None

    def ubah_jml(nm, jml):
        sisa = jml - 1
        if sisa > 0:
            dk.cur.execute("UPDATE user_foods SET jumlah=? WHERE nama=?", (sisa, nm))
        else:
            dk.cur.execute("DELETE FROM user_foods WHERE nama=?", (nm,))
        dk.db.commit()

    def ambil_user():
        dk.cur.execute("SELECT * FROM user")
        return dk.cur.fetchone()

    def halusinasi():
        arts.forest.toPlane()
        time.sleep(1)

    lst = tampil_mknan()
    if not lst:
        print(f"{layout.font.kuneng}Tidak ada makanan!")
        time.sleep(2)
        layout.font.clear()
        return

    d = pilih_mknan(lst)
    if d is None:
        return

    nama_item = d[1]
    kenyang_item = d[2]
    jumlah_item = d[3]

    ubah_jml(nama_item, jumlah_item)

    usr = ambil_user()
    nama_user = usr[1]
    kesehatan = usr[2]
    energi = usr[3]
    haus = usr[4]

    if nama_item.lower() == "air bersih":
        new_haus = haus + kenyang_item
        if new_haus > 100:
            new_haus = 100
        dk.cur.execute("UPDATE user SET kehausan=? WHERE nama=?", (new_haus, nama_user))
        dk.db.commit()
        print(f"Anda meminum {nama_item}. Rasa haus berkurang {kenyang_item}")
        print()
        print("Saran, air dimasak di panci sampai suhu memanas lalu didinginkan untuk mengurangi bakteri di dalamnya.")
        time.sleep(4)
        return

    if kenyang_item == 0:
        new_kesehatan = kesehatan - 5
        dk.cur.execute("UPDATE user SET kesehatan=? WHERE nama=?", (new_kesehatan, nama_user))
        dk.db.commit()
        print(f"{layout.font.abang}Perutmu sakit! {nama_item} berbahaya!")
        time.sleep(5)
        halusinasi()
        return

    if energi >= 100:
        if kesehatan >= 100:
            print(f"{layout.font.kuneng}Anda tidak lapar!")
            return
        new_kesehatan = kesehatan + 5
        if new_kesehatan > 100:
            new_kesehatan = 100
        dk.cur.execute("UPDATE user SET kesehatan=? WHERE nama=?", (new_kesehatan, nama_user))
        dk.db.commit()
        print("Kesehatan bertambah")
        return

    if energi + kenyang_item >= 100:
        new_energi = 100
        dk.cur.execute("UPDATE user SET energi=? WHERE nama=?", (new_energi, nama_user))
        dk.db.commit()
        new_kesehatan = kesehatan + 5
        if new_kesehatan > 100:
            new_kesehatan = 100
        dk.cur.execute("UPDATE user SET kesehatan=? WHERE nama=?", (new_kesehatan, nama_user))
        dk.db.commit()
        print("Energi penuh + kesehatan naik")
        return

    new_energi = energi + kenyang_item
    dk.cur.execute("UPDATE user SET energi=? WHERE nama=?", (new_energi, nama_user))
    dk.db.commit()
    print(f"Anda memakan {nama_item}. Energi naik {kenyang_item}")