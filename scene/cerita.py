import sys
import time
from data import dk
import layout
import arts



def tik(teks, lamb=0.1):
    
    for hrf in teks:
        sys.stdout.write(hrf)
        sys.stdout.flush()
        time.sleep(lamb)
    sys.stdout.write("\n")
    sys.stdout.flush()

def clr():
    layout.font.clear()
    
def cerita():
    dk.cur.execute("SELECT nama FROM user")
    hs = dk.cur.fetchone()[0]
    if hs:
        nama = hs
    else:
        nama = "Orang"

    rkit = [
    f"*wshhh wshhh wshhh... angin laut berhembus lembut*",
    f"{nama}: \"Wah... anginnya sejuk sekali. Perjalanan pulang hari ini terasa tenang...\"",
    f"*tiba-tiba langit menghitam, suara ombak menggelegar menghantam lambung kapal*",
    f"{nama}: \"A-apa ini?! Badai?! Pegangannya licin..!\"",
    f"*kapal berguncang keras, pandanganmu goyah sebelum semuanya tenggelam dalam gelap*",
    f"{nama}: \"Haaakh… khh… aku… di mana ini?\"",
    f"*kamu tersadar di atas pasir basah, hanya ditemani suara ombak dan angin dingin*",
    f"{nama}: \"Pulau…? Tidak ada siapa-siapa… apa aku benar-benar selamat sendirian?\""
    ]
    for pos, kal in enumerate(rkit):

        clr() 
        print(f"{layout.font.kuneng}", end="")  
        tik(kal) 
        
        print(f"{layout.font.reset}", end="")

        time.sleep(1.2)