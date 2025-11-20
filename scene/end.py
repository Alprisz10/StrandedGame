import time
from data import dk
import layout
import arts

def end():
    layout.font.clear()
    print("Syarat dan bahan pembuatan rakit\n   1. 25 Batu\n   2. 30 Pelepah\n   3. 15 Ranting\n 4. Memiliki 5 jenis makanan")
    print()
    input("Klik enter untuk lanjut")
    print(f"{layout.font.kuneng}Cek persyaratan...{layout.font.reset}")
    time.sleep(1)

    dk.cur.execute("SELECT COUNT(DISTINCT nama) FROM user_foods")
    jml_mkn = dk.cur.fetchone()[0]

    if jml_mkn < 5:
        layout.font.clear()
        print(f"{layout.font.abang}Persyaratan belum terpenuhi! (Jenis makanan kurang){layout.font.reset}")
        time.sleep(2)
        return
    
    Batu = 0
    Pelepah = 0
    Ranting = 0

    dk.cur.execute("SELECT jumlah FROM user_inventory WHERE nama='Pelepah Pisang'")
    p_result = dk.cur.fetchone()
    if p_result:
        Pelepah = p_result[0]
    
    dk.cur.execute("SELECT jumlah FROM user_inventory WHERE nama='Ranting/Kayu'")
    r_result = dk.cur.fetchone()
    if r_result:
        Ranting = r_result[0]
    
    dk.cur.execute("SELECT jumlah FROM user_inventory WHERE nama='Batu'")
    b_result = dk.cur.fetchone()
    if b_result: 
        Batu = b_result[0]
    
    
    if Batu < 25 or Pelepah < 30 or Ranting < 15:
        layout.font.clear()
        print(f"{layout.font.abang}Bahan kurang! (Batu: {Batu}/25, Pelepah: {Pelepah}/30, Ranting: {Ranting}/15){layout.font.reset}")
        time.sleep(2)
        return

    langkah = [
        "Pergi mencari bambu tua yang kuat",
        "Memotong bambu memakai batu tajam",
        "Membersihkan ruas bambu untuk diratakan",
        "Mengumpulkan pelepah pisang untuk tali ikat",
        "Mengambil ranting untuk penopang awal",
        "Menyusun bambu sejajar di tanah",
        "Mengikat dua sisi bambu dengan pelepah pisang",
        "Menambah ikatan silang biar kuat",
        "Meratakan bagian bawah rakit dengan ranting",
        "Mengencangkan semua ikatan terakhir",
        "Menguji kekuatan rakit dengan menekan bagian tengah",
        "Mendorong rakit ke sungai perlahan"
    ]

    jeda = 100 / len(langkah) / 10

    for l in langkah:
        layout.font.clear()
        print(f"{layout.font.cyan}{l}{layout.font.reset}")
        time.sleep(jeda)

    dk.cur.execute("UPDATE user_inventory SET jumlah = jumlah - 25 WHERE nama='Batu'")
    dk.cur.execute("UPDATE user_inventory SET jumlah = jumlah - 30 WHERE nama='Pelepah Pisang'")
    dk.cur.execute("UPDATE user_inventory SET jumlah = jumlah - 15 WHERE nama='Ranting/Kayu'")

    dk.cur.execute("DELETE FROM user_inventory WHERE jumlah <= 0")

    dk.db.commit()
    
    layout.font.clear()
    print(f"{layout.font.ijo}Rakit bambu selesai dibuat!{layout.font.reset}")
    time.sleep(1)
    layout.font.clear()
    print("Anda keluar dari pulau!!")
    arts.anEnd.anEnd()
    time.sleep(2)
