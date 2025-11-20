#file utama (smkn kare)
import time
import arts
from data import dk
import layout
import scene

print(f"{layout.font.ijo}")
while True:
	
	layout.font.clear()
	arts.logo.anLogo()
	
	print("[1] New game\n[2] Load game\n[3] About")
	jawBeranda = input("Masukkan angka pilihan : ")
		
	if jawBeranda == '1':
		layout.font.clear()
		dk.cur.execute("SELECT EXISTS(SELECT 1 FROM user)")
		cekUser = dk.cur.fetchone()[0]
		
		if cekUser == 0:
			layout.font.clear()
			jawNama = input("Masukkan username : ")
			queryNama = "INSERT INTO user ('nama') VALUES (?)"
			dk.cur.execute(queryNama, (jawNama,))
			dk.db.commit()
			arts.anBoat.anBoat()
			scene.cerita.cerita()
			scene.play.play()
			
		elif cekUser == 1:
			kondisi = 1
			while True:
				layout.font.clear()
				print(f"{layout.font.kuneng}Anda sudah pernah bermain, apakah anda yakin ingin menghapus dan menambahkan data baru?{layout.font.reset}")
				print()
				print(f"[1] Lanjut menghapus dan membuat data")
				print(f"[2] {layout.font.ijo}kembali untuk load data game{layout.font.reset}")
				jawBaru = input("Masukkan angka pilihan : ")
				if jawBaru == '1':
					dk.cur.execute("DELETE FROM user")
					dk.cur.execute("DELETE FROM user_fish")
					dk.cur.execute("DELETE FROM user_inventory")
					dk.cur.execute("DELETE FROM user_forefoods")
					dk.cur.execute("DELETE FROM user_foods")
					dk.cur.execute("DELETE FROM user_achievement")
					
					dk.db.commit()
					print(f"{layout.font.kuneng}delete...{layout.font.reset}")
					time.sleep(1)
					break
				elif jawBaru == '2':
					print(f"{layout.font.kuneng}loading...{layout.font.reset}")
					time.sleep(1)
					layout.font.clear()
					break
				else:
					print(layout.font.errorInput())
	elif jawBeranda == '2':
		dk.cur.execute("SELECT EXISTS(SELECT 1 FROM user)")
		cekUser = dk.cur.fetchone()[0]

		if cekUser == None or cekUser == 0:
			print(f"{layout.font.abang}Anda belum memiliki data, buat data di nomor 1{layout.font.reset}")
			time.sleep(4)
		else:
			layout.font.clear()
			print(f"{layout.font.kuneng}loading...{layout.font.reset}")
			time.sleep(1)
			scene.play.play()
	elif jawBeranda == '3':
		print(f"╭______________ ABOUT ____________╮")
		print()
		print("GAME : stranded (terdampar)\nDEKS : Game ini bercerita tentang\n       sesorang yang ingin pulang ke\n       desanya tetapi mengalami peristiwa buruk yang\n       membuatnya harus bertahan hidup\nTUJUAN : mengajarkan kepada pengguna\n       cara bertahan hidup di alam mengenalkan pengguna\n       kepada komponen² yang ada di alam\nCREATOR : Nawa alsaprise & Ridhwan rizqullloh\n")
		print("╭_________________________________╮")
		print()
		input("Enter untuk kembali!")