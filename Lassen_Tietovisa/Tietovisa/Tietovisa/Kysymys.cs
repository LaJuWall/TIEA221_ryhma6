using System;
using System.Text;

namespace Tietovisa
{
 
    /// <summary>
    /// Luokka, joka ylläpitää yksittäisen kysymyksen tietoja.
    /// </summary>
    public class Kysymys
    {
        /// <summary>
        /// merkkijono, joka sisältää itse kysymyksen (Esim. "Paljonko on 1+1?")
        /// </summary>
        public string itsekysymys;
        /// <summary>
        /// merkkijono, joka sisältää vastausvaihtoehdon A
        /// </summary>
        public string vaihtoehtoA;
        /// <summary>
        /// merkkijono, joka sisältää vastausvaihtoehdon B
        /// </summary>
        public string vaihtoehtoB;
        /// <summary>
        /// merkkijono, joka sisältää vastausvaihtoehdon C
        /// </summary>
        public string vaihtoehtoC;
        /// <summary>
        /// merkkijono, joka sisältää vastausvaihtoehdon D
        /// </summary>
        public string vaihtoehtoD;
        /// <summary>
        /// merkkijono, joka sisältää oikean vastausvahtoehdon kirjaimen
        /// </summary>
        public string oikeaVastaus;

        /// <summary>
        /// Parametritän muodostaja
        /// </summary>
        public Kysymys()
        {
            itsekysymys = "Kysymys";
            vaihtoehtoA = "A";
            vaihtoehtoB = "B";
            vaihtoehtoC = "C";
            vaihtoehtoD = "D";
            oikeaVastaus = "A";
        }

        /// <summary>
        /// Parametrillinen muodostaja, joka ottaa parametriksi merkkijonon, jonka pohjalta kysymys muodostetaan
        /// </summary>
        /// <param name="syote">merkkijono, joka sisältää kaikki kysymykselle tarpeelliset tiedot.</param>
        public Kysymys(string syote)
        {
            StringBuilder apuriBuilder = new StringBuilder();
            apuriBuilder.Append(syote);

            itsekysymys = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            vaihtoehtoA = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            vaihtoehtoB = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);
            
            vaihtoehtoC = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);
            
            vaihtoehtoD = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            oikeaVastaus = Convert.ToString(apuriBuilder);       


        }

        /// <summary>
        /// Palauttaa "eka|toka|kolmas" tyylisestä merkkijonosta osan "eka"
        /// </summary>
        /// <param name="teksti">merkkijono, josta tietoa halutaan irrottaa</param>
        /// <returns>annetun merkkijonon sisältö indeksistä 0, seuraavaan '|' merkkiin asti</returns>
        public string erotaSeuraava(string teksti)
        {

            string palaute = teksti.Substring(0, teksti.IndexOf('|'));

            return(palaute);
        
        }

        /// <summary>
        /// Metodi muodostaa kysymys luokan muuttujat merkkijonon pohjalta
        /// </summary>
        /// <param name="syote">merkkijono, josta halutaan alustaa muuttujien arvot</param>
        public void muodostaStringistä(String syote)
        {
            StringBuilder apuriBuilder = new StringBuilder();
            apuriBuilder.Append(syote);

            itsekysymys = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            vaihtoehtoA = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            vaihtoehtoB = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            vaihtoehtoC = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            vaihtoehtoD = erotaSeuraava(Convert.ToString(apuriBuilder));
            apuriBuilder = poistaKatsottu(apuriBuilder);

            oikeaVastaus = Convert.ToString(apuriBuilder);       
        
        }

        /// <summary>
        /// Poistaa "eka|toka|kolmas" tyylisestä merkkijonosta kaiken ensimmäisestä merkistä, ensimmäiseen '|' -merkkiin
        /// </summary>
        /// <param name="syote">merkkijono, josta merkkejä halutaan poistaa</param>
        /// <returns>merkkijonon, josta on poistettu ensimmäinen osio (Esim. "eka|")</returns>
        public StringBuilder poistaKatsottu(StringBuilder syote)
        {
            string apuri = Convert.ToString(syote);

            StringBuilder palaute = new StringBuilder();
            palaute.Append(apuri.Substring((apuri.IndexOf('|') + 1), (apuri.Length - (apuri.IndexOf('|') + 1))));

            return palaute;
        }

        /// <summary>
        /// Tarkistetaan, vastaako syöte oikeaVastaus -muuttujaa
        /// </summary>
        /// <param name="annettuVastaus">käyttäjän antama syöte</param>
        /// <returns>true, jos syöte on sama kuin muuttuja. Muutoin false</returns>
        public bool TarkistaVastaus(string annettuVastaus)
        {
            if (annettuVastaus == oikeaVastaus) return true;

            return false;
        }


    }
}