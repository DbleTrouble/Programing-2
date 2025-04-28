using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog310a_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Random rand = new Random(); // python: rand = Random()

            // int lcv = 0; while (lcv < ...) { ...; lcv++;}
            for (int lcv = 0; lcv < rand.Next(5, 11); lcv++)
            {
                double freq = rand.Next(0, 21) + rand.NextDouble();
                string msg = "";
                int stars = (int)Math.Round(freq);
                for (int i = 0; i < stars; i++)
                    msg += "*";
                msg += " " + Math.Round(freq, 2);
                listBox1.Items.Add(msg);
            }
        }
    }
}
