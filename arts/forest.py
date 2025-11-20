import time

def clear():
	print("\033[2J\033[H", end="")

def forest():
	frame = [
	"     ___",
	"   _(   )_       ___",
	"  (_     _)    _(  _)_ ",
	" (_ .      )  (_      )",
	") (__' ‚__) )  (__.|__)",
	"_    | |(_ ._)    ||     ",
	" )_  ] |  ||      ||       ",
	" ._) | | _||_,/‚ _]|_._,),_",
	"_ __ | |_ _",
	"__ _ __- _ __ _ _ __ _-_ _  _",]
	
	b = 0
	while b<10:
		print(frame[b])
		b = b+1
		
def toPlane():
	plane = ["             ,-.",
	"   _,.      /  /",
	"  ; \____,-==-._  )",
	"  //_    `----' {+>",
	"  `  `'--/  /-'`(",
	"        /  /",
	"        `='",]
	
	clear()
	forest()
	print("Akhhh!!")
	time.sleep(2)
	print("Kenapa ini?!")
	time.sleep(2)
	print("Kepalaku pusing banget!!")
	time.sleep(2)
	clear()
	print("Haaaaaa???")
	time.sleep(2)
	clear()
	print("Kenapa hutan tiba tiba menghilang?!!")
	time.sleep(3)
	clear()
		
	frame = 0
	while frame < 7:
		print(plane[frame])
		frame = frame + 1
	time.sleep(1)
	print("Apa itu?")
	time.sleep(2)
	print("Itu? itu pesawat")
	time.sleep(2)
	print("Heyy!! Hey pesawat!!")
	time.sleep(2)
	print("Tolong aku, pesawat!!")
	time.sleep(2)
	print("Heyyy!!")
	time.sleep(2)
	
	clear()