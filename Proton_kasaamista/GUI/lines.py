from kivy.app import App
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.clock import Clock
from math import cos, sin
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
import random
import sys
import os

""" Maaritetaan ikkunan korkeus ja leveys. """
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')

""" Maaritetaan naytoon piirtyvat elementit ja niiden ominaisuudet. """
Builder.load_string('''
<LinePlayground>:
    canvas:
        Rectangle:
            pos: root.width * 3 / 4, 320
            size: 2, 480

        Rectangle:
            pos: 0, 320
            size: root.width, 2

        Rectangle:
            pos: 0, 400
            size: root.width, 2

        Color:
            rgba: 1, .1, .1, .9
        Line:
            width: 2.
            points: root.points

        Color:
            rgba: .1, .1, 1, .9
        Line:
            width: 2.
            points: root.points2

        Color:
            rgba: .1, 1, .1, .9
        Line:
            width: 2.
            points: root.points3

        Color
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: root.palikan_paikka
            size: root.palikan_koko

    Label:
        pos: 187.5, 80
        font_size: 70 
        color: 1, .1, .1, .9 
        text: '10'

    Label:
        pos: 187.5, 200
        font_size: 70
        color: .1, .1, 1, .9  
        text: '10'

    Label:
        pos: 187.5, 320
        font_size: 70
        color: .1, 1, .1, .9  
        text: '10'

    Label:
        pos: -187.5, -40
        font_size: 70
        text: '10'

    Label:
        pos: -65.5, -40
        font_size: 70
        text: '10'

    Label:
        pos: 65.5, -40
        font_size: 70
        text: '10'

    Label:
        pos: 187.5, -40
        font_size: 70
        text: '10'

    Label:
        pos: 0, -120
        font_size: 18
        size_hint: .3, .2
        text: root.label_txt

    Label:
        pos: -500, -500
        font_size: 1
        text: root.aloita_naytto(self)

    GridLayout:
        cols: 2
        size_hint: 1, None
        height: 240

        GridLayout:
            cols: 2

            Button:
                text: root.a_btn_txt
                on_press: root.a_press(self)

            Button:
                text: root.b_btn_txt
                on_press: root.b_press(self)

            Button:
                text: root.c_btn_txt
                on_press: root.c_press(self)

            Button:
                text: root.d_btn_txt
                on_press: root.d_press(self)

<CustomPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Popup'
    
    GridLayout:
        cols: 1

        Label:
            text: 'Vastasit vaarin. Peli on paattynyt'

        Button:
            text: 'Aloita alusta'
            on_press: root.alotaAlusta()

        Button:
            text: 'Sulje peli'
            on_press: root.lopetaPeli()

''')

class UusiksMeni(Exception):
    def __init__(self):
        pass

class CustomPopup(Popup):

    def lopetaPeli(self):
        sys.exit()

    def alotaAlusta(self):
        raise UusiksMeni()

class SkenaarioLista():
    """Luokka, jonka tehtavana on yllapitaa listaa kaytettavissa olevista skenaaarioista.
       Aina kun uusi skenaario palautetaan, se poistetaan listasta, jottei samaa skenaariota 
       kayteta kahdesti. """
    def __init__(self):
        filu = open("skenaariot.txt")
        self.skenaariot = [row.strip().split('|') for row in filu]
        self.skenaariot.pop(0)
        print self.skenaariot
        random.shuffle(self.skenaariot)
    def annaSkenaario(self):
        if len(self.skenaariot) == 0:
            return "loppu"
        print "^^^^^^^^^^^^^^"
        print self.skenaariot
        print "^^^^^^^^^^^^^^"
        palaute = self.skenaariot[0]
        self.skenaariot.pop(0)
        return str(palaute)[2:][:4]

