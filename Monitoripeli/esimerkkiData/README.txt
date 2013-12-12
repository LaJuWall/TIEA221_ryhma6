Haluttu tiedostorakenne on seuraava (kaksi skenaariota, joiden nimet ovat esim ja esim2):

Datakansio
|
+--> skenaariot.txt
	 pohjustukset.txt
	 esim_kys.txt
	 esim_vas.txt
	 esim_sel.txt
	 esim2_kys.txt
	 esim2_vas.txt
	 esim2_sel.txt

Muista nimetä yllä olevaan tyyliin. Eli esim. "esim2" skenaarion tiedostot on nimetty esim2_kys.txt jne...

Seuraavissa selityksissä laatikoiden sisällä on esimerkki tiedostoista löytyvä data.

**** skenaariot.txt ****

Tähän tiedostoon tulee kaikkien skenaarioiden id:t (Nimet)

+skenaariot.txt-----+
| id 				|
| esim 				|
| esim2				|
+-------------------+

id = Skenaarion nimi/id

**** pohjustuket.txt ****

Tähän tiedostoon laitetaan skenaarioihin (mahdollisesti) liittyvät pohjustukset

+pohjustukset.txt------------+
| sken_id |pohj_txt       |  |
| esim2   |liiba_laaba    |  |
+----------------------------+

sken_id = skenaarion nimi, johon tämän rivin pohjustus liittyy
pohj_txt = pohjustus

**** _kys.txt ****

Tähän tiedostoon siis kaikki kysymyksiin liittyvät tiedot.

+esim_kys.txt-------------------------------------------------------------------------------------------------------------------------+
| kys_id |kys_txt       |vas_id1 |vas_id2 |vas_id3 |vas_id4 |sel_id |ar_pul |ar_haps |ar_verp |ar_co2 |ar_bis |ar_mac |ar_lamp |      |
| 01     |eka_kysymys   |001     |002     |002     |002     |01     |101    |102     |103     |104    |105    |106    |107     |      |
| 02     |toka_kysymys  |002     |002     |003     |002     |01     |201    |202     |203     |204    |205    |206    |207     |      |
| 03     |kolmas_kysymys|002     |004     |002     |002     |01     |301    |302     |303     |304    |305    |306    |307     |      |
| 04     |neljas_kysymys|002     |002     |002     |005     |01     |401    |402     |403     |404    |405    |406    |407     |      |
+-------------------------------------------------------------------------------------------------------------------------------------+

kys_id = Kysymyksen id
kys_txt = Kysymyksen teksti
vas_id1 = vastauksen 1 id
vas_id2 = vastauksen 2 id
vas_id3 = vastauksen 3 id
vas_id4 = vastauksen 4 id
sel_id = Tähän kysymykseen liittyvän selityksen id
ar_pul = Tähän kysymykseen sidottu pulssin arvo
ar_haps = Tähän kysymykseen sidottu happisaturaation arvo
ar_verp = Tähän kysymykseen sidottu verenpaineen arvo
ar_co2 = Tähän kysymykseen sidottu co2 (hiilidioksidi) arvo
ar_bis = Tähän kysymykseen sidottu BIS arvo
ar_mac = Tähän kysymykseen sidottu MAC arvo

**** _vas.txt ****

Tähän tiedostoon tulee kaikki vastauksiin liittyvät tiedot

+esim_vas.txt------------------+
| vas_id |vas_txt |kys_id |    |
| 001    |oikein  |02     |    |
| 002    |vaarin  |00     |    |
| 003    |oikein  |03     |    |
| 004    |oikein  |04     |    |
| 005    |oikein  |01     |    |
+------------------------------+

vas_id = vastauksen id
vas_txt = vastauksen teksti
kys_id = mikäli vastaus on väärä, laita tähän 00. Mikäli vastaus on oikein ja skenaario päättyy, laita 01. Mikäli vastaus on oikein ja skenaario jatkuu, laita seuraavan kysymyksen id

**** _sel.txt ****

Tähän tiedostoon tulee kaikki selityksiin liittyvät tiedot

+esim_sel.txt---------------------+
| sel_id |sel_txt             |   |
| 01     |tassapa_on_selitysta|   |
+---------------------------------+

sel_id = tämän selityksen id
sel_txt = selityksen teksti