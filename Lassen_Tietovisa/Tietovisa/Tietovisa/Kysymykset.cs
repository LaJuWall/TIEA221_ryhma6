namespace Tietovisa
{
    /// <summary>
    /// Luokka, jonka tarkoitus on säilyttää merkkijono taulukossa kaikki käytössä olevat
    /// kysymykset. Taulukko kasvattaa kokoaan omatoimisesti, mikäli se on tarpeen.
    /// </summary>
    class Kysymykset
    {
        public string[] kysymystaulukko;
        public int seuraavaIndeksi;

        /// <summary>
        /// Parametritön muodostaja, joka luo 5 paikkaa suuren taulukon
        /// </summary>
        public Kysymykset()
        {
            kysymystaulukko = new string[5];
            seuraavaIndeksi = 0;
        }

        /// <summary>
        /// Muodostaja, joka luo alkuun parametrina tuodun kokonaisluvun suuruisen taulukon
        /// </summary>
        /// <param name="maara">kokonaisluku, jonka suuruinen taulukko luodaan.</param>
        public Kysymykset(int maara)
        {
            kysymystaulukko = new string[maara];
            seuraavaIndeksi = 0;
        }

        /// <summary>
        /// Lisätään parametrina tuotu merkkijono taulukkoon.
        /// </summary>
        /// <param name="lisattava">merkkijono, joka halutaan lisätä taulukkoon.</param>
        public void LisaaKysymys(string lisattava)
        {
            if (seuraavaIndeksi == (kysymystaulukko.Length - 2))
            {
                KasvataKokoa();
            }
               
            kysymystaulukko[seuraavaIndeksi] = lisattava;
            seuraavaIndeksi++;
        }

        /// <summary>
        /// Kasvatetaan kysymystaulukon kokoa luomalla uusi, viisi paikkaa suurempi aputaulukko
        /// johon vanhan taulukon tiedot kopioidaan.
        /// </summary>
        public void KasvataKokoa()
        {
           
            int i = 0;
            string[] aputaulukko = new string[kysymystaulukko.Length + 5];
            while (i < kysymystaulukko.Length)
            {
                aputaulukko[i] = kysymystaulukko[i];
                i++;
            }

            kysymystaulukko = aputaulukko;
        }

        /// <summary>
        /// Palauttaa taulukon alkion, joka sijaitsee indeksissä i
        /// </summary>
        /// <param name="i">Halutun alkion indeksi</param>
        /// <returns>i:nessä indeksissä oleva alkio</returns>
        public string Anna(int i)
        {
            return kysymystaulukko[i];
        }
    }
}
