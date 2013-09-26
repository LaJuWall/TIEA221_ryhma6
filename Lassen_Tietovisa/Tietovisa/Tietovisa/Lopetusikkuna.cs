using System;
using System.Windows.Forms;

namespace Tietovisa
{
    /// <summary>
    /// Pelin lopetusikkuna, jossa pelaaja näkee saamansa pistemäärän ja voi halutessaan aloittaa uuden pelin tai sulkea ohjelman.
    /// </summary>
    public partial class Lopetusikkuna : Form
    {
        /// <summary>
        /// Parametritön muodostaja.
        /// </summary>
        public Lopetusikkuna()
        {
            InitializeComponent();
        }

        /// <summary>
        /// Parametrillinen muodostaja.
        /// </summary>
        /// <param name="pisteet">Kilpailijan pelin aikana saadut pisteet</param>
        /// <param name="nimi">Kilpailijan nimimerkki</param>
        public void Nayta_Lopetusikkuna(int pisteet, string nimi)
        {
            Otsikko_Label.Text = "Peli on päättynyt, " + nimi + "!";
            if (nimi == "")
            {
                Otsikko_Label.Text = "Peli on päättynyt!";
            }
            Tulos_label.Text = "Vastasit oikein " + pisteet + " kysymykseen!";
        }

        /// <summary>
        /// "Sulje" nappia painamalla, koko ohjelma suljetaan
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Sulje_Nappi_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        /// <summary>
        /// "Alusta" nappia painamalla kutsutaan Program luokassa olevaa "alusta" metodia, jolla peli aloitetaan alusta.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Alusta_Nappi_Click(object sender, EventArgs e)
        {
            Program.alusta();
        }

        /// <summary>
        /// Ikkunan sulkeutuessa, koko ohjelma lopetetaan.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Lopetusikkuna_FormClosed(object sender, FormClosedEventArgs e)
        {
            Application.Exit();
        }

    }
}
