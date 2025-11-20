import time

def clear():
	print("\033[2J\033[H", end="")

def anCrafting():
	an = [
	"╔╦╗╔═╗╔══╗─╔╗╔══╗╔═╦╗╔══╗╔═╦╗",
	"║╔╝║╬║║╔╗║─║║╚║║╝║║║║║╔╗║║║║║",
	"║╚╗║╗╣║╠╣║╔╣║╔║║╗║║║║║╠╣║║║║║",
	"╚╩╝╚╩╝╚╝╚╝╚═╝╚══╝╚╩═╝╚╝╚╝╚╩═╝",
	"─────────────────────────────",]
	
	frame = 0
	while frame < 4:
		print(an[frame])
		frame = frame + 1
		time.sleep(0.5)
		
def anCraftingnol():
	an = [
	"╔╦╗╔═╗╔══╗─╔╗╔══╗╔═╦╗╔══╗╔═╦╗",
	"║╔╝║╬║║╔╗║─║║╚║║╝║║║║║╔╗║║║║║",
	"║╚╗║╗╣║╠╣║╔╣║╔║║╗║║║║║╠╣║║║║║",
	"╚╩╝╚╩╝╚╝╚╝╚═╝╚══╝╚╩═╝╚╝╚╝╚╩═╝",
	"─────────────────────────────",]
	
	frame = 0
	while frame < 4:
		print(an[frame])
		frame = frame + 1
		
def membuat():
	an = ["Membuat.","Membuat..","Membuat...","Membuat.",]
	
	frame = 0
	while frame < 4:
		print(an[frame])
		frame = frame + 1
		time.sleep(1)
		clear()