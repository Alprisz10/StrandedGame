
import time
from data import dk
import layout
import random
import feature
import arts

def anSearch():
	anSearching = ["Mencari.","Mencari..","Mencari...","Mencari."]
	loop = 0
	while loop < 4:
		print(f"{layout.font.kuneng}{anSearching[loop]}{layout.font.reset}")
		loop = loop + 1
		time.sleep(1)
		layout.font.clear()
	dk.cur.execute("SELECT * FROM inven_items")
	isi = dk.cur.fetchall()
	random.shuffle(isi)
	if isi:
		while True:
			hasil = isi[1][1]
			print("Anda mendapatkan satu",hasil,"dari",isi[1][3])
			print("[1] Simpan\n[2] Buang")
			jawDapat = input("Masukkan pilihan : ")
			if jawDapat == '1':
				queryCek = "SELECT EXISTS(SELECT * FROM user_inventory WHERE nama = ?)"
				dk.cur.execute(queryCek, (hasil,))
				cekItems = dk.cur.fetchone()[0]
				if cekItems == 1:
					queryCekjumlah = "SELECT jumlah FROM user_inventory WHERE nama = ?"
					dk.cur.execute(queryCekjumlah,(hasil,))
					jumlah = dk.cur.fetchone()[0]
					tambahJumlah = jumlah + 1
					queryTambahjumlah = "UPDATE user_inventory SET jumlah = ? WHERE nama = ?"
					dk.cur.execute(queryTambahjumlah, (tambahJumlah, hasil,))
					dk.db.commit()
					break
				else:
					queryTambah = "INSERT INTO user_inventory ('id','nama','jumlah','didapatkan','manfaat','jenis') VALUES  (?,?,?,?,?,?)"
					dk.cur.execute(queryTambah,(isi[1][0],isi[1][1],1, isi[1][3], isi[1][2],'items',))
					dk.db.commit()
					break
			elif jawDapat == '2':
				break
			else:
				layout.font.clear()
				print("[!] Anda memasukkan pilihan yang tidak sesuai [!]")
				time.sleep(1)
				
	else:
		print("Anda tidak mendapatkan apa²")
	
def searching():
	feature.thirsty.startKehausan()
	while True:
		layout.font.clear()
		arts.forest.forest()
		print()
		layout.bar.bar()
		print()
		print("Mencari sumber daya akan menguras 2% energi anda, apakah mau lanjut?")
		print("[1] Ya, lanjut\n[2] Tidak jadi, kembali saja")
		jawSearching = input("Masukkan pilihan anda : ")
		if jawSearching == '1':
			dk.cur.execute("SELECT energi FROM user")
			energi = dk.cur.fetchone()[0]
			if energi < 5:
				print("Energi anda tidak cukup!!")
				time.sleep(1)
			else:
				jumlahEnergi = energi - 2
				queryUpenergi = "UPDATE user SET energi = ?"
				dk.cur.execute(queryUpenergi, (jumlahEnergi,))
				anSearch()
		elif jawSearching == '2':
			layout.font.clear()
			break
		else:
			layout.font.clear()
			print("[!] Anda memasukkan pilihan yang tidak sesuai [!]")
			time.sleep(1)