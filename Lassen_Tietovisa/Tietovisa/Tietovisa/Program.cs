using System;
using System.Windows.Forms;

namespace Tietovisa
{
    /// <summary>
    /// Tietovisa, yksinkertainen tietokilpailupeli. Ensin pelissä käytettävät kysymykset luetaan ohjelman
    /// käynnistys kansiosta olevasta kysymykset.txt tiedostosta. Tämän jälkeen pelaajalta kysytään nimimerkki
    /// ja haluttu pelin pituus. Aloitusikkuna piilotetaan, pelissä käytettävät kysymykset arvotaan ja avataan 
    /// pelin pääikkuna, jossa pelaaja vastaa arvottuihin kysymyksiin. Kun kaikki kysymykset on käyty läpi, pääikkuna
    /// piilotetaan ja avataan lopetusikkuna, jossa pelaajalle kerrotaan, kuinka moneen kysymykseen hän vastasi
    /// oikein. Halutessaan pelaaja voi lopetusikkunassa aloittaa pelin alusta (lopetusikkuna piilotetaan ja aloitusikkuna
    /// avataan uudestaan) tai sulkea ohjelman.
    /// </summary>
    static class Program
    {
        private static Aloitusikkuna Alotus;
        private static Paaikkuna Paa;
        private static Lopetusikkuna Loppu;
        /// <summary>
        /// Merkkijonotaulukko, mihin talletetaan kaikki käyttökelpoiset kysymysrivit, jotka on kysymykset.txt
        /// tiedostossa.
        /// </summary>
        private static Kysymykset KaikkiKysymykset;
        /// <summary>
        /// Merkkijonotaulukko, mihin tallennetaan yksittäisessä pelissä käytettävät kysymykset.
        /// </summary>
        private static string[] KaytettavatKysymykset;
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            KaikkiKysymykset = new Kysymykset();
            LueTiedostosta();
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(Alotus = new Aloitusikkuna(KaikkiKysymykset.seuraavaIndeksi));
        }

        /// <summary>
        /// Kun kilpailija valitsee aloitusikkunasta "Aloita", paaikkuna kutsuu tätä metodia aloittaakseen pelin.
        /// </summary>
        /// <param name="pituus">Kilpailijan valitsema pelin pituus</param>
        /// <param name="nimimerkki">Kilpailijan nimimerkki</param>
        public static void kaynnista(int pituus, string nimimerkki)
        {
            Alotus.Visible = false;
            KaytettavatKysymykset = new string[pituus];
            KaytettavatKysymykset = ArvoKysymykset(pituus);
            
            if (Paa == null)
            {
                Paa = new Paaikkuna();
                Paa.AloitaPeli(KaytettavatKysymykset, pituus, nimimerkki);
                Paa.Show();
                Alotus.Enabled = false;
                }
            else
            {
                Paa.AloitaPeli(KaytettavatKysymykset, pituus, nimimerkki);
                Paa.Visible = true;
                Paa.Enabled = true;
                Alotus.Enabled = false;
            }
        }

        /// <summary>
        /// Kun pelaaja on vastannut kaikkiin kysymyksiin, pääikkuna kutsuu komentoa avaamaan lopetusikkunan 
        /// </summary>
        /// <param name="pisteet">Kilpailijan pistemäärä</param>
        /// <param name="nimi">Kilpailijan nimimerkki</param>
        public static void lopeta(int pisteet, string nimi)
        {
            Paa.Visible = false;
            if (Loppu == null)
            {
                Loppu = new Lopetusikkuna();
                Loppu.Nayta_Lopetusikkuna(pisteet, nimi);
                Loppu.Show();
                Paa.Enabled = false;
            }
            else
            {
                Loppu.Nayta_Lopetusikkuna(pisteet, nimi);
                Loppu.Visible = true;
                Loppu.Enabled = true;
                Paa.Enabled = false;
            }
        }

        /// <summary>
        /// Piilotetaan ja otetaan pelin lopetusikkuna pois käytöstä ja palautetaan aloitusikkuna näkyviin.
        /// </summary>
        public static void alusta()
        {
            Loppu.Enabled = false;
            Loppu.Visible = false;
            Alotus.Visible = true;
            Alotus.Enabled = true;
        }

        /// <summary>
        /// Piilotetaan ja otetaan pelin pääikkuna pois käytöstä ja palautetaan aloitusikkuna näkyviin.
        /// </summary>
        public static void kesken_alusta()
        {
            Paa.Visible = false;
            Paa.Enabled = false;
            Alotus.Enabled = true;
            Alotus.Visible = true;
            
        }

