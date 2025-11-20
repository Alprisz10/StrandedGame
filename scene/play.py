import arts
import feature
import layout
import threading
import time
import scene

def play():
    feature.thirsty.startKehausan()
    while True:
        print(f"{layout.font.ijo}")
        arts.forest.forest()
        print()
        layout.bar.bar()
        print()
        print("[1] Aktifitas\n[2] Inventory\n[3] Bantuan\n[4] Keluar\n[•] Enter untuk refresh bar")
        jawPlay = input("Masukkan pilihan : ")

        if jawPlay == '1':
            layout.font.clear()
            while True:
                arts.forest.forest()
                print()
                layout.bar.bar()
                print()
                print("[1] Cari sumber daya\n[2] Kerajinan\n[3] Memancing\n[4] Mencari air\n[5] Mencari makanan hutan\n[6] Memasak\n[7] Makan/Minum\n[8] Pembuatan rakit (end)\n[•] Enter untuk refresh bar")
                jawAktifitas = input("Masukkan pilihan (q untuk keluar): ")
                if jawAktifitas == '1':
                    feature.searching.searching()
                elif jawAktifitas == '2':
                    layout.font.clear()
                    feature.crafting.crafting()
                elif jawAktifitas == '3':
                    layout.font.clear()
                    feature.fishing.fishing()
                elif jawAktifitas == '4':
                    layout.font.clear()
                    feature.lookWater.lookWater()
                elif jawAktifitas == '5':
                    layout.font.clear()
                    feature.lookFoods.lookFoods()
                if jawAktifitas == '6':
                    layout.font.clear()
                    feature.cooking.cooking()
                elif jawAktifitas == '7':
                    layout.font.clear()
                    feature.eating.eating()
                elif jawAktifitas == '8':
                    layout.font.clear()
                    scene.end.end()
                elif jawAktifitas == 'q':
                    layout.font.clear()
                    break
                elif jawAktifitas == '':
                    layout.font.clear()
                    print(f"{layout.font.kuneng}Telah dirifresh!{layout.font.reset}")
                    continue
        elif jawPlay == '2':
            layout.font.clear()
            feature.inventory.inventory()
        elif jawPlay == '4':
            break
        elif jawPlay == '':
            layout.font.clear()
            print(f"{layout.font.kuneng}Telah dirifresh!{layout.font.reset}")
            continue
        else:
            layout.font.clear()
            print(layout.font.errorInput())
            continue
        