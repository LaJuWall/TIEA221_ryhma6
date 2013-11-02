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

Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '800')

#kysymykset = open("k_elaimet.txt")
#taulukko = [row.replace(" ", "").strip('\n').split('|') for row in kysymykset]
#taulukko = kysymykset.readlines()
#kysymykset.close()
#print(taulukko)



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
            points: (0, 480, 374, 480)

        Color:
            rgba: .1, .1, 1, .9
        Line:
            width: 2.
            points: (0, 600, 374, 600)

        Color:
            rgba: .1, 1, .1, .9
        Line:
            width: 2.
            points: (0, 720, 374, 720)

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
        text: root.label_txt

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
                text: 'B'
                on_press: root.b_press(self)

            Button:
                text: 'C'
                on_press: root.c_press(self)

            Button:
                text: 'D'
                on_press: root.d_press(self)

''')


class KysymysLista():
    def __init__(self):
        kysymykset = open("k_elaimet.txt")
        self.taulukko = [row.strip().split('|') for row in kysymykset]
        #taulukko = kysymykset.readlines()
        kysymykset.close()
        self.taulukko.pop(0)

class VastausLista():
    def __init__(self):
        vastaukset = open("v_elaimet.txt")
        self.taulukko = [row.strip().split('|') for row in vastaukset]
        #taulukko = kysymykset.readlines()
        vastaukset.close()
        self.taulukko.pop(0)

class SelitystenLista():
    def __init__(self):
        selitykset = open("s_elaimet.txt")
        self.taulukko = [row.strip().split('|') for row in selitykset]
        #taulukko = kysymykset.readlines()
        selitykset.close()
        self.taulukko.pop(0)

class Kysymys():
    def __init__(self, k_id=None, k_txt=None, k_vid1=None, k_vid2=None, k_vid3=None, k_vid4=None):
        self.k_id = k_id
        self.k_txt = k_txt
        self.k_vid1 = k_vid1
        self.k_vid2 = k_vid2
        self.k_vid3 = k_vid3
        self.k_vid4 = k_vid4

class Vastaus():
    def __init__(self, v_id=None, v_txt=None, v_skid=None):
        self.v_id = v_id
        self.v_txt = v_txt
        self.v_skid = v_skid

class Selitys():
    def __init__(self, s_id=None, s_txt=None):
        self.s_id = s_id
        self.s_txt = s_txt

class LinePlayground(FloatLayout):
    
    kysymykset = KysymysLista()
    print "****************"
    print kysymykset.taulukko
    print "****************"
    
    vastaukset = VastausLista()
    print "****************"
    print vastaukset.taulukko
    print "****************"
    
    selitykset = SelitystenLista()
    print "****************"
    print vastaukset.taulukko
    print "****************"

    a_btn_txt = StringProperty('''A''')
    b_btn_txt = StringProperty('''B''')
    c_btn_txt = StringProperty('''C''')
    d_btn_txt = StringProperty('''D''')
    label_txt = StringProperty('''TASSA ON KYMYSYS''')
    sound = SoundLoader.load('testi.wav')
    if sound:
        print("Sound found at %s" % sound.source)
        print("Sound is %.3f seconds" % sound.length)
        sound.play()
    if not sound:
        print("EI SE MUSA TOIMI!!!")
    
    def a_press(instance, value):
        print instance.a_btn_txt
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        instance.a_btn_txt = "Nyt A vaihtui"
        instance.label_txt = "Nyt kysymys vaihtui"
        popup = Popup(title="Painoit nappulaa!",
            content=Label(text='Painoit A:ta'),
            size_hint=(None, None),
            size=(400, 400))
        popup.open()
        print instance.a_btn_txt

    def b_press(instance, value):
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        popup = Popup(title="Painoit nappulaa!",
            content=Label(text='Painoit B:ta'),
            size_hint=(None, None),
            size=(400, 400))
        popup.open()

    def c_press(instance, value):
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        popup = Popup(title="Painoit nappulaa!",
            content = Label(text="Painoit C:ta"),
            size_hint=(None, None),
            size=(400, 400))
        popup.open()

    def d_press(instance, value):
        sound = SoundLoader.load('testi2.wav')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()
        if not sound:
            print("EI SE AANI TOIMI!!!")
        popup = Popup(title="Painoit nappulaa!",
            content=Label(text='Painoit D:ta'),
            size_hint=(None, None),
            size=(400, 400))
        popup.open()

class TestLineApp(App):
    def build(self):
        return LinePlayground()


if __name__ == '__main__':
    TestLineApp().run()
