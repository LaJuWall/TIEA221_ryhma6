using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;

namespace Testeri
{
    static class Program
    {
        public static Palikka blokki;
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            blokki = new Palikka();
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new VastausIkkuna());
        }

    }
}
