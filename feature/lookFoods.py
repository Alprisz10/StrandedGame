
import time
from data import dk
import feature
import random
import arts
import layout

def clear():
	print("\033[2J\033[H", end="")

def anSearch():
	anCari = ["Mencari.","Mencari..","Mencari...","Mencari."]
	for hsil in anCari:
		print(layout.font.kuneng,hsil,layout.font.reset)
		time.sleep(1)
		clear()
	dk.cur.execute("SELECT * FROM inven_forefoods")
	isi = dk.cur.fetchall()
	random.shuffle(isi)
	if isi:
		while True:
			hasil = isi[1][1]
			print("Anda mendapatkan satu",hasil,"dari",isi[1][3])
			print("[1] Simpan\n[2] Buang")
			jawDapat = input("Masukkan pilihan : ")
			if jawDapat == '1':
				queryCek = "SELECT EXISTS(SELECT * FROM user_forefoods WHERE nama = ?)"
				dk.cur.execute(queryCek, (hasil,))
				cekItems = dk.cur.fetchone()[0]
				if cekItems == 1:
					queryCekjumlah = "SELECT jumlah FROM user_forefoods WHERE nama = ?"
					dk.cur.execute(queryCekjumlah,(hasil,))
					jumlah = dk.cur.fetchone()[0]
					tambahJumlah = jumlah + 1
					queryTambahjumlah = "UPDATE user_forefoods SET jumlah = ? WHERE nama = ?"
					dk.cur.execute(queryTambahjumlah, (tambahJumlah, hasil,))
					dk.db.commit()
					break
				else:
					queryTambah = "INSERT INTO user_forefoods ('id','nama','jumlah','kekenyangan') VALUES  (?,?,?,?)"
					dk.cur.execute(queryTambah, (isi[1][0],isi[1][1],1,isi[1][4]))
					dk.db.commit()
					break
			elif jawDapat == '2':
				clear()
				break
			else:
				clear()
				print(f"{layout.font.abang}[!] Anda memasukkan pilihan yang tidak sesuai [!]{layout.font.reset}")
				time.sleep(1)
				
	else:
		print("Anda tidak mendapatkan apa²")
	
def lookFoods():
	feature.thirsty.startKehausan()
	while True:
		layout.font.clear()
		arts.forest.forest()
		print()
		layout.bar.bar()
		print(f"\n{layout.font.ijo}Cara memilih makanan layak makan di hutan{layout.font.kuneng}\n1. Buah:\n   Aman jika tidak terlalu mencolok, tidak berbau aneh, tidak ada getah putih. Lihat hewan makan, tapi tetap hati-hati.\n2. Jamur:\n   Hindari jika tidak ahli. Banyak yang mirip tapi beracun.\n3. Hewan/Ikan:\n   Aman jika masih segar, tidak bau, daging tidak lembek.\n4. Serangga:\n   Aman jika tidak berwarna cerah, tidak berbulu, dan dimasak dulu.\n5. Daun/Akar:\n   Hindari yang pahit, bergetah putih, atau menyebabkan gatal.\n6. Air:\n   Ambil dari air mengalir dan rebus dulu.\nAturan utama:\n   Jika ragu → jangan dimakan.{layout.font.reset}")
		print()
		print("Mencari sumber daya akan menguras 8% energi, apakah mau lanjut?")
		print("[1] Ya, lanjut\n[2] Tidak jadi, kembali saja")
		jawsearchForestFood = input("Masukkan pilihan anda : ")
		if jawsearchForestFood == '1':
			dk.cur.execute("SELECT energi FROM user")
			energi = dk.cur.fetchone()[0]
			if energi < 10:
				print(f"{layout.font.abang}[!] Energi anda tidak cukup [!]{layout.font.reset}")
				time.sleep(1)
			else:
				jumlahEnergi = energi - 10
				queryUpenergi = "UPDATE user SET energi = ?"
				dk.cur.execute(queryUpenergi, (jumlahEnergi,))
				anSearch()
		elif jawsearchForestFood == '2':
			layout.font.clear()
			break
		else:
			clear()
			print(f"{layout.font.abang}[!] Anda memasukkan pilihan yang tidak sesuai [!]{layout.font.reset}")
			time.sleep(1)