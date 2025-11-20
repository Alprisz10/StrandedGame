import time
import arts

def stayFish():
	an = ["           ‘\ ",
	"          ‘  \    O",
	"        ‘     \@  |",
	"      ‘        `\/|",
	"    ‘            /|     *   *",
	"  ‘              \|   (/  )/",
	"‘~-~-~-~-~-~“““““““““*““““““*“““",
	"~-~-~-~““ejm97“““““)/“““““(/““"]
	
	for has in an:
		print(has)
		
def strikeFish():
	an = ["    .    |",
	"   .    _|",
	"       /o \ ",
	"      |\__/|",
	"     /|'-'\)",
	"    |/|    |",
	"    |/;    \)",
	"       \__/",
	"       //\\",
	"      /_/\_\ "]
	
	for has in an:
		print(has)
		
def waitFishing():
		setStart = time.time()
		an = ["menunggu umpan dimakan.","menunggu umpan dimakan..","menunggu umpan dimakan...","menunggu umpan dimakan...."]
		
		while time.time() - setStart < 11:
			for has in an:
				print(has)
				time.sleep(1)
				arts.font.clear()
		