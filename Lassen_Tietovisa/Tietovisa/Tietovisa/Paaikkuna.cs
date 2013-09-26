using System;
using System.Windows.Forms;

namespace Tietovisa
{
    /// <summary>
    /// Pelin pääikkuna. Kysymyksiin vastaaminen tapahtuu ruudussa olevia nappeja painamalla.
    /// Pääikkunasta pelaaja voi avata myös valikkoja, joista hän voi aloittaa pelin alusta, 
    /// sulkea ohjelman, katsoa pelin tiedot tai lukea ohjeistuksen.
    /// </summary>
    public partial class Paaikkuna : Form
    {
        
        private Tietoikkuna InfoIkkuna;
        private Ohjeistus Ohjeikkuna;
        /// <summary>
        /// kokonaisluku, joka määrittää pelin pituuden.
        /// </summary>
        private int pituus;
        /// <summary>
        /// merkkijonotaulukko, jossa on pelissä käytettävät kysymykset.
        /// </summary>
        private string[] kysymykset;
        /// <summary>
        /// Kilpailija muuttuja pelaajan tietoja varten.
        /// </summary>
        private Kilpailija pelaaja;
        /// <summary>
        /// Kysymys muuttuja, joka tietää yhden kysymyksen tiedot.
        /// </summary>
        private Kysymys kysymysNyt;
        /// <summary>
        /// kokonaislukumuuttuja, jolla ylläpidetään tietoa vastattujen kysymysten määrästä.
        /// </summary>
        private int laskuri;
        
        /// <summary>
        /// Parametritön muodostaja.
        /// </summary>
        public Paaikkuna()
        {
            InitializeComponent();
        }

        /// <summary>
        /// Aloitetaan komponenttiin uusi peli parametreinä annettujen tietojen pohjalta.
        /// </summary>
        /// <param name="lista">merkkijonotaulukko, jossa on pelissä käytettävät kysymykset</param>
        /// <param name="pelinPituus">pelin pituus(kysymysten määrä) kokonaislukumuuttujana</param>
        /// <param name="nimimerkki">pelaajalle haluttu nimimerkki</param>
        public void AloitaPeli(string[] lista, int pelinPituus, string nimimerkki)
        {
            this.Text = "Tietovisa - " + nimimerkki;
            kysymykset = lista;
            pituus = pelinPituus;
            pelaaja = new Kilpailija(nimimerkki, 0);
            kysymysNyt = new Kysymys();
            laskuri = 0;
            Vaihe_Bar.Maximum = pituus;
            MuodostaKysymys();
        }

        /// <summary>
        /// Kutsutaan Program luokassa olevaa Nayta_Loppu metodia.
        /// </summary>
        private void Nayta_Loppu()
        {
            Program.lopeta(pelaaja.Pisteet, pelaaja.Nimimerkki);
        }

        /// <summary>
        /// Kun käyttäjä painaa A nappulaa, tarkastetaan onko vastaus A oikein ja lisätään tarvittaessa kilpailijalle piste.
        /// Tämän jälkeen muodosstetaan seuraava kysymys.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void A_Nappi_Click(object sender, EventArgs e)
        {
            if (kysymysNyt.TarkistaVastaus("A"))
            {
                pelaaja.lisaaPiste();
                MuodostaKysymys();
            }
            else MuodostaKysymys();
        }

        /// <summary>
        /// Kun käyttäjä painaa B nappulaa, tarkastetaan onko vastaus B oikein ja lisätään tarvittaessa kilpailijalle piste.
        /// Tämän jälkeen muodosstetaan seuraava kysymys.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void B_nappi_Click(object sender, EventArgs e)
        {
            if (kysymysNyt.TarkistaVastaus("B"))
            {
                pelaaja.lisaaPiste();
                MuodostaKysymys();
            }
            else MuodostaKysymys();
        }

        /// <summary>
        /// Kun käyttäjä painaa C nappulaa, tarkastetaan onko vastaus C oikein ja lisätään tarvittaessa kilpailijalle piste.
        /// Tämän jälkeen muodosstetaan seuraava kysymys.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void C_nappi_Click(object sender, EventArgs e)
        {
            if (kysymysNyt.TarkistaVastaus("C"))
            {
                pelaaja.lisaaPiste();
                MuodostaKysymys();
            }
            else MuodostaKysymys();
        }

        /// <summary>
        /// Kun käyttäjä painaa D nappulaa, tarkastetaan onko vastaus D oikein ja lisätään tarvittaessa kilpailijalle piste.
        /// Tämän jälkeen muodosstetaan seuraava kysymys.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void D_Nappi_Click(object sender, EventArgs e)
        {
            if (kysymysNyt.TarkistaVastaus("D"))
            {
                pelaaja.lisaaPiste();
                MuodostaKysymys();
            }
            else MuodostaKysymys();
        }

        /// <summary>
        /// Valikossa olevasta "Aloita alusta" -vaihtoehdosta klikkaamalla peli aloitetaan alusta ja käyttäjä palautetaan aloitusikkunaan.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void aloitaAlustaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Tahdotko varmasti aloittaa alusta?", "Tietovisa", MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            switch (result)
            {
                case DialogResult.OK:
                    Program.kesken_alusta();
                    break;

                case DialogResult.Cancel:
                    break;
            }

        }

        /// <summary>
        /// Valikossa olevasta "Sulje" -vaihtoehdosta klikkaamalla koko ohjelma sulkeutuu
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void suljeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Tahdotko varmasti sulkea Tietovisan?", "Tietovisa", MessageBoxButtons.OKCancel, MessageBoxIcon.Question);
            switch (result)
            {
                case DialogResult.OK:
                    Application.Exit();
                    break;

                case DialogResult.Cancel:
                    break;
            }

        }

        /// <summary>
        /// Valikossa olevasta "Näytä ohje" -vaihtoehdosta klikkaamalla avataan uusi ikkuna, jossa on ohjelman ohjeistus.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void näytäOhjeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Ohjeikkuna = new Ohjeistus();
            Ohjeikkuna.ShowDialog();
        }

        /// <summary>
        /// Valikossa olevasta "Tietoja Tietovisasta" vaihtoehdosta klikkaamalla avataan uusi ikkuna, jossa on ohjelman perustiedot.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void tietojaTietovisastaToolStripMenuItem_Click(object sender, EventArgs e)
        {
            InfoIkkuna = new Tietoikkuna();
            InfoIkkuna.ShowDialog();
        }

        /// <summary>
        /// Muodostetaan kysymys ikkunaan, mikäli laskurin arvo on pinenmpi tai yhtäsuuri kuin pituus. Muussa
        /// tapauksessa peli lopetetaan.
        /// </summary>
        private void MuodostaKysymys()
        {
            if (laskuri >= pituus) Nayta_Loppu();
            else
            {
                kysymysNyt.muodostaStringistä(kysymykset[laskuri]);
                Kysymys_Label.Text = kysymysNyt.itsekysymys;
                A_Label.Text = kysymysNyt.vaihtoehtoA;
                B_Label.Text = kysymysNyt.vaihtoehtoB;
                C_Label.Text = kysymysNyt.vaihtoehtoC;
                D_Label.Text = kysymysNyt.vaihtoehtoD;
                Vaihe_Bar.Value = laskuri;
                laskuri++;
                Vaihe_Label.Text = laskuri + "/" + pituus;
            }
            
        }

        /// <summary>
        /// Kun ikkuna suljetaan, koko ohjelman suoritus lopetetaan.
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void Paaikkuna_FormClosed(object sender, FormClosedEventArgs e)
        {
            Application.Exit();
        }

    }
}