# thirsty.py
import threading
import time
from data import dk

def startKehausan():
    def mng_kehausan():
        cur = dk.db.cursor()

        while True:
            time.sleep(30)
            
            cur.execute("SELECT kehausan, kesehatan FROM user")
            rows = cur.fetchall()

            if not rows:
                continue

            for row in rows:
                kehausanS = row[0]
                kesehatanS = row[1]
                
                kehausan_baru = max(0, kehausanS - 1)
                kesehatan_baru = kesehatanS
                
                if kehausan_baru == 0 and kehausanS == 0:
                    kesehatan_baru = max(0, kesehatanS - 1)
                
                cur.execute(
                    "UPDATE user SET kehausan = ?, kesehatan = ?",
                    (kehausan_baru, kesehatan_baru)
                )

            dk.db.commit()

    threading.Thread(target=mng_kehausan, daemon=True).start()