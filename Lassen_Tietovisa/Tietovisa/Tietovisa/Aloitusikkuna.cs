using System;
using System.Windows.Forms;

namespace Tietovisa
{
    /// <summary>
    /// Pelin aloitusikkuna, jossa pelaaja syöttää nimimerkkinsä ja haluamansa pelin pituuden.
    /// </summary>
    public partial class Aloitusikkuna : Form
    {
        /// <summary>
        /// Parametritön muodostaja.
        /// </summary>
        public Aloitusikkuna()
        {
            InitializeComponent();
        }

        /// <summary>
        /// Muodostaja, joka ottaa parametrikseen kokonaisluvun, joka sijoitetaan sliderin maksimiarvoksi. Mikäli
        /// kokonaisluku on 0, ilmoitetaan käyttäjälle, ettei kysymyksiä ole käytettävissä.
        /// </summary>
        /// <param name="maara">kokonaisluku, joka halutaan sliderin maksimiksi</param>
        public Aloitusikkuna(int maara)
        {
            InitializeComponent();
            Valitsin.Maximum = maara;
            if (maara == 0) EiKysymyksiä();
        }

       /// <summary>
       /// Mitä tapahtuu, kun käyttäjä klikkaa "Aloita" nappulaa
       /// </summary>
       /// <param name="sender"></param>
       /// <param name="e"></param>
        private void Aloitus_Nappi_Click(object sender, EventArgs e)
        {
            Program.kaynnista(Valitsin.Value, nimi_boxi.Text);
        }

        /// <summary>
        /// Käyttäjän muuttaessa sliderin arvoa, sen alapuolella olevan labelin teksti muuttuu.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void trackBar1_ValueChanged(object sender, EventArgs e)
        {
            Montako_Label.Text = "Kysymysten määrä: " + Valitsin.Value;
        }

        /// <summary>
        /// Näytetään virheilmoitus, jossa kerrotaan ettei Kysymykset.txt tiedostossa ole käyttökelpoisia kysymyksiä, ja ohjelma
        /// lopetetaan.
        /// </summary>
        public static void EiKysymyksiä()
        {
            MessageBox.Show("Kysmykset.txt tiedostossa ei ollut yhtäkään oikein kirjoitettua kysymystä. Ole hyvä ja korjaa kysymysten muoto esimerkin mukaiseksi ja käynnistä Tietovisa uudelleen.", "Tietovisa", MessageBoxButtons.OK ,MessageBoxIcon.Error);
            Environment.Exit(0);
        }
    }
}