class KysymysLista():
    """ Luokka, jonka tehtavana on pitaa ylla listaa kaikista kaytossa olevista kysymyksista.
        Muodostajassa kysymykset luetaan suoraan 'kysymys.txt' tiedostosta
        TODO: Muodostajan pitaisi lukea tiedosto, jonka nimi annetaan esim parametrina. """
    def __init__(self, sken_nimi):
        skenNimi = str(sken_nimi)
        skenNimi.replace("[", "")
        skenNimi.replace("]", "")
        skenNimi.replace("'", "")
        nimi = skenNimi + "_kys.txt"
        filu = open(nimi)
        taulukko = [row.strip().split('|') for row in filu]
        filu.close()
        taulukko.pop(0)
        self.kysymykset = []
        for datalist in taulukko:
            kysymys = Kysymys(datalist[0], datalist[1], datalist[2], datalist[3], datalist[4], datalist[5], datalist[6])
            self.kysymykset.append(kysymys)

class VastausLista():
    """ Luokka, jonka tehtavana on yllapitaa listaa kaikista kaytossa olevista vastauksista.
        Muodostajassa vastaukset luetaan suoraan 'vastaus.txt' tiedostosta
        TODO: Muodostajan pitaisi lukea tiedosto, jonka nimi annetaan esim parametrina. """
    def __init__(self, sken_nimi):
        nimi = sken_nimi + "_vas.txt"
        vastaukset = open(nimi)
        taulukko = [row.strip().split('|') for row in vastaukset]
        #taulukko = kysymykset.readlines()
        vastaukset.close()
        taulukko.pop(0)
        self.vastaukset = []
        for datalist in taulukko:
            vastaus = Vastaus(datalist[0], datalist[1], datalist[2])
            self.vastaukset.append(vastaus)

class SelitystenLista():
    """ Luokka, jonka tehtavana on yllapitaa listaa kaikista kaytossa olevista selityksista.
        Muodostajassa vastaukset luetaan suoraan 'selitys.txt' tiedostosta
        TODO: Muodostajan pitaisi lukea tiedosto, jonka nimi annetaan esim parametrina. """
    def __init__(self, sken_nimi):
        nimi = sken_nimi + "_sel.txt"
        selitykset = open(nimi)
        taulukko = [row.strip().split('|') for row in selitykset]
        #taulukko = kysymykset.readlines()
        selitykset.close()
        taulukko.pop(0)
        self.selitykset = []
        for datalist in taulukko:
            selitys = Selitys(datalist[0], datalist[1])
            self.selitykset.append(selitys)

class Kysymys():
    """ Kysymysluokka. Tarkoitus kasitella yksittaisen kysymyksen tietoja.
        Muodostajaa asettaa tiedot annettujen patametrien pohjalta."""
    def __init__(self, k_id=None, k_txt=None, k_vid1=None, k_vid2=None, k_vid3=None, k_vid4=None, k_sid=None):
        self.k_id = k_id
        self.k_txt = k_txt
        self.k_vid1 = k_vid1
        self.k_vid2 = k_vid2
        self.k_vid3 = k_vid3
        self.k_vid4 = k_vid4
        self.k_sid = k_sid

class Vastaus():
    """ Vastausluokka. Tarkoitus kasitella yksittaisen vastauksen tietoja.
        Muodstaja asettaa tiedot annettujen parametrien pohjalta. """
    def __init__(self, v_id=None, v_txt=None, v_skid=None):
        self.v_id = v_id
        self.v_txt = v_txt
        self.v_skid = v_skid

class Selitys():
    """ Selitysluokka. Tarkoitus kasitella yksittaisen vastauksen tietoja.
        Muodstaja asettaa tiedot annettujen parametrien pohjalta.
    """
    def __init__(self, s_id=None, s_txt=None):
        self.s_id = s_id
        self.s_txt = s_txt


