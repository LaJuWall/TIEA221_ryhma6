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

""" Maaritetaan ikkunan korkeus ja leveys. """
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')

########## 1.KAYTTOLIITTYMAN MAARITTELY ##########

""" Maaritetaan naytoon piirtyvat elementit ja niiden ominaisuudet. """
Builder.load_string('''
<MonitoriPeli>:
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

    Label:
        id: pulssi
        pos: 185, 370
        font_size: 18
        text: root.pulssi

    Label:
        id: happisaturaatio
        pos: 185, 270
        font_size: 18
        text: root.happiS

    Label:
        id: verenpaine
        pos: 185, 170
        font_size: 18
        text: root.verP

    Label:
        id: co2
        pos: 185, 70
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
        pos: 0, -120
        font_size: 18
        text: root.label_txt

    Button:
        pos: 0, 775
        size_hint: None, None
        size: 95, 25
        text: root.aanet_txt
        on_press: root.toggleSound()

    Button:
        pos: 96, 775
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
                text: root.a_btn_txt
                on_press: root.a_press()

            Button:
                text: root.b_btn_txt
                on_press: root.b_press()

            Button:
                text: root.c_btn_txt
                on_press: root.c_press()

            Button:
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
            on_press: root.dismiss()

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
            on_press: root.dismiss()

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
            text_size: None, None
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

''')


class VaaraContent(BoxLayout):
    text = StringProperty("")
    textlabel = ObjectProperty()

    def __init__(self, text, parent):
        BoxLayout.__init__(self)
        self.text = text
        self.myparent = parent

    def on_close_button_clicked(self):
        self.myparent.dismiss()

    def alotaAlusta(self):
        self.myparent.myparent.peli.aloitaAlusta()
        self.myparent.myparent.paivitaNaytto()
        self.myparent.dismiss()

    def sulje(self):
        sys.exit()

class VaaraPopup(Popup):

    def __init__(self, title, text, parent):
        self.myparent = parent
        Popup.__init__(self, title=" ", separator_color=[0.15, 0.15, 0.15, 0.15])
        self.content = VaaraContent(text, self)

    def lopetaPeli(self):
        sys.exit()

class AlkuContent(BoxLayout):

    def __init__(self, parent):
        BoxLayout.__init__(self)
        self.myparent = parent

    def on_close_button_clicked(self):
        sys.exit

    def alotaAlusta(self):
        sys.exit

    def sulje(self):
        sys.exit()

class MainMenu(Popup):

    def __init__(self):
        Popup.__init__(self)
        self.content = AlkuContent(self)

    def lopetaPeli(self):
        sys.exit()

class SkenLapiPopup(Popup):

    def lopetaPeli(self):
        sys.exit()

class PeliLapiPopup(Popup):

    def lopetaPeli(self):
        sys.exit()

class InfoPopup(Popup):
    pass

class MonitoriPeli(FloatLayout):

    def a_press(self):
        self.jatketaanko(self.peli.vastaukset_nyt[0].v_skid)

    def b_press(self):
        self.jatketaanko(self.peli.vastaukset_nyt[1].v_skid)

    def c_press(self):
        self.jatketaanko(self.peli.vastaukset_nyt[2].v_skid)

    def d_press(self):
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
                p = SkenLapiPopup()
                p.open()
            else:
                self.peli.aloitaAlusta()
                self.paivitaNaytto()
                p = PeliLapiPopup()
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

    def seuraavaSkenaario(self):
        self.peli.asetaSeuraavaSkenaario()
        self.paivitaNaytto()

    def toggleSound(self):
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

    def NaytaInfo(self):
        poppi = InfoPopup()
        poppi.open()

    peli = DataManager()
    aanet = True
    aanet_txt = StringProperty("Äänet pois")

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

    sound = SoundLoader.load('testi.wav')
    if sound:
        print("Sound found at %s" % sound.source)
        print("Sound is %.3f seconds" % sound.length)
        sound.play()
    if not sound:
        print("EI SE MUSA TOIMI!!!")

class Peli(App):
    def build(self):
        return MonitoriPeli()

if __name__ == '__main__':
    Peli().run()