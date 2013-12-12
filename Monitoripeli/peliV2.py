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
        pos: 0, -120
        font_size: 18
        text: root.label_txt

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
    title: 'Popup'
    
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
    title: 'Popup'
    
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
        Popup.__init__(self, title=title)
        self.content = VaaraContent(text, self)

    def lopetaPeli(self):
        sys.exit()

class SkenLapiPopup(Popup):

    def lopetaPeli(self):
        sys.exit()

class PeliLapiPopup(Popup):

    def lopetaPeli(self):
        sys.exit()

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

    def seuraavaSkenaario(self):
        self.peli.asetaSeuraavaSkenaario()
        self.paivitaNaytto()

    peli = DataManager()

    label_txt = StringProperty(peli.kysymys_nyt.k_txt)
    a_btn_txt = StringProperty(peli.vastaukset_nyt[0].v_txt)
    b_btn_txt = StringProperty(peli.vastaukset_nyt[1].v_txt)
    c_btn_txt = StringProperty(peli.vastaukset_nyt[2].v_txt)
    d_btn_txt = StringProperty(peli.vastaukset_nyt[3].v_txt)
    selitys = StringProperty(peli.selitys_nyt)

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