class LinePlayground(FloatLayout):
    """ Luokka, jossa itse peli on kirjoitettu metodeineen. """
    
    # Alustetaan tarpeelliset listat ja muuttujat
    skenaariot = SkenaarioLista()
    skenaario_nyt = skenaariot.annaSkenaario()
    print "!!!!!!!!!!!!!"
    print skenaario_nyt
    print "!!!!!!!!!!!!!"
    jatketaanko = True
    kysymykset = KysymysLista(skenaario_nyt)
    vastaukset = VastausLista(skenaario_nyt)
    points = ListProperty([0, 480, 374, 480])
    points2 = ListProperty([0, 600, 374, 600])
    points3 = ListProperty([0, 720, 374, 720])
    dt = NumericProperty(0)
    palikan_paikka = ListProperty([0, 405])
    palikan_koko = ListProperty([375, 395])
    
    def alustaPeli(self):
        #printtailu tehty vain kehityksen helpottamiseksi.
        #printtaa_k(kysymykset.kysymykset)
        #printtaa_v(vastaukset.vastaukset)
        #Otetaan kasiteltava kysymys ylos.
        self.kysymys_nyt = self.anna_kysymys(self.kysymykset.kysymykset, "01")
        #print kysymys_nyt.k_txt
        #Otetaan kasiteltavan kysymyksen vastaukset muistiin.
        self.vastaukset_nyt = self.anna_vastaukset(self.kysymys_nyt, self.vastaukset.vastaukset)
        #print vastaukset_nyt

        #Asetetaan nappuloiden ja kysymys_labelin teksti.
        self.a_btn_txt = StringProperty(self.vastaukset_nyt[0].v_txt)
        self.b_btn_txt = StringProperty(self.vastaukset_nyt[1].v_txt)
        self.c_btn_txt = StringProperty(self.vastaukset_nyt[2].v_txt)
        self.d_btn_txt = StringProperty(self.vastaukset_nyt[3].v_txt)
        self.label_txt = StringProperty(self.kysymys_nyt.k_txt)
        
        #Kaynnistetaan musiikki.
        sound = SoundLoader.load('testi.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE MUSA TOIMI!!!")

    def aloitaAlusta(self):
        print "SESESESESSESESESESESESESESESESESESESESESESESES"
    
    def lopetaPeli(self):
        sys.exit()
    
    def aloita_uus_skenaario(self, value):
        self.skenaario_nyt = self.skenaariot.annaSkenaario()
        self.kysymykset = KysymysLista(self.skenaario_nyt)
        self.vastaukset = VastausLista(self.skenaario_nyt)
        self.kysymys_nyt = self.anna_kysymys_2(self.kysymykset.kysymykset, "01")
        self.vastaukset_nyt = self.anna_vastaukset_2(self.kysymys_nyt, self.vastaukset.vastaukset)
    
    def a_press(instance, value):
        """ Kun pelaaja painaa A nappia, soitetaan painamisaani ja 
            siirrytaan tarkastamaan vastauksen oikeellisuutta. """
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        instance.tarkista_vastaus("A", instance.vastaukset_nyt)
   
    def b_press(instance, value):
        """ Kun pelaaja painaa B nappia, soitetaan painamisaani ja 
            siirrytaan tarkastamaan vastauksen oikeellisuutta. """
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        instance.tarkista_vastaus("B", instance.vastaukset_nyt)
   
    def c_press(instance, value):
        """ Kun pelaaja painaa C nappia, soitetaan painamisaani ja 
            siirrytaan tarkastamaan vastauksen oikeellisuutta. """
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        instance.tarkista_vastaus("C", instance.vastaukset_nyt)
        
    def d_press(instance, value):
        """ Kun pelaaja painaa D nappia, soitetaan painamisaani ja 
            siirrytaan tarkastamaan vastauksen oikeellisuutta. """
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        instance.tarkista_vastaus("D", instance.vastaukset_nyt)
        
    def anna_kysymys(lista, h_id):
        """ Palautetaan kysymyslistasta kysymysm jonka ID vastaa 
            haettua ID:ta (h_id) """
        for kysymys in lista:
          if kysymys.k_id == h_id:
            return kysymys
  
    def anna_vastaukset(kys, vas_lis):
        """ Palauttaa listana kaikki annettuun kysymykseen (kys) 
            liittyvat vastaukset. """
        palaute = []
        v_idt = [kys.k_vid1, kys.k_vid2, kys.k_vid3, kys.k_vid4]
        for v_id in v_idt:
            for vas in vas_lis:
                if vas.v_id == v_id:
                    palaute.append(vas)
        return palaute

    def anna_kysymys_2(self, lista, h_id):
        """ Purkka viritelma. Tekee saman kuin anna_kysymys, 
            mutta tama toimii ohjelman kaynnistyksen yhteydessa. """
        for kysymys in lista:
          if kysymys.k_id == h_id:
            return kysymys
   
    def anna_vastaukset_2(self, kys, vas_lis):
        """ Purkka viritelma. Tekee saman kuin anna_vastaukset, 
            mutta tama toimii ohjelman kaynnistyksen yhteydessa. """
        palaute = []
        v_idt = [kys.k_vid1, kys.k_vid2, kys.k_vid3, kys.k_vid4]
        for v_id in v_idt:
            for vas in vas_lis:
                if vas.v_id == v_id:
                    palaute.append(vas)
        return palaute
   
    def aseta_seuraava_kysymys(self, kys_id):
        """ Asettaa tamanhetkiseksi kysymykseksi kys_id:ta vastaavan kysymyksen. """
        self.kysymys_nyt = self.anna_kysymys_2(self.kysymykset.kysymykset, kys_id)
        self.vastaukset_nyt = self.anna_vastaukset_2(self.kysymys_nyt, self.vastaukset.vastaukset)
        self.a_btn_txt = self.vastaukset_nyt[0].v_txt
        self.b_btn_txt = self.vastaukset_nyt[1].v_txt
        self.c_btn_txt = self.vastaukset_nyt[2].v_txt
        self.d_btn_txt = self.vastaukset_nyt[3].v_txt
        self.label_txt = self.kysymys_nyt.k_txt
  
    def mitasSitten(self, annettu_id):
        """ Tarkistetaan mita tehdaan seuraavaksi. 
            Mikali annettu_id on 00, pelaaja on vastannut vaarin. 
            Mikali annettu_id on 01, pelaaja on saanut kysymyssarjan paatokseen. 
            Muussa tapauksessa asetetaan seuraavakis annettu_id:ta vastaava kysymys. """
        if annettu_id == "00":
            print "Vaara vastaus napattu!"
            #popup = Popup(title="Game over",
            #content=Label(text='Vaara vastaus! Aloita alusta.'),
            #size_hint=(None, None),
            #size=(400, 400),
            #auto_dismiss=False)
            #popup.open()
            p = CustomPopup()
            p.open()
        if annettu_id == "01":
            popup = Popup(title="Congratulations!",
            content=Label(text='Vastasit kaikkiin kysymyksiin oikein. Peli on ohi.'),
            size_hint=(None, None),
            size=(400, 400),
            auto_dismiss=False)
            popup.open()
        else:
            self.aseta_seuraava_kysymys(annettu_id)
   
    def tarkista_vastaus(self, vastaus, vastaukset):
        """ Lahetettaan mitasSitten metodille painalluksen mukainen vastaus. 
            TODO: Mitas sitten kun vastausten paikat ovat arvottu. """
        # Iffin jalkeen maritellaan muuttuja ja sit tehaan
        # Mitas sitten metdodin temput tassa? Ei tarvii teha
        # Yhta ylimaarasta metodia.
        if vastaus == "A":
            self.mitasSitten(vastaukset[0].v_skid)
        if vastaus == "B":
            self.mitasSitten(vastaukset[1].v_skid)
        if vastaus == "C":
            self.mitasSitten(vastaukset[2].v_skid)
        if vastaus == "D":
            self.mitasSitten(vastaukset[3].v_skid)
   
    def hae_selitys(self, kyssari, selitykset):
            """ Haetaan kysymykseen liitetty selitys. """
            h_id = kyssari.k_sid
            for seli in selitykset:
                if seli.s_id == h_id:
                    return seli.s_txt
            return "EI LOYTYNY"

    def printtaa_k(lista):
          """ Tama on vain testaukseen liittyva metodi. Tulostaa 
              kaikkien listassa olevien kysymysten tiedot. """
          print lista
          for kyssari in lista:
              print "******"
              print "Kysymyksen ID on: " + kyssari.k_id
              print "Kysymyksen teksti on: " + kyssari.k_txt
              print "Kysymyksen vastaus_ID:t on: " + kyssari.k_vid1 + ", " + kyssari.k_vid2 + ", " +  kyssari.k_vid3 + ", " +  kyssari.k_vid4
   
    def printtaa_v(lista):
        """ Tama on vain testaukseen liittyva metodi. Tulostaa 
            kaikkien listassa olevien vastausten tiedot. """
        print lista
        for vastaus in lista:
            print "******"
            print "Vastauksen ID on: " + vastaus.v_id
            print "Vastauksen teksti on: " + vastaus.v_txt
            print "Vastauksen s_id on: " + vastaus.v_skid
   
    def animointi(self, value):
        """ Maaritetaan points listan luvut. Naiden 
            lukujen perusteella piirretaan monitorin viiva. """
        # Tee kaikista animoitni metodeista yksi
        dt = 0.5
        cy = 480.00
        cx = 0.00
        w = 380.00
        step = 10
        points = []
        self.dt += dt
        for i in xrange(int(w / step)):
            x = i * step
            points.append(cx + x)
            points.append(cy + cos(x / w * 8. + self.dt) * 240.00 * 0.2)
        self.points = points
   
    def animointi_2(self, value):
        """ Maaritetaan points2 listan luvut. Naiden 
            lukujen perusteella piirretaan monitorin viiva. """
        dt = 0.5
        cy = 600.00
        cx = 0.00
        w = 380.00
        step = 10
        points = []
        self.dt += dt
        for i in xrange(int(w / step)):
            x = i * step
            points.append(cx + x)
            points.append(cy + cos(x / w * 8. + self.dt) * 240.00 * 0.2)
        self.points2 = points
   
    def animointi_3(self, value):
            """ Maaritetaan points3 listan luvut. Naiden 
                lukujen perusteella piirretaan monitorin viiva. """
            dt = 1.5
            cy = 720.00
            cx = 0.00
            w = 380.00
            step = 10
            points = []
            self.dt += dt
            for i in xrange(int(w / step)):
                x = i * step
                points.append(cx + x)
                points.append(cy + cos(x / w * 8. + self.dt) * 240.00 * 0.2)
            self.points3 = points

    def palikka_anim_start(self, value):
          """ Purkkaa. Metodi kaynnistaa animaation """
          self.animointi(self)
          self.animointi_2(self)
          self.animointi_3(self)
          Clock.schedule_interval(self.paivita_palikan_paikka, 0)
    
    def paivita_palikan_paikka(self, dt):
        """ Liikuttaa naytolla liikkuvaa mustaa palikkaa. """
        if self.palikan_koko[0] > 15:
            self.palikan_koko[0] += -1
        self.palikan_paikka[0] += 1
        if self.palikan_paikka[0] == 360:
            self.palikan_paikka[0] = 0
    
    def aloita_naytto(self, value):
        """ Purkkaa. Metodi kaynnistaa animaation """
        self.animointi(self)
        self.animointi_2(self)
        self.animointi_3(self)
        Clock.schedule_interval(self.paivita_palikan_paikka, 0)
        return " "   
          
    alustaPeli(self)

class TestLineApp(App):
    Appi = LinePlayground()

    def build(self):
        return self.Appi
    def aloitaAlusta(self):
        self.Appi.aloitaAlusta()


if __name__ == '__main__':
    peli = TestLineApp()
    try:
        peli.run()
    except UusiksMeni:
        print "VIRHE NAPATTU!!!"
        peli.aloitaAlusta()
