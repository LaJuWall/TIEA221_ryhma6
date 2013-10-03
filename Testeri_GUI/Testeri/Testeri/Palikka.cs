using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Testeri
{
    class Palikka
    {

        public static string[] kysymystaulukko;
        public static Random Arpoja;

        public string AnnaKysymys()
        {
            int numero = Arpoja.Next(0, 5);
            return kysymystaulukko[numero];
        }
        
        public Palikka()
        {
            kysymystaulukko = new string[5];
            kysymystaulukko[0] = "Olenko minä peli?";
            kysymystaulukko[1] = "Oletko sinä peli?";
            kysymystaulukko[2] = "Onko 1+1=3 totta?";
            kysymystaulukko[3] = "Anata no namae wa Lasse-san desuka?";
            kysymystaulukko[4] = "KikkelisKokkelis?";
            Arpoja = new Random();

        }

        
    
    }
}