        /// <summary>
        /// Luetaan kysymykset kysymykset.txt -tiedostosta ja sijoitetaan ne merkkijonotaulukkoon, mikäli tiedoston rivi ei ala
        /// '*' merkillä tai aiheuta virhettä, kun siitä yritetään muodostaa pelissä käytettävä kysymys olio. Mikäli kysymykset.txt
        /// tiedostoa ei löydy, ohjelma luo uuden kysymkset.txt tiedoston, jossa on ohjeet kysymysten kirjoittamiseen ja yksi esimerkki.
        /// </summary>
        public static void LueTiedostosta()
        {            
            int i = 0;
            Kysymys testi = new Kysymys();
            string line;
            string tiedostonOsoite = HaePolku();
            MessageBox.Show("Ohjelma avattiin kansiosta: " + tiedostonOsoite);
            try
            {
                System.IO.StreamReader file = new System.IO.StreamReader(tiedostonOsoite, System.Text.Encoding.Default, true);
                while ((line = file.ReadLine()) != null)
                {
                    string tarkistettava = line;
                    if (tarkistettava.Substring(0, 1) == "*")
                    {
                        i++;
                        continue;
                    }
                    try
                    {
                        testi.muodostaStringistä(tarkistettava);
                    }
                    catch (Exception)
                    {
                        i++;
                        continue;
                    }
                    KaikkiKysymykset.LisaaKysymys(tarkistettava);
                    i++;
                }
            }
            catch (Exception)
            {
                string[] oletusrivit = { "*Kysymykset on kirjoitettava muodossa: KYSYMYS|VAIHTOEHTO_A|VAIHTOEHTO_B|VAIHTOEHTO_C|VAIHTOEHTO_D|OIKEAN VASTAUKSEN KIRJAIN", 
                                         "*Esimerkiksi: Oletko sinä elossa?|Kyllä|En|Ehkä|En tiedä|A", 
                                         "Montako vastausvaihtoehtoa tässä kysymyksessä on?|1|2|3|4|D" };
                System.IO.File.WriteAllLines(tiedostonOsoite, oletusrivit, System.Text.Encoding.Default);
                MessageBox.Show("kysymykset.txt tiedostoa ei löytynyt. Ohjelma luo tiedoston, jossa on ohjeet kysymysten kirjoittamiseksi ja yksi esimerkkikysymys", "Tietovisa - Tiedostoa ei löytynyt!", MessageBoxButtons.OK, MessageBoxIcon.Error);
                Environment.Exit(0);
            }
        }        
        
        /// <summary>
        /// Arvotaan kaikista kysymyksistä pelissä käytettävät kysymykset, pyytämällä
        /// ArvoIndeksit metodilta kokonaislkukutaulukko, jonka osoittamista indekseistä
        /// haetaan pelissä käytettävät kysymykset.
        /// </summary>
        /// <param name="maara">kokonaisluku muuttuja, joka määrittää käytettävien kysymysten määrän.</param>
        /// <returns>merkkijono taulukko, jossa on pelissä käytettävät kysymykset.</returns>
        public static string[] ArvoKysymykset(int maara)
        {
            int[] luvut = ArvoIndeksit(maara);
            int i = 0;
            string[] palaute = new string[maara];

            while (i < maara)
            {
                palaute[i] = KaikkiKysymykset.Anna(luvut[i]);
                i++;
            }

            return palaute;
        }

        /// <summary>
        /// Arvotaan muuttujan maara verran kokonaislukuja väliltä 0 - kysymysten määrä. Taulukkoon ei
        /// tule samaa lukua kahdesti.
        /// </summary>
        /// <param name="maara">kokonaisluku, jonka suuruinen määrä lukuja arvotaan</param>
        /// <returns>kokonaisluku taulukko, johon on arvottu kokonaislukuja</returns>
        public static int[] ArvoIndeksit(int maara)
        {
            int i = 0;
            int k;
            int[] arvotut = new int[maara];
            Random arpoja = new Random();
            bool loytynyt;
            while (i < maara)
            {

                    int luku = arpoja.Next(KaikkiKysymykset.seuraavaIndeksi);
                
                    if (i == 0)
                    {
                            arvotut[i] = luku;
                            i++;
                    }
                    else
                    {
                            loytynyt = false;
                            k = 0;

                    while (k < i)
                    {
                            if (luku == arvotut[k]) loytynyt = true;
                            k++;
                    }

                    if (loytynyt == false)
                    {
                        arvotut[i] = luku;
                        i++;
                    }
                }
            }
            return arvotut;
        }

        /// <summary>
        /// Tutkitaan, mistä sijainnista ohjelma on käynnistetty, ja palautetaan tieto merkkijonona.
        /// </summary>
        /// <returns>polku, josta ohjelma on käynnistetty</returns>
        public static string HaePolku()
        {
            string polku;
            polku = Environment.CurrentDirectory;
            polku = polku + "\\kysymykset.txt";
            return polku;
        }

    }
}
