def anBoat():
	def clear():
		print("\033[2J\033[H", end="")
	import time
	
	a = 0
	while a <= 3:
		boat = ["                v    ~.    v  ","          v           /|","                     / |        v  ","            v       /__|__","                  \--------/","~~~~~~~^~~~^~~~~~~~`~~~~~~'~~~~~~~~~~~~~~~"]
		clear()
		
		batasFrame = len(boat)
		frame = 0
		
		while frame < batasFrame:
			print(boat[frame])
			frame = frame + 1
		
		time.sleep(0.25)
		clear()
		
		boat2 = ["                    -.v         v","             v        /|","                     / |             v","                v   /__|__","                  \--------/","~~~~~~~~~~~~~~~~~~^‘~~~^~~’~~~~~~~~~~~~~~~"]
		
		batasFrame = len(boat2)
		frame = 0
		while frame < batasFrame:
			print(boat2[frame])
			frame = frame + 1
			
		time.sleep(0.25)
		clear()
		
		boat3 = ["                    ~.      v      v","                  v   /|","                     / |                v","                   /_v|__","                  \--------/","~~~~~~~~~~~~~~~~~~~'~~~~~~‘~~~~~~~~^~~~^~~"]
		batasFrame = len(boat3)
		frame = 0
		while frame < batasFrame:
			print(boat3[frame])
			frame = frame + 1
			
		time.sleep(0.25)
		clear()
		
		boat4 = ["                     -.               v",
		"                      /|    v ",
		" v                   / |                ",
		"                    /_|__       v",
		"                  \--------/","~^~~~^~~~~~~~~~~~~~'~~~~~~‘~~~~~~~~~~~~~~~"]
		
		batasFrame = len(boat4)
		frame = 0
		while frame < batasFrame:
			print(boat4[frame])
			frame = frame + 1
			
		time.sleep(0.25)
		clear()
		
		boat5 = ["  v                  ~.            ",
		"                     /|        v ",
		"       v            / |                ",
		"                   /_|__           v",
		"                  \--------/",
		"~~~~~~~~~~~~~~~~~^~'~~^~~~‘~~~~~~~~~~~~~~~"]
		
		batasFrame = len(boat5)
		frame = 0
		while frame < batasFrame:
			print(boat5[frame])
			frame = frame + 1
			
		time.sleep(0.25)
		clear()
		
		boat6 = ["  v    v             -.            ",
		"                     /|        v ",
		"           v        / |                ",
		"  v                /_|__           ",
		"                  \--------/",
		"~~~~~~~~~~~~~~~~~~~'~~~~~~‘~~~~~~~^~~^~~~~"]
		
		batasFrame = len(boat6)
		frame = 0
		while frame < batasFrame:
			print(boat6[frame])
			frame = frame + 1
			
		time.sleep(0.25)
		a = a + 1