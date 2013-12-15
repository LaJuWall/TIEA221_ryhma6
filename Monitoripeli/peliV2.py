# -*- coding:utf-8 -*-
from kivy.app import App
from kivy.properties import OptionProperty, NumericProperty, ListProperty, \
        BooleanProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.clock import Clock
from math import cos, sin
from kivy.config import Config
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
import random
import dataManageri
from dataManageri import DataManager
import sys
from decimal import Decimal

""" Maaritetaan ikkunan korkeus ja leveys. """
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')

########## 1.KAYTTOLIITTYMAN MAARITTELY ##########

""" Maaritetaan naytoon piirtyvat elementit ja niiden ominaisuudet. """
Builder.load_string('''
<Tausta>:
    Label:
        opacity: 0
        pos: 0, 0
        text: root.startUp()

<Menuu>:
    FloatLayout:
        Label:
            text: 'Tervetuloa monitoripeliin'
            font_size: 30
            size_hint: None, None
            pos: root.width * .4, 600
        Button:
            text: 'Aloita peli'
            size_hint: None, None
            on_press: root.klikki()
            pos: root.width * .15, 250
            size: root.width * .7, 100
        Button:
            text: 'Info'
            size_hint: None, None
            on_press: root.NaytaInfo()
            pos: root.width * .15, 150
            size: root.width * .7, 100
        Button:
            text: 'Sulje peli'
            size_hint: None, None
            on_press: root.sulje()
            pos: root.width * .15, 50
            size: root.width * .7, 100

<MonitoriPeli>:
    canvas:
        Rectangle:
            pos: root.width * 3 / 4, root.height * .5 -80
            size: 2, root.height * .5 + 80

        Rectangle:
            pos: 0, root.height * .5 - 80
            size: root.width, 2

        Rectangle:
            pos: 0, root.height * .5
            size: root.width, 2

        # Käyrät
        Color:
            rgba: 1, .1, .1, .9
        Line:
            width: 2.
            points: root.points

        Color:
            rgba: 1, 1, .1, .9
        Line:
            width: 2.
            points: root.points2

        Color:
            rgba: .1, 1, .1, .9
        Line:
            width: 2.
            points: root.points3

        Color:
            rgba: 1, 1, 1, .9
        Line:
            width: 2.
            points: root.points4

        Color
            rgba: 0, 0, 0, 1
        Rectangle:
            pos: root.palikan_paikka
            size: root.palikan_koko


    Label:
        pos: -500, -500
        font_size: 1
        text: root.aloita_naytto(self)

    Label:
        id: pulssi
        pos: root.width * .35, 350
        font_size: 18
        text: root.pulssi

    Label:
        id: happisaturaatio
        pos: root.width * .35, 250
        font_size: 18
        text: root.happiS

    Label:
        id: verenpaine
        pos: root.width * .35, 150
        font_size: 18
        text: root.verP

    Label:
        id: co2
        pos: root.width * .35, 50
        font_size: 18
        text: root.co2

    Label:
        id: BIS
        pos: -185, -43
        font_size: 18
        text: root.bis

    Label:
        id: MAC
        pos: -75, -43
        font_size: 18
        text: root.mac

    Label:
        id: lampotila
        pos: 35, -43
        font_size: 18
        text: root.lamp

    Label:
        pos: 10, -120
        text_size: root.width, 40
        font_size: 18
        text: root.label_txt

    Button:
        pos: 0, root.height -25
        size_hint: None, None
        size: 95, 25
        text: root.aanet_txt
        on_press: root.toggleSound()

    Button:
        pos: 96, root.height -25
        size_hint: None, None
        size: 95, 25
        text: 'Info'
        on_press: root.NaytaInfo()

    GridLayout:
        cols: 2
        size_hint: 1, None
        height: 240

        GridLayout:
            cols: 2

            Button:
            	text_size: root.width*.4, 50
                text: root.a_btn_txt
                on_press: root.a_press()

            Button:
            	text_size: root.width * .4 , 50
                text: root.b_btn_txt
                on_press: root.b_press()

            Button:
            	text_size: root.width * .4 , 50
                text: root.c_btn_txt
                on_press: root.c_press()

            Button:
            	text_size: root.width * .4 , 50
                text: root.d_btn_txt
                on_press: root.d_press()

<SkenLapiPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Monitoripeli'
    
    GridLayout:
        cols: 1

        Label:
            text: 'Skenaario suoritettu!'

        Button:
            text: 'Seuraava skenaario!'
            on_press: root.seuraavaSkeni()

        Button:
            text: 'Sulje peli'
            on_press: root.lopetaPeli()

<PeliLapiPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Monitoripeli'
    
    GridLayout:
        cols: 1

        Label:
            text: 'Kaikkiin kysymyksiin vastattu oikein!'

        Button:
            text: 'Aloita alusta'
            on_press: root.seuraavaSkeni()

        Button:
            text: 'Sulje peli'
            on_press: root.lopetaPeli()

<VaaraContent>:
    
    orientation: 'horizontal'
    textlabel: textlabel
    padding: 10
    spacing: 10

    GridLayout:

        cols: 1

        Label:
            text_size: root.width, 250
            id: textlabel
            text: root.text
            bold: True
            font_size: '25sp'
        Widget:
            heigth: 5
        GridLayout:
            cols: 1

        Button:
            id: close_button
            text: 'Yritä uudestaan'
            font_size: '30sp'
            on_press: root.on_close_button_clicked()

        Button:
            id: alusta_button
            text: 'Aloita alusta'
            font_size: '30sp'
            on_press: root.alotaAlusta()

        Button:
            id: sulje_button
            text: 'Lopeta peli'
            font_size: '30sp'
            on_press: root.sulje()

<AlkuContent>:
    
    orientation: 'horizontal'
    padding: 10
    spacing: 10

    GridLayout:

        cols: 1

        Label:
            text: 'Tervetuloa monitoripeliin'
            bold: True
            font_size: '25sp'
        Widget:
            heigth: 5
        GridLayout:
            cols: 1

        Button:
            id: close_button
            text: 'Aloita peli'
            font_size: '30sp'
            on_press: root.on_close_button_clicked()

        Button:
            id: alusta_button
            text: 'Info'
            font_size: '30sp'
            on_press: root.alotaAlusta()

        Button:
            id: sulje_button
            text: 'Sulje peli'
            font_size: '30sp'
            on_press: root.sulje()

<InfoPopup>:
    size_hint: .5, .5
    auto_dismiss: False
    title: 'Info'
    
    GridLayout:
        cols: 1


        Label:
            pos: 0, 0
            text_size: root.width - 15, 70
            padding_x: -7
            padding_y: -9
            text: 'Tekijät: Lasse Wallden, Janne Virkkunen, Kristiina Manninen & Reeta Parkkonen'

        Label:
            pos: 0, 0
            text_size: root.width - 15, 130
            padding_x: -7
            padding_y: -10
            text: 'Musiikki: "The Complex" Kevin MacLeod (incompetech.com) Licensed under Creative Commons: By Attribution 3.0 http://creativecommons.org/ licenses/by/3.0/'

        Button:
            text: 'Sulje'
            on_press: root.dismiss()

<PohjaContent>:
    
    orientation: 'horizontal'
    textlabel: textlabel
    padding: 10
    spacing: 10

    GridLayout:

        cols: 1

        Label:
            text_size: root.width, 100
            id: textlabel
            text: root.text
            bold: True
            font_size: '25sp'
        Widget:
            heigth: 5
        GridLayout:
            cols: 1

        Button:
            id: close_button
            text: 'Jatka'
            font_size: '30sp'
            on_press: root.on_close_button_clicked()

''')

