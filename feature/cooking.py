import time
import layout
import arts
from data import dk

def conKenyang(k):
    if k == 1:
        return 10
    if k == 2:
        return 20
    if k == 3:
        return 30
    return 0

def inpUfood(namFood, kekenyangan):
    namaMatang = namFood + " matang"
    dk.cur.execute("SELECT * FROM user_foods WHERE nama=?", (namaMatang,))
    ada = dk.cur.fetchone()
    if ada:
        dk.cur.execute("UPDATE user_foods SET jumlah = jumlah + 1 WHERE nama=?", (namaMatang,))
    else:
        dk.cur.execute("INSERT INTO user_foods (nama, kekenyangan, jumlah) VALUES (?, ?, 1)", (namaMatang, kekenyangan))
    dk.db.commit()

def konItems(table, id_data, jumlah):
    if jumlah > 1:
        dk.cur.execute(f"UPDATE {table} SET jumlah = jumlah - 1 WHERE id=?", (id_data,))
    else:
        dk.cur.execute(f"DELETE FROM {table} WHERE id=?", (id_data,))
        dk.cur.execute("INSERT INTO user_inventory ('id','nama','didapatkan','jumlah','jenis') VALUES (11, 'Arang','Bekas pembakaran',3,'items')")
    dk.db.commit()

def cekInvItem(nama_item):
    dk.cur.execute("SELECT * FROM user_inventory WHERE nama=?", (nama_item,))
    return dk.cur.fetchone()

def pakaiInvItem(nama_item):
    item = cekInvItem(nama_item)
    if not item:
        return False

    idd = item[0]
    jumlah = item[2]

    if jumlah > 1:
        dk.cur.execute("UPDATE user_inventory SET jumlah = jumlah - 1 WHERE id=?", (idd,))
    else:
        dk.cur.execute("DELETE FROM user_inventory WHERE id=?", (idd,))
    dk.db.commit()
    return True

def cooking():
    while True:
        dk.cur.execute("SELECT * FROM user_fish")
        fish_list = dk.cur.fetchall()

        dk.cur.execute("SELECT * FROM user_forefoods")
        forefoods_list = dk.cur.fetchall()

        print("Anda ingin memasak menggunakan apa?\n[1] Perapian (Bakar/kukus)\n[2] Bambu (Pemasakan dalam bambu)\n[3] Keluar")
        jawCookMethod = input("Masukkan angka pilihan anda : ")

        if jawCookMethod == '1':
            if not cekInvItem("Perapian"):
                layout.font.clear()
                print(f"{layout.font.abang}[!] Anda tidak memiliki Perapian [!]{layout.font.reset}")
                continue

            layout.font.clear()
            print("Pembakaran langsung lebih cocok untuk makan daging!")
            jawPickMethod = input("\n[1] Lanjut menggunakan teknik ini\n[2] Kembali saja\nMasukkan angka pilihan anda : ")

            if jawPickMethod == '1':
                if not pakaiInvItem("Perapian"):
                    layout.font.clear()
                    print(f"{layout.font.abang}[!] Anda tidak memiliki Perapian [!]{layout.font.reset}")
                    continue

                print("\n=== PILIH IKAN YANG MAU DIBAKAR ===")
                if len(fish_list) == 0:
                    layout.font.clear()
                    print(f"{layout.font.abang}[!] Anda tidak memiliki ikan [!]{layout.font.reset}")
                else:
                    for i, fish in enumerate(fish_list, start=1):
                        print(f"[{i}] {fish[1]} ({fish[3]}x)")

                    pilih = input("Masukkan nomor ikan : ")

                    if pilih.isdigit():
                        pilih = int(pilih)
                        if 1 <= pilih <= len(fish_list):
                            data = fish_list[pilih - 1]
                            id_data = data[0]
                            nama_data = data[1]
                            kekenyangan_data = conKenyang(data[2])
                            jumlah_data = data[3]

                            konItems("user_fish", id_data, jumlah_data)
                            inpUfood(nama_data, kekenyangan_data)

                            print(f"{nama_data} matang berhasil dibuat!")

        elif jawCookMethod == '2':
            if not cekInvItem("Potongan bambu"):
                layout.font.clear()
                print(f"{layout.font.abang}[!] Anda tidak memiliki Potongan bambu di inventory [!]{layout.font.reset}")
                continue

            layout.font.clear()
            print("Pengkukusan menggunakan bambu lebih cocok untuk memasak tumbuhan")
            jawPickMethod = input("\n[1] Lanjut menggunakan teknik ini\n[2] Kembali saja\nMasukkan angka pilihan anda : ")

            if jawPickMethod == '1':
                if not pakaiInvItem("Potongan bambu"):
                    layout.font.clear()
                    print(f"{layout.font.abang}[!] Anda tidak memiliki Potongan bambu [!]{layout.font.reset}")
                    continue

                print("\n=== PILIH MAKANAN HUTAN YANG MAU DIMASAK ===")
                if len(forefoods_list) == 0:
                    layout.font.clear()
                    print(f"{layout.font.abang}[!] Anda tidak memiliki makanan hutan [!]{layout.font.reset}")
                else:
                    for i, item in enumerate(forefoods_list, start=1):
                        print(f"[{i}] {item[1]} ({item[3]}x)")

                    pilih = input("Masukkan nomor makanan : ")

                    if pilih.isdigit():
                        pilih = int(pilih)
                        if 1 <= pilih <= len(forefoods_list):
                            data = forefoods_list[pilih - 1]
                            id_data = data[0]
                            nama_data = data[1]
                            kekenyangan_data = conKenyang(data[2])
                            jumlah_data = data[3]

                            konItems("user_forefoods", id_data, jumlah_data)
                            inpUfood(nama_data, kekenyangan_data)

                            print(f"{nama_data} matang berhasil dibuat!")

        elif jawCookMethod == '3':
            layout.font.clear()
            break

        else:
            layout.font.clear()
            print(f"{layout.font.abang}[!] Anda memasukkan pilihan yang tidak sesuai [!]{layout.font.reset}")