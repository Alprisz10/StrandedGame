import arts
from data import dk
import time
import layout

def crafting():
    while True:
        layout.font.clear()
        arts.anCrafting.anCrafting()
        print("Anda ingin membuat apa?")
        print("[1] Pisau\n[2] Pancing\n[3] Alat pembuat api\n[4] Penyaring air\n[5] Tempat berlindung (Shelter)\n[6] Perapian")
        
        try:
            jawCrafting = int(input("Masukkan pilihan anda (0 untuk keluar): "))
            
            if jawCrafting == 0:
                layout.font.clear()
                break
            
            queryCektools = "SELECT * FROM inven_needs WHERE id = ?"
            dk.cur.execute(queryCektools, (jawCrafting,))
            hasil = dk.cur.fetchone()
            
            layout.font.clear()
            arts.anCrafting.anCraftingnol()

            bahan_list = [hasil[3], hasil[4], hasil[5], hasil[6]]
            bahan_list = [b for b in bahan_list if b != "-"]

            print(f"Membuat {hasil[1]}\nBahan bahan :")
            for i, b in enumerate(bahan_list, 1):
                print(f"   {i}. {b}")
            print(f"Cara pembuatan : {hasil[2]}")

            jawLanjutcraft = input(
                f"\nMembuat {hasil[1]} akan mengurangi 10% energi anda!\n"
                f"[1] Lanjut membuat {hasil[1]}\n[2] Kembali saja\nMasukkan nomor pilihan anda : "
            )

            if jawLanjutcraft != '1':
                continue

            layout.font.clear()
            dk.cur.execute("SELECT energi FROM user")
            energi = dk.cur.fetchone()[0]

            if energi < 10:
                print("Energi anda tidak cukup!!")
                time.sleep(1)
                break
            else:
                jumlahEnergi = energi - 10
                queryUpenergi = "UPDATE user SET energi = ?"
                dk.cur.execute(queryUpenergi, (jumlahEnergi,))
                dk.db.commit()

            cekItem = "SELECT jumlah FROM user_inventory WHERE nama = ?"
            delItem = "DELETE FROM user_inventory WHERE nama = ?"
            upJutem = "UPDATE user_inventory SET jumlah = ? WHERE nama = ?"

            bahan_tidak_ada = False
            jumlah_bahan = {}

            for bahan in bahan_list:
                dk.cur.execute(cekItem, (bahan,))
                cek = dk.cur.fetchone()
                if cek is None:
                    print(f"Anda tidak memiliki {bahan} yang dibutuhkan!")
                    bahan_tidak_ada = True
                    break
                jumlah_bahan[bahan] = cek[0]

            if bahan_tidak_ada:
                break

            for bahan in bahan_list:
                jumlah = jumlah_bahan[bahan]
                if jumlah == 1:
                    dk.cur.execute(delItem, (bahan,))
                else:
                    dk.cur.execute(upJutem, (jumlah - 1, bahan))
                dk.db.commit()
                
            if hasil[7] == 'achievement':
                queryTamtools = "INSERT INTO user_achievement (id, nama, jenis) VALUES (?,?,?)"
                dk.cur.execute(queryTamtools, (hasil[0], hasil[1], hasil[7]))
                dk.db.commit()
            else:
                queryTamtools = "INSERT INTO user_inventory (id, nama, jumlah, jenis) VALUES (?,?,?,?)"
                dk.cur.execute(queryTamtools, (hasil[0], hasil[1], 10, hasil[7]))
                dk.db.commit()

            arts.anCrafting.membuat()
            print(f"Anda memperoleh {hasil[1]}!!")
            time.sleep(1.5)

        except ValueError:
            print("Anda memasukkan salah")