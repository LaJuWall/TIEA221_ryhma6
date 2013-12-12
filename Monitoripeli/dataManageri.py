# -*- coding:utf-8 -*-
import random
import sys

class KysymysLista():
	""" Luokka, jonka tehtavana on pitaa ylla listaa kaikista kaytossa olevista kysymyksista. """
	
	def __init__(self, sken_nimi):
		skenNimi = str(sken_nimi)
		skenNimi.replace("[", "")
		skenNimi.replace("]", "")
		skenNimi.replace("'", "")
		nimi = skenNimi + "_kys.txt"
		filu = open(nimi)
		taulukko = [row.strip().replace(" ", "").replace("_", " ").split('|') for row in filu]
		filu.close()
		taulukko.pop(0)
		self.kysymykset = []
		for datalist in taulukko:
			kysymys = Kysymys(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6], datalist[7], datalist[8], datalist[9], datalist[10], datalist[11], datalist[12], datalist[13])
			self.kysymykset.append(kysymys)

	def annaKysymys(self, lista, h_id):
		print h_id
		print lista
		for kysymys in lista.kysymykset:
		  if kysymys.k_id == h_id:
			return kysymys

class Kysymys():
	""" Kysymysluokka. Tarkoitus kasitella yksittaisen kysymyksen tietoja.
		Muodostajaa asettaa tiedot annettujen patametrien pohjalta.
		
		Lyhenteiden selitykset:
		k_id = Taman kysymyksen ID
		k_txt = Taman kysymyksen teksti
		k_vid 1-4 = Tahan kysymykseen sidottujen vastausten ID:t
		k_sid = Tahan kysymyksen sidotun selityksen ID
		k_arPul = Taman kysymyksen aikana oleva Pulssi
		k_arHaps = Taman kysymyksen aikana oleva Happisaturaatio
		k_arVep = Taman kysymyksen aikana oleva verenpaine
		k_arCo2 = Taman kysymyksen aikana oleva Co2 arvo
		k_arBis = Taman kysymyksen aikana oleva Bis arvo
		k_arMac = Taman kysymyksen aikana oleva Mac arvo
		k_arLamp = Taman kysymyksen aikana oleva lampotila """

	def __init__(self, k_id=None, k_txt=None, k_vid1=None, k_vid2=None, k_vid3=None, k_vid4=None, k_sid=None, k_arPul=None, k_arHaps=None, k_arVep=None, k_arCo2=None, k_arBis=None, k_arMac=None, k_arLamp=None):
		self.k_id = k_id
		self.k_txt = k_txt
		self.k_vid1 = k_vid1
		self.k_vid2 = k_vid2
		self.k_vid3 = k_vid3
		self.k_vid4 = k_vid4
		self.k_sid = k_sid
		self.k_arPul = k_arPul
		self.k_arHaps = k_arHaps
		self.k_arVep = k_arVep
		self.k_arCo2 = k_arCo2
		self.k_arBis = k_arBis
		self.k_arMac = k_arMac
		self.k_arLamp = k_arLamp

class VastausLista():
	""" Luokka, jonka tehtavana on yllapitaa listaa kaikista kaytossa olevista vastauksista. """
	def __init__(self, sken_nimi):
		nimi = sken_nimi + "_vas.txt"
		vastaukset = open(nimi)
		taulukko = [row.strip().replace(" ", "").replace("_", " ").split('|') for row in vastaukset]
		#taulukko = kysymykset.readlines()
		vastaukset.close()
		taulukko.pop(0)
		self.vastaukset = []
		for datalist in taulukko:
			vastaus = Vastaus(datalist[0], datalist[1], datalist[2])
			self.vastaukset.append(vastaus)

	def annaVastaukset(self, kys):
		palaute = []
		v_idt = [kys.k_vid1, kys.k_vid2, kys.k_vid3, kys.k_vid4]
		for v_id in v_idt:
			for vas in self.vastaukset:
				if vas.v_id == v_id:
					palaute.append(vas)
		return palaute

