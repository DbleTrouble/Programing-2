using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog122b_Form
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
            listBox1.Items.Add("Hours\t\tRate of Pay");

            int H = int.Parse(textBox1.Text);
            double R = double.Parse(textBox2.Text);

            int lcv = 0;
            while (lcv <= H) 
            {
                double pay = (lcv * R);
                listBox1.Items.Add(lcv + "\t\t" + pay);
                lcv++;
            }
        }
    }
}
