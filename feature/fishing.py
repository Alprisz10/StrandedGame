import time
from data import dk
import random
import layout
import arts

def oracle():
	an = "              .---.         ,,",
	"   ,,        /     \       ;,,'",
	"  ;, ;      (  o  o )      ; ;",
	"    ;,';,,,  \  \/ /      ,; ;",
	" ,,,  ;,,,,;;,`   '-,;'''',,,'",
	";,, ;,, ,,,,   ,;  ,,,'';;,,;''';",
	"   ;,,,;    ~~'  '';,,''',,;''''",
	"                      '''",
	for sil in an:
		print(layout.font.abang, sil)
	

def fishingStart():
	print()
	input("Klik enter sebanyak mungkin untuk melempar kail dengan kekuatan penuh!\nKlik [enter] untuk lanjut")
	layout.font.clear()
	print("PERSIAPAN!!!")
	time.sleep(1.5)
	layout.font.clear()
	print("Satu!")
	time.sleep(1)
	layout.font.clear()
	print("Dua!")
	time.sleep(1)
	layout.font.clear()
	print("MULAI!!!!")
	time.sleep(0.25)
	layout.font.clear()
	
	setMulai = time.time()
	waktuBerhenti = 5
	poinKekuatan = 0
	
	while time.time() - setMulai < waktuBerhenti:
		input("Klik Enter!")
		poinKekuatan = poinKekuatan + 1
		layout.font.clear()
		
	hasilFish = 0
		
	if poinKekuatan < 30:
		print(f"Kail berhasil dilempar!")
		print(f"{layout.font.kuneng}[ System ] : {layout.font.reset}Bwahaha, Lemparan apa itu lemah banget!")
		dk.cur.execute("SELECT * FROM inven_fish WHERE kedalaman = 10")
		fishDasar = dk.cur.fetchall()
		random.shuffle(fishDasar)
		hasilFish = fishDasar[1]
	elif poinKekuatan > 30 and poinKekuatan < 40:
		print(f"Kail berhasil dilempar!")
		print(f"{layout.font.kuneng}[ System ] : {layout.font.reset}Lumayan juga lemparanmh!")
		dk.cur.execute("SELECT * FROM inven_fish WHERE kedalaman = 50")
		fishSedang = dk.cur.fetchall()
		random.shuffle(fishSedang)
		hasilFish = fishSedang[1]
	elif poinKekuatan > 40:
		print(f"Kail berhasil dilempar!")
		print(f"{layout.font.kuneng}[ System ] : {layout.font.reset}Wah wah anda pantas disebut legend!")
		dk.cur.execute("SELECT * FROM inven_fish WHERE kedalaman = 100")
		fishDalam = dk.cur.fetchall()
		random.shuffle(fishDalam)
		hasilFish = fishDalam[1]
	
	time.sleep(3)
	arts.anFishing.waitFishing()
	layout.font.clear()
	print("STRIKE!!")
	time.sleep(1.5)
	print()
	while True:
		arts.anFishing.strikeFish()
		print(f"Anda mendapatkan {hasilFish[2]} \n{hasilFish[3]} \nHabitat : {hasilFish[1]}, {hasilFish[4]}")
		print("[1] Simpan\n[2] Rilis")
		jawStrike = input("Masukkan angka pilihanmu : ")
		if jawStrike == '1':
			queryCekfish = "SELECT EXISTS(SELECT * FROM user_fish WHERE nama = ?)"
			dk.cur.execute(queryCekfish, (hasilFish[2],))
			hasCekfish = dk.cur.fetchone()[0]
			print("Ikan telah ditambahkan!")
			layout.font.clear()
			if hasCekfish == 0:
				queryAddfish = "INSERT INTO user_fish ('id','nama','jumlah','kekenyangan') VALUES  (?,?,?,?)"
				dk.cur.execute(queryAddfish, (hasilFish[0], hasilFish[2], 1,hasilFish[6]))
				dk.db.commit()
				break
			else:
				queryCekjumlah = "SELECT jumlah FROM user_fish WHERE nama = ?"
				dk.cur.execute(queryCekjumlah,(hasilFish[2],))
				jumlah = dk.cur.fetchone()[0]
				tambahJumlah = jumlah + 1
				queryTambahjumlah = "UPDATE user_inventory SET jumlah = ? WHERE nama = ?"
				dk.cur.execute(queryTambahjumlah, (tambahJumlah, hasilFish[2],))
				dk.db.commit()
				break
			
		elif jawStrike == '2':
			break
		else:
			layout.font.clear()
			print(f"{layout.font.abang}[!] Anda memasukkan pilihan yanh tidak sesuai [!]{layout.font.reset}")
			time.sleep(1)
			
def cekFishingrod():
	dk.cur.execute("SELECT jumlah FROM user_inventory WHERE nama = 'Pancing ikan'")
	hasCektahan = dk.cur.fetchone()[0]
	
	if hasCektahan == 1:
		dk.cur.execute("DELETE FROM user_inventory WHERE nama = 'Pancing ikan'")
		dk.db.commit()
	else:
		kurFishingrod = hasCektahan - 1
		queryUptahan ="UPDATE user_inventory SET jumlah = ? WHERE nama = 'Pancing ikan'"
		dk.cur.execute(queryUptahan, (kurFishingrod,))
		dk.db.commit()
	
	fishingStart()
	
def fishingTrue():
	while True:
		print("Memancing akan menguras 10% tenaga, dan merusak pancing sebesar 7%")
		print("[1] Lanjut memancing\n[2] Tidak jadi, kembali saja")
		jawFishing = input("Masukkan angka pilihanmu : ")
		
		if jawFishing == '1':
			dk.cur.execute("SELECT energi FROM user")
			energi = dk.cur.fetchone()[0]
			if energi < 10:
				print("Energi anda tidak cukup!!")
				time.sleep(1)
			else:
				jumlahEnergi = energi - 10
				queryUpenergi = "UPDATE user SET energi = ?"
				dk.cur.execute(queryUpenergi, (jumlahEnergi,))
				cekFishingrod()
		elif jawFishing == '2':
			break
		else:
			layout.font.clear()
			print(f"{layout.font.abang}[!] Anda memasukkan pilihan yang tidak sesuai [!]{layout.font.reset}")
			time.sleep(1)

def fishing():
	oracle()
	dk.cur.execute("SELECT EXISTS(SELECT * FROM user_inventory WHERE nama = 'Pancing ikan')")
	hasCekpan = dk.cur.fetchone()[0] 
	if hasCekpan == 0:
		print(f"{layout.font.abang}[!] Anda tidak memiliki pancing ikan [!]{layout.font.reset}")
	else:
		fishingTrue()