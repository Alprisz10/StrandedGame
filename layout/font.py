
abang = "\033[31m"
ijo = "\033[32m"
kuneng = "\033[33m"
reset = "\033[0m"
kandel = "\033[1m"
cyan = "\033[0;36m"

def errorInput():
	print(kandel,abang,"[!] Anda memasukkan pilihan yang tidak sesuai [!]", reset)

def clear():
	print("\033[2J\033[H", end="")