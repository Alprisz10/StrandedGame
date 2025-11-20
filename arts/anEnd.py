import time
import layout

text = [" _____           _                              ",
"| ____|_ __   __| |   __ _  __ _ _ __ ___   ___ ",
"|  _| | '_ \ / _` |  / _` |/ _` | '_ ` _ \ / _ \ ",
"| |___| | | | (_| | | (_| | (_| | | | | | |  __/",
"|_____|_| |_|\__,_|  \__, |\__,_|_| |_| |_|\___|",
"                     |___/                      "]
thanks = "Selamat dan terimakasih telah memainkan game ini sampai selesai!"

def anEnd():
		for hasText in text:
			print(layout.font.ijo,hasText)
			time.sleep(1)
		print(layout.font.cyan, thanks)