class Vastaus():
	""" Vastausluokka. Tarkoitus kasitella yksittaisen vastauksen tietoja.
		Muodstaja asettaa tiedot annettujen parametrien pohjalta. 

		Lyhenteiden selitykset:
		v_id = Taman vastauksen ID
		v_txt = Taman vastauksen teksti
		v_skid = Mita seuraa tasta vastauksesta
				 00 => Vastaus on vaara
				 01 => Vastaus on skenaarion viimeinen
				 muu => Seuraava kysymys, jonka ID on 'muu' """
	
	def __init__(self, v_id=None, v_txt=None, v_skid=None):
		self.v_id = v_id
		self.v_txt = v_txt
		self.v_skid = v_skid

class SelitystenLista():
	""" Luokka, jonka tehtavana on yllapitaa listaa kaikista kaytossa olevista selityksista. """
	
	def __init__(self, sken_nimi):
		nimi = sken_nimi + "_sel.txt"
		selitykset = open(nimi)
		taulukko = [row.strip().replace(" ", "").replace("_", " ").split('|') for row in selitykset]
		selitykset.close()
		taulukko.pop(0)
		self.selitykset = []
		for datalist in taulukko:
			selitys = Selitys(datalist[0], datalist[1])
			self.selitykset.append(selitys)

	def annaSelitys(self, lista, h_id):
		for selitys in lista:
		  if selitys.s_id == h_id:
			return selitys

class Selitys():
	""" Selitysluokka. Tarkoitus kasitella yksittaisen vastauksen tietoja.
		Muodstaja asettaa tiedot annettujen parametrien pohjalta. """
	
	def __init__(self, s_id=None, s_txt=None):
		self.s_id = s_id
		self.s_txt = s_txt

class Pohjustukset():
	def __init__(self):
		nimi = "pohjustukset.txt"
		vastaukset = open(nimi)
		taulukko = [row.strip().replace(" ", "").replace("_", " ").split('|') for row in vastaukset]
		vastaukset.close()
		taulukko.pop(0)
		self.pohjustukset = []
		for datalist in taulukko:
			pohjustus = Pohjustus(datalist[0], datalist[1])
			self.pohjustukset.append(pohjustus)

	def annaPohjustus(self, sken_id):
		palaute = None
		h_id = sken_id 
		for pohj in self.pohjustukset:
			if pohj.kys_id == h_id:
				palaute = pohj
		return palaute

class Pohjustus():
	def __init__(self, kys_id=None, p_txt=None):
		self.kys_id = kys_id
		self.p_txt = p_txt

class SkenaarioLista():
	"""Luokka, jonka tehtavana on yllapitaa listaa kaytettavissa olevista skenaaarioista.
	   Aina kun uusi skenaario palautetaan, se poistetaan listasta, jottei samaa skenaariota 
	   kayteta kahdesti. """
	
	def __init__(self):
		filu = open("skenaariot.txt")
		self.skenaariot = [row.strip().split('|') for row in filu]
		self.skenaariot.pop(0)
		random.shuffle(self.skenaariot)
	
	def annaSkenaario(self):
		if len(self.skenaariot) == 0:
			print "Skenaariot loppu..."
			sys.exit(0)
		palaute = self.skenaariot[0]
		self.skenaariot.pop(0)
		return str(palaute)[2:][:-2]

