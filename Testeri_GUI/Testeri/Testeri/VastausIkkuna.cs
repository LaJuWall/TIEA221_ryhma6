using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace Testeri
{
    public partial class VastausIkkuna : Form
    {
        
        public VastausIkkuna()
        {
            InitializeComponent();
        }

        private void A_Nappi_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Klikkasit aata", "Testeri", MessageBoxButtons.OK);
            KysymysLabel.Text = Program.blokki.AnnaKysymys();
        }

        private void B_nappi_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Klikkasit beetä", "Testeri", MessageBoxButtons.OK);
            KysymysLabel.Text = Program.blokki.AnnaKysymys();
        }

        private void C_Nappi_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Klikkasit ceetä", "Testeri", MessageBoxButtons.OK);
            KysymysLabel.Text = Program.blokki.AnnaKysymys();
        }

        private void D_Nappi_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Klikkasit deetä", "Testeri", MessageBoxButtons.OK);
            KysymysLabel.Text = Program.blokki.AnnaKysymys();
        }

    }
}
