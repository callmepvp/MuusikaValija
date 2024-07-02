import itertools as it

class Muusika:
	def __init__(self, nimi, emotsioonid):
		self.nimi = nimi
		self.emotsioonid = emotsioonid

	def getEmotsioonid(self):
		return self.emotsioonid
	
	def kasOmabEmotsiooniPaari(self, paar):
		return self.getEmotsioonid()[paar[0]] == 1 and self.getEmotsioonid()[paar[1]] == 1
		

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

	kõikMeeleolud = set()
	kõikLaulud = []
	for grupp in tekstigrupid:
		kõikLaulud.append(grupp[0])
		for sõna in grupp[1:]:
			kõikMeeleolud.add(sõna)
	
	print(kõikMeeleolud)

	lood = []
	for laul in tekstigrupid:
		emotsioonid = {j : 1 if j in laul else 0 for j in kõikMeeleolud}
		lugu = Muusika(laul[0], emotsioonid)
		lood.append(lugu)

	meeleoluPaarid = list(it.combinations(kõikMeeleolud, 2))
	paaridDict = {i : 0 for i in meeleoluPaarid}
	for i in meeleoluPaarid:
		for j in lood:
			if j.kasOmabEmotsiooniPaari(i):
				paaridDict[i] += 1

	suurimVäärtus = max(paaridDict.values())
	for j in paaridDict:
		paaridDict[j] = paaridDict[j] / suurimVäärtus
	
	print(paaridDict)
main()