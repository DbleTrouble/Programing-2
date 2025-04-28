using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog122a_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("Number\t\tSquare\t\tSquare Root");
            int lcv = 1;
            while (lcv <= 50) {
                int sqr = (int)Math.Pow(lcv, 2);
                double sqrt = Math.Sqrt(lcv);
                //listBox1.Items.Add(lcv + "\t\t" + sqr + "\t\t" + Math.Round(sqrt, 4));
                //listBox1.Items.Add($"{lcv}\t\t{sqr}\t\t{MMath.Round(sqrt, 4)}"); // f-string
                listBox1.Items.Add(string.Format("{0}\t\t{1}\t\t{2}", lcv, sqr, Math.Round(sqrt, 4))); // also f-string
                lcv++; // lcv += 1
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
        }
    }
}
