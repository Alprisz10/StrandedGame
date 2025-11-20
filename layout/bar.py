import time
import layout
import feature
from data import dk

def bar():
    dk.cur.execute("SELECT * FROM user")
    hasCek = dk.cur.fetchall()
    
    warna = (layout.font.ijo, layout.font.kuneng, layout.font.cyan)
    nama = ("Kesehatan","Energi   ","Hidrasi  ")
    
    varWadh = 2
    while varWadh <= 4:
        bagData  = int(hasCek[0][varWadh] / 5)
        wadhLog = "▆"*bagData
        print(f"{warna[varWadh - 2]}{nama[varWadh - 2]} {wadhLog:<20} ({hasCek[0][varWadh]}%) {layout.font.reset}")
        varWadh = varWadh + 1