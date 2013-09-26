namespace Tietovisa
{
    /// <summary>
    ///  Erilaisiin yksinkertaisiin peleihin soveltuva Kilpailija luokka, joka ylläpitää tietoja kilpailijan nimimerkistä ja pisteistä.
    /// </summary>
    class Kilpailija
    {
        /// <summary>
        /// Kilpailijan nimimerkki
        /// </summary>
        private string privaattiNimimerkki;
        /// <summary>
        /// Kilpailijan pisteet
        /// </summary>
        private int privaattiPisteet;

        /// <summary>
        /// Kilpailijan käyttämä nimimerkki
        /// </summary>
        public string Nimimerkki
        {
            get
            {
                return privaattiNimimerkki;
            }
            set
            {
                privaattiNimimerkki = value;
            }
        }

        /// <summary>
        /// Kilpailijan pistemäärä
        /// </summary>
        public int Pisteet
        {
            get
            {
                return privaattiPisteet;
            }
            set
            {
                privaattiPisteet = value;
            }
        }


        /// <summary>
        /// Parametritön muodostaja asettaa kilpailijalle oletusnimen "Kilapilija" ja pisteiksi 0
        /// </summary>
        public Kilpailija()
        {
            privaattiNimimerkki = "Kilapilija";
            privaattiPisteet = 0;
        }

        /// <summary>
        /// Muodostaja joka ottaa vastaan parametreinä halutun nimimerkin ja pistemäärän.
        /// </summary>
        /// <param name="nimi">Kilpailijalle annettava nimimerkki</param>
        /// <param name="pointsit">Kilpailijalle annettava pistemäärä</param>
        public Kilpailija(string nimi, int pointsit)
        {
            privaattiNimimerkki = nimi;
            privaattiPisteet = pointsit;
        }

        /// <summary>
        /// Metodi, joka lisää kilpailijalle yhden pisteen
        /// </summary>
        public void lisaaPiste()
        {
            privaattiPisteet++;
        }

        /// <summary>
        /// Metodi, joka lisää kilpailijalle x määrän pisteitä
        /// </summary>
        /// <param name="x">Pistemäärä joka kilpailijalle halutaan lisätä</param>
        public void lisaaPisteita(int x)
        {
            privaattiPisteet = privaattiPisteet + x;
        }

        /// <summary>
        /// Metodi, joka vähentää kilpailijalta yhden pisteen
        /// </summary>
        public void vahennaPiste()
        {
            privaattiPisteet--;
        }

        /// <summary>
        /// Metodi, joka vähentää kilpailijalta x määrän pisteitä
        /// </summary>
        /// <param name="x">Pistemäärä joka kilpailijalta halutaan vähenntää</param>
        public void vahennaPisteita(int x)
        {
            privaattiPisteet = privaattiPisteet - x;
        }

        /// <summary>
        /// Palauttaa kilpailijan tiedot merkkijonona muodossa: Nimimerkki|Pisteet (Esim. Kilpailija|0)
        /// </summary>
        /// <returns>Kilpailijan tiedot merkkijonona</returns>
        public string Merkkijonoksi()
        {
            return "" + privaattiNimimerkki + "|" + privaattiPisteet;
        }

    }

}