class DataManager():
	def __init__(self):
		print "*** Aloitettiin datamangerin alustus ***"
		self.skenaariot = SkenaarioLista()
		print "Skenaariot alustettu!"
		self.skenaario_nyt = self.skenaariot.annaSkenaario()
		print "Ensimmäinen skenaario otettu"
		self.kysymykset = KysymysLista(self.skenaario_nyt)
		print "Kysymykset ladattu!"
		self.vastaukset = VastausLista(self.skenaario_nyt)
		print "Vastaukset ladattu!"
		self.selitykset = SelitystenLista(self.skenaario_nyt)
		print "Selitykset ladattu!"
		self.kysymys_nyt = self.kysymykset.annaKysymys(self.kysymykset, "01")
		print "Kysymys otettu käsittelyyn!"
		self.vastaukset_nyt = self.vastaukset.annaVastaukset(self.kysymys_nyt)
		print "Kysymyksen vastaukset haettu!"
		self.selitys_nyt = self.selitykset.annaSelitys(self.selitykset.selitykset ,self.kysymys_nyt.k_sid)
		print "Selitys otettu talteen!"
		self.pohjustukset = Pohjustukset()
		self.pohjustus_nyt = self.pohjustukset.annaPohjustus(self.skenaario_nyt)
		print "HUOMIOHUOMIOHUOMIOHUOMIO"
		print self.pohjustus_nyt
		print "Ses"

	def printtaaKysymys(otus):
		onkoPohj = None
		if onkoPohj:
			print "POHJUSTUS:"
			print "Blaa blaa blaa"
		print "*******************"
		print "KYSYMYS:"
		print otus.kysymys_nyt.k_txt
		print " "
		print "MONITORIN ARVOT:"
		print "Pulssi: " + otus.kysymys_nyt.k_arPul
		print "Happisaturaatio: " + otus.kysymys_nyt.k_arHaps
		print "Verenpaine: " + otus.kysymys_nyt.k_arVep
		print "Co2: " + otus.kysymys_nyt.k_arCo2
		print "BIS: " + otus.kysymys_nyt.k_arBis
		print "MAC: " + otus.kysymys_nyt.k_arMac
		print "Lampotila: " + otus.kysymys_nyt.k_arLamp
		print " "
		print "VASTAUKSET:"
		#for vastaus in otus.vastaukset_nyt:
		#	print vastaus.v_txt
		print "A: " + otus.vastaukset_nyt[0].v_txt
		print "B: " + otus.vastaukset_nyt[1].v_txt
		print "C: " + otus.vastaukset_nyt[2].v_txt
		print "D: " + otus.vastaukset_nyt[3].v_txt

	def mitasSitten(self, annettu_id):
		if annettu_id == "00":
			print "Vastasit väärin... Selitys:"
			print self.selitys_nyt.s_txt
			return False
		if annettu_id == "01":
			print "Vastasit kaikkiin kysymyksiin oikein! Tahdotko jatkaa toisella kysymyssarjalla?"
			sitten = raw_input('K = Kylla | E = Ei >>>> ')
			if sitten == "E":
				return False
			if sitten == "K":
				self.asetaSeuraavaSkenaario()
				return True
		else:
			self.asetaSeuraavaKysymys(annettu_id)
			return True

	def asetaSeuraavaKysymys(self, annettu_id):
		self.kysymys_nyt = self.kysymykset.annaKysymys(self.kysymykset, annettu_id)
		self.vastaukset_nyt = self.vastaukset.annaVastaukset(self.kysymys_nyt)

	def asetaSeuraavaSkenaario(self):
		self.skenaario_nyt = self.skenaariot.annaSkenaario()
		self.kysymykset = KysymysLista(self.skenaario_nyt)
		self.vastaukset = VastausLista(self.skenaario_nyt)
		self.selitykset = SelitystenLista(self.skenaario_nyt)
		self.kysymys_nyt = self.kysymykset.annaKysymys(self.kysymykset, "01")
		self.vastaukset_nyt = self.vastaukset.annaVastaukset(self.kysymys_nyt)
		self.selitys_nyt = self.selitykset.annaSelitys(self.selitykset.selitykset ,self.kysymys_nyt.k_sid)

	def aloitaAlusta(self):
		self.skenaariot = SkenaarioLista()
		self.skenaario_nyt = self.skenaariot.annaSkenaario()
		self.kysymykset = KysymysLista(self.skenaario_nyt)
		self.vastaukset = VastausLista(self.skenaario_nyt)
		self.selitykset = SelitystenLista(self.skenaario_nyt)
		self.kysymys_nyt = self.kysymykset.annaKysymys(self.kysymykset, "01")
		self.vastaukset_nyt = self.vastaukset.annaVastaukset(self.kysymys_nyt)
		self.selitys_nyt = self.selitykset.annaSelitys(self.selitykset.selitykset ,self.kysymys_nyt.k_sid)


def main():
	manageri = DataManager()
	jatketaanko = True
	
	while jatketaanko:
		manageri.printtaaKysymys()
		vastaus = raw_input('Vastauksesi >>> ')
		if vastaus == "A":
			jatketaanko = manageri.mitasSitten(manageri.vastaukset_nyt[0].v_skid)
		if vastaus == "B":
			jatketaanko = manageri.mitasSitten(manageri.vastaukset_nyt[1].v_skid)
		if vastaus == "C":
			jatketaanko = manageri.mitasSitten(manageri.vastaukset_nyt[2].v_skid)
		if vastaus == "D":
			jatketaanko = manageri.mitasSitten(manageri.vastaukset_nyt[3].v_skid)


if __name__ == "__main__":
	main()