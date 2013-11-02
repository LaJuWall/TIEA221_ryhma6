class KysymysLista():
    def __init__(self):
        filu = open("k_elaimet.txt")
        taulukko = [row.strip().split('|') for row in filu]
        #taulukko = kysymykset.readlines()
        filu.close()
        taulukko.pop(0)
        self.kysymykset = []
        for datalist in taulukko:
            kysymys = Kysymys(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5])
            self.kysymykset.append(kysymys)

class VastausLista():
    def __init__(self):
        vastaukset = open("v_elaimet.txt")
        taulukko = [row.strip().split('|') for row in vastaukset]
        #taulukko = kysymykset.readlines()
        vastaukset.close()
        taulukko.pop(0)
        self.vastaukset = []
        for datalist in taulukko:
            vastaus = Vastaus(datalist[0], datalist[1], datalist[2])
            self.vastaukset.append(vastaus)

class SelitystenLista():
    def __init__(self):
        selitykset = open("s_elaimet.txt")
        taulukko = [row.strip().split('|') for row in selitykset]
        #taulukko = kysymykset.readlines()
        selitykset.close()
        taulukko.pop(0)
        self.selitykset = []
        for datalist in taulukko:
            selitys = Selitys(datalist[0], datalist[1])
            self.selitykset.append(selitys)

class Kysymys():
    def __init__(self, k_id=None, k_txt=None, k_vid1=None, k_vid2=None, k_vid3=None, k_sid=None):
        self.k_id = k_id
        self.k_txt = k_txt
        self.k_vid1 = k_vid1
        self.k_vid2 = k_vid2
        self.k_vid3 = k_vid3
        self.k_sid = k_sid

class Vastaus():
    def __init__(self, v_id=None, v_txt=None, v_skid=None):
        self.v_id = v_id
        self.v_txt = v_txt
        self.v_skid = v_skid

class Selitys():
    def __init__(self, s_id=None, s_txt=None):
        self.s_id = s_id
        self.s_txt = s_txt

def printtaa_k(lista):
    print lista
    for kyssari in lista:
        print "******"
        print "Kysymyksen ID on: " + kyssari.k_id
        print "Kysymyksen teksti on: " + kyssari.k_txt
        print "Kysymyksen vastaus_ID:t on: " + kyssari.k_vid1 + ", " + kyssari.k_vid2 + ", " +  kyssari.k_vid3 + ", " +  kyssari.k_vid4

def printtaa_v(lista):
    print lista
    for vastaus in lista:
        print "******"
        print "Vastauksen ID on: " + vastaus.v_id
        print "Vastauksen teksti on: " + vastaus.v_txt
        print "Vastauksen s_id on: " + vastaus.v_skid

def printtaa_s(lista):
    print lista
    for seli in lista:
        print "*******"
        print "Selityksen ID on: " + seli.s_id
        print "Selityksen teksti on: " + seli.s_txt 

def anna_kysymys(lista, h_id):
    for kysymys in lista:
        if kysymys.k_id == h_id:
            return kysymys

def anna_vastaukset(kys, vas_lis):
    palaute = []
    v_idt = [kys.k_vid1, kys.k_vid2, kys.k_vid3]
    for v_id in v_idt:
        for vas in vas_lis:
            if vas.v_id == v_id:
                palaute.append(vas)
    return palaute

def tarkista_vastaus(vastaus, vastaukset):
    if vastaus == "A":
        return vastaukset[0].v_skid
    if vastaus == "B":
        return vastaukset[1].v_skid
    if vastaus == "C":
        return vastaukset[2].v_skid

def hae_selitys(kyssari, selitykset):
    h_id = kyssari.k_sid
    for seli in selitykset:
        if seli.s_id == h_id:
            return seli.s_txt
    return "EI LOYTYNY"

def main():

    print "Tahdotko tuostaa filuja (T) vai testata pelia (P)?"
    mitatehda = raw_input("Vastaa tahan: ")
    vastaukset = VastausLista()
    kysymykset = KysymysLista()
    selitykset = SelitystenLista()
    if mitatehda == "T":
        print "********************"
        printtaa_k(kysymykset.kysymykset)
        printtaa_v(vastaukset.vastaukset)
        printtaa_s(selitykset.selitykset)
    if mitatehda == "P":
        jatketaanko = True
        seur_id = "01"
        while jatketaanko:
            kysymys_nyt = anna_kysymys(kysymykset.kysymykset, seur_id)
            vastaukset_nyt = anna_vastaukset(kysymys_nyt, vastaukset.vastaukset)
            print kysymys_nyt.k_txt
            print "A: " + vastaukset_nyt[0].v_txt
            print "B: " + vastaukset_nyt[1].v_txt
            print "C: " + vastaukset_nyt[2].v_txt
            p_vastaus = raw_input("Vastauksesi on?")
            mitaSitten = tarkista_vastaus(p_vastaus, vastaukset_nyt)
            if mitaSitten == "00":
                print "Vaarin meni!"
                selitys = hae_selitys(kysymys_nyt, selitykset.selitykset)
                print "Selitys: " + selitys
                jatketaanko = False
                break
            if mitaSitten == "01":
                print "Lapaisit pelin!"
                jatketaanko == False
                break
            seur_id = mitaSitten
        

if __name__ == "__main__":
    main()