class Muusika:
	def __init__(self, nimi):
		self.nimi = nimi
		#self.emotsioonid = 
		

def main():
	fail = open("Lugude omadused.txt", encoding="utf-8")
	tekstigrupid = []
	grupp = []
	for i in fail:
		if i == "\n":
			tekstigrupid.append(grupp)
			grupp = []
		else:
			grupp.append(i.strip())
	for i in tekstigrupid:
		print(i)
	

	kõikMeeleolud = set()
	for grupp in tekstigrupid:
		for sõna in grupp[1:]:
			kõikMeeleolud.add(sõna)
			
	print(kõikMeeleolud)
main()