import time
from data import dk
import layout
import arts

def inventory():
	while True:
		layout.font.clear()
		print("[1] Makanan mentah\n[2] Makanan matang\n[3] Peralatan\n[4] Item\n[5] Pencapaian\n[6] Kembali")
		jawInven = input("Masukkan angka pilihan anda : ")
		print(f"{layout.font.cyan}")
		if jawInven == '1':
			print()
			print("◆ ▬▬▬▬ ❴ MAKANAN MENTAH ❵ ▬▬▬▬ ◆")
			dk.cur.execute("SELECT * FROM user_fish")
			invenFish = dk.cur.fetchall()
			print("[•] IKAN MENTAH")
			if invenFish == None or len(invenFish) == 0:
				print("Tidak memiliki ikan!")
			else:
				panInvenfish = len(invenFish)
				varWadh = 0
				while varWadh <= panInvenfish - 1:
					print(f"[{varWadh + 1}] {invenFish[varWadh][1]} ({invenFish[varWadh][3]}x)")
					varWadh = varWadh + 1
				
			print()
			dk.cur.execute("SELECT * FROM user_foreFoods")
			invenForefoods = dk.cur.fetchall()
			print("[•] MAKANAN HUTAN")
			if invenFish == None or len(invenForefoods) == 0:
				print("Tidak memiliki makanan hutan!")
			else:
				panInvenfore = len(invenForefoods)
				varWadh = 0
				while varWadh <= panInvenfore - 1:
					print(f"[{varWadh + 1}] {invenForefoods[varWadh][1]} ({invenForefoods[varWadh][3]}x)")
					varWadh = varWadh + 1
			print("◆ ▬▬▬▬▬▬▬▬ ❴ ✪ ❵ ▬▬▬▬▬▬▬▬ ◆")
			input("Klik Enter untuk menutup!")
					
		elif jawInven == '2':
			print()
			print("◆ ▬▬▬▬ ❴ MAKANAN MATANG ❵ ▬▬▬▬ ◆")
			dk.cur.execute("SELECT * FROM user_foods")
			invenFoods = dk.cur.fetchall()
			if invenFoods == None or len(invenFoods) == 0:
				print("Tidak memiliki makanan matang")
			else:
				panFoods = len(invenFoods)
				varWadh = 0
				while varWadh < panFoods:
					print(f"[{varWadh +1}] {invenFoods[varWadh][1]} ({invenFoods[varWadh][3]}x)")
					varWadh = varWadh + 1
			print("◆ ▬▬▬▬▬▬▬▬ ❴ ✪ ❵ ▬▬▬▬▬▬▬▬ ◆")
				
			input("Klik enter untuk menutup!")
			
		elif jawInven == '3':
			print()
			print("◆ ▬▬▬▬ ❴ PERALATAN ❵ ▬▬▬▬ ◆")
			dk.cur.execute("SELECT * FROM user_inventory WHERE jenis = 'tools'")
			invenTools = dk.cur.fetchall()
			if invenTools == None or len(invenTools) == 0:
				print("Tidak memiliki peralatan")
			else:
				panTools = len(invenTools)
				varWadh = 0
				while varWadh < panTools:
					print(f"[{varWadh +1}] {invenTools[varWadh][1]} ({invenTools[varWadh][2]}0%)")
					varWadh = varWadh + 1
			print("◆ ▬▬▬▬▬▬ ❴  •  ❵ ▬▬▬▬▬▬ ◆")
			input("Klik enter untuk menutup!")
			
		elif jawInven == '5':
			print()
			print("◆ ▬▬▬▬ ❴ PENCAPAIAN ❵ ▬▬▬▬ ◆")
			dk.cur.execute("SELECT * FROM user_inventory WHERE jenis = 'achievement'")
			invenAchiev = dk.cur.fetchall()
			if invenAchiev == None or len(invenAchiev) == 0:
				print("Tidak memiliki pencapaian")
			else:
				panAchiev = len(invenAchiev)
				varWadh = 0
				while varWadh < panAchiev:
					print(f"[{varWadh +1}] {invenAchiev[varWadh][1]} ({invenAchiev[varWadh][2]}x)")
					varWadh = varWadh + 1
			print("◆ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ◆")
			input("Klik enter untuk menutup!")
			
		elif jawInven == '4':
			print()
			print("◆ ▬▬▬▬▬ ❴ ITEMS ❵ ▬▬▬▬▬ ◆")
			dk.cur.execute("SELECT * FROM user_inventory WHERE jenis = 'items'")
			invenItems = dk.cur.fetchall()
			if invenItems == None or len(invenItems) == 0:
				print("Tidak memiliki items")
			else:
				panItems = len(invenItems)
				varWadh = 0
				while varWadh < panItems:
					print(f"[{varWadh +1}] {invenItems[varWadh][1]} ({invenItems[varWadh][2]}x)")
					varWadh = varWadh + 1
			print("◆ ▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ ◆")
			input("Klik enter untuk menutup!")
		elif jawInven == "6":
			layout.font.clear()
			break
		else:
			layout.font.clear()
			print(layout.font.errorInput())
			time.sleep(3)