class PohjaContent(BoxLayout):
    text = StringProperty("")
    textlabel = ObjectProperty()

    def __init__(self, text, parent):
        BoxLayout.__init__(self)
        self.text = text
        self.myparent = parent

    def on_close_button_clicked(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.myparent.dismiss()

class PohjaPopup(Popup):

    def __init__(self, text, parent):
        self.myparent = parent
        Popup.__init__(self, title=" ", separator_color=[0.15, 0.15, 0.15, 0.15])
        self.content = PohjaContent(text, self)

class VaaraContent(BoxLayout):
    text = StringProperty("")
    textlabel = ObjectProperty()

    def __init__(self, text, parent):
        BoxLayout.__init__(self)
        self.text = text
        self.myparent = parent

    def on_close_button_clicked(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.myparent.dismiss()

    def alotaAlusta(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.myparent.myparent.peli.aloitaAlusta()
        self.myparent.myparent.paivitaNaytto()
        self.myparent.dismiss()

    def sulje(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit()

class VaaraPopup(Popup):

    def __init__(self, title, text, parent):
        self.myparent = parent
        Popup.__init__(self, title=" ", separator_color=[0.15, 0.15, 0.15, 0.15])
        self.content = VaaraContent(text, self)

    def lopetaPeli(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit()

class AlkuContent(BoxLayout):

    def __init__(self, parent):
        BoxLayout.__init__(self)
        self.myparent = parent

    def on_close_button_clicked(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit

    def alotaAlusta(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit

    def sulje(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit()

class MainMenu(Popup):

    def __init__(self):
        Popup.__init__(self)
        self.content = AlkuContent(self)

    def lopetaPeli(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit()

class SkenLapiPopup(Popup):

    def __init__(self, parent):
        Popup.__init__(self)
        self.myparent = parent

    def lopetaPeli(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit()

    def seuraavaSkeni(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.myparent.pohjustus2 = self.myparent.peli.pohjustukset.annaPohjustus(self.myparent.peli.skenaario_nyt)
        self.myparent.pohjustus = self.myparent.pohjustus2.p_txt
        poppi = PohjaPopup(self.myparent.pohjustus, self.myparent)
        poppi.open()
        self.dismiss()

class PeliLapiPopup(Popup):

    def __init__(self, parent):
        Popup.__init__(self)
        self.myparent = parent

    def lopetaPeli(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit()

    def seuraavaSkeni(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.myparent.pohjustus2 = self.myparent.peli.pohjustukset.annaPohjustus(self.myparent.peli.skenaario_nyt)
        self.myparent.pohjustus = self.myparent.pohjustus2.p_txt
        poppi = PohjaPopup(self.myparent.pohjustus, self.myparent)
        poppi.open()
        self.dismiss()

class InfoPopup(Popup):
    pass

class MonitoriPeli(FloatLayout):

    def a_press(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.jatketaanko(self.peli.vastaukset_nyt[0].v_skid)

    def b_press(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.jatketaanko(self.peli.vastaukset_nyt[1].v_skid)

    def c_press(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.jatketaanko(self.peli.vastaukset_nyt[2].v_skid)

    def d_press(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        self.jatketaanko(self.peli.vastaukset_nyt[3].v_skid)
        
    def jatketaanko(self, h_id):
        if h_id == "00":
            print "VAARA VASTAUS NAPATTU!!!!"
            selitys = self.peli.selitys_nyt.s_txt
            print selitys
            poppi = VaaraPopup("Vastasit vaarin", selitys, self)
            poppi.open()

        
        if h_id == "01":
            if len(self.peli.skenaariot.skenaariot) > 0:
                self.peli.asetaSeuraavaSkenaario()
                self.paivitaNaytto()
                p = SkenLapiPopup(self)
                p.open()
            else:
                self.peli.aloitaAlusta()
                self.paivitaNaytto()
                p = PeliLapiPopup(self)
                p.open()
       
        else:
            self.peli.asetaSeuraavaKysymys(h_id)
            self.paivitaNaytto()


    def paivitaNaytto(self):
        self.label_txt = self.peli.kysymys_nyt.k_txt
        self.a_btn_txt = self.peli.vastaukset_nyt[0].v_txt
        self.b_btn_txt = self.peli.vastaukset_nyt[1].v_txt
        self.c_btn_txt = self.peli.vastaukset_nyt[2].v_txt
        self.d_btn_txt = self.peli.vastaukset_nyt[3].v_txt
        self.pulssi = self.peli.kysymys_nyt.k_arPul
        self.happiS = self.peli.kysymys_nyt.k_arHaps
        self.verP = self.peli.kysymys_nyt.k_arVep
        self.co2 = self.peli.kysymys_nyt.k_arCo2
        self.bis = self.peli.kysymys_nyt.k_arBis
        self.mac = self.peli.kysymys_nyt.k_arMac
        self.lamp = self.peli.kysymys_nyt.k_arLamp
        self.animointi()
        self.animointi_2()
        self.animointi_3(self.pulssi)
        self.animointi_4()         

    def seuraavaSkenaario(self):
        self.peli.asetaSeuraavaSkenaario()
        self.pohjustus2 = self.peli.pohjustukset.annaPohjustus(self.peli.skenaario_nyt)
        self.pohjustus = self.pohjustus2.p_txt
        self.paivitaNaytto()
        poppi = PohjaPopup(self.pohjustus, self)
        poppi.open()

    def toggleSound(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        if self.aanet:
           self.aanet = False
           self.sound.stop()
           self.aanet_txt = "Äänet päälle"
        else:
           self.aanet = True
           self.sound.play()
           self.aanet_txt = "Äänet pois"

    def Aloitus(self):
        print "Tämä käynnistettiin!"
        mainMenu = MainMenu()
        mainMenu.open() 
        return " "        


    def animointi(self):
        """ Maaritetaan points listan luvut. Naiden 
            lukujen perusteella piirretaan monitorin viiva. """
        # Tee kaikista animoitni metodeista yksi
        dt = 0.5
        cy = Config.getint('graphics', 'height') * .6875
        cx = 0.00
        w = Config.getint('graphics', 'width') * .748
        step = 10
        points = []
        self.dt += dt
        for i in xrange(int(w / step)):
            x = i * step
            points.append(cx + x)
            points.append(cy + cos(x / w * 8. + self.dt) * 240.00 * 0.2)
        self.points = points
   
    def animointi_2(self):
        """ Maaritetaan points2 listan luvut. Naiden 
            lukujen perusteella piirretaan monitorin viiva. """
        dt = 0.5
        cy = Config.getint('graphics', 'height') * .8125
        cx = 0.00
        w = Config.getint('graphics', 'width') * .748
        step = 10
        points = []
        self.dt += dt
        for i in xrange(int(w / step)):
            x = i * step
            points.append(cx + x)
            points.append(cy + cos(x / w * 25. + self.dt) * 240.00 * 0.2)
        self.points2 = points
   
    def animointi_3(self, pulssi):
        """ Maaritetaan points3 listan luvut. Naiden 
            ukujen perusteella piirretaan monitorin viiva. """
        dt = 0.5
        cy = Config.getint('graphics', 'height') * .9375
        cx = 0.00
        w = Config.getint('graphics', 'width') * .748
        step = 10
        points = []
        self.dt += dt
        intervalli = (float(pulssi) / 100.0) * 1.5
        print intervalli
        for i in xrange(int(w / step)):
            x = i * step
            points.append(cx + x)
            points.append(cy + cos(x / w * (intervalli*10.) + self.dt) * 240.00 * 0.2)
        self.points3 = points

    def animointi_4(self):
        """ Maaritetaan points4 listan luvut. Naiden 
            ukujen perusteella piirretaan monitorin viiva. """
        dt = 0.5
        cy = Config.getint('graphics', 'height') * .5625
        cx = 0.00
        w = Config.getint('graphics', 'width') * .748
        step = 10
        points = []
        self.dt += dt
        for i in xrange(int(w / step)):
            x = i * step
            points.append(cx + x)
            points.append(cy + sin(x / w * 8. + self.dt) * 120.00 * 0.2)
        self.points4 = points

    def paivita_palikan_paikka(self, dt):
        """ Liikuttaa naytolla liikkuvaa mustaa palikkaa. """
        if self.palikan_koko[0] > 15:
            self.palikan_koko[0] += -1
        self.palikan_paikka[0] += 1
        if self.palikan_paikka[0] == 360:
            self.palikan_paikka[0] = 0

    def NaytaInfo(self):
    	sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        poppi = InfoPopup()
        poppi.open()

    peli = DataManager()
    aanet = True
    aanet_txt = StringProperty("Äänet pois")

    dt = NumericProperty(0)
    palikan_paikka = ListProperty([0, Config.getint('graphics', 'height')* .5 + 5])
    palikan_koko = ListProperty([Config.getint('graphics', 'width')* .748, Config.getint('graphics', 'height')* .5 ])

    label_txt = StringProperty(peli.kysymys_nyt.k_txt)
    a_btn_txt = StringProperty(peli.vastaukset_nyt[0].v_txt)
    b_btn_txt = StringProperty(peli.vastaukset_nyt[1].v_txt)
    c_btn_txt = StringProperty(peli.vastaukset_nyt[2].v_txt)
    d_btn_txt = StringProperty(peli.vastaukset_nyt[3].v_txt)
    selitys = StringProperty(peli.selitys_nyt)
    pulssi = StringProperty(peli.kysymys_nyt.k_arPul)
    happiS = StringProperty(peli.kysymys_nyt.k_arHaps)
    verP = StringProperty(peli.kysymys_nyt.k_arVep)
    co2 = StringProperty(peli.kysymys_nyt.k_arCo2)
    bis = StringProperty(peli.kysymys_nyt.k_arBis)
    mac = StringProperty(peli.kysymys_nyt.k_arMac)
    lamp = StringProperty(peli.kysymys_nyt.k_arLamp)
    pohjustus2 = peli.pohjustukset.annaPohjustus(peli.skenaario_nyt)
    pohjustus = pohjustus2.p_txt
    points = ListProperty([0, Config.getint('graphics', 'height') * .6875, Config.getint('graphics', 'width') * .748, Config.getint('graphics', 'height') * .6875])  # toiseksi alimman käytän pisteet
    points2 = ListProperty([0, Config.getint('graphics', 'height') * .8125, Config.getint('graphics', 'width') * .748, Config.getint('graphics', 'height') * .8125]) # toiseksi ylimmän käyrän pisteet
    points3 = ListProperty([0, Config.getint('graphics', 'height') * .9375, Config.getint('graphics', 'width') * .748, Config.getint('graphics', 'height') * .9375]) # ylimmän käyrän pisteet
    points4 = ListProperty([0, Config.getint('graphics', 'height') * .562, Config.getint('graphics', 'width') * .748, Config.getint('graphics', 'height') * .5625])  # alimman käytän pisteet

    sound = SoundLoader.load('testi.WAV')
    if sound:
        #print("Sound found at %s" % sound.source)
        #print("Sound is %.3f seconds" % sound.length)
        sound.play()
    if not sound:
        print("EI SE AANI TOIMI!!!")

    def aloita_naytto(self, value):
        """ Purkkaa. Metodi kaynnistaa animaation """
        self.animointi()
        self.animointi_2()
        self.animointi_3(self.pulssi)
        self.animointi_4()
        Clock.schedule_interval(self.paivita_palikan_paikka, 0)
        return " "  

class Menuu(FloatLayout):
    def __init__(self, parent):
        FloatLayout.__init__(self)
        self.myparent = parent

    def klikki(self):
        lisattava = MonitoriPeli()
        self.myparent.add_widget(lisattava)
        poppi = PohjaPopup(lisattava.pohjustus, lisattava)
        poppi.open()
        self.myparent.remove_widget(self)
        sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")

    def NaytaInfo(self):
        poppi = InfoPopup()
        poppi.open()
        sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")

    def sulje(self):
        sound = SoundLoader.load('bliip.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        sys.exit()


class Tausta(FloatLayout):

    def startUp(self):
        lisattava = Menuu(self)
        self.add_widget(lisattava)
        return " "



class Peli(App):
    def build(self):
        return Tausta()

if __name__ == '__main__':
    Peli().run()