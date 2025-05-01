using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog435_TicketSales_Form
{
    public partial class GeneralSales : Form
    {
        public GeneralSales()
        {
            InitializeComponent();
        }

        private void radioButton1_CheckedChanged(object sender, EventArgs e)
        {
            int T = int.Parse(textBox1.Text);
            double TT = T * 20;
            double TA = TT * .06;
            double TC = TT + TA;
            label5.Text = "$" + TT;
            label6.Text = "$" + TA;
            label7.Text = "$" + TC;
        }

        private void radioButton2_CheckedChanged(object sender, EventArgs e)
        {
            int T = int.Parse(textBox1.Text);
            double TT = T * 15;
            double TA = TT * .06;
            double TC = TT + TA;
            label5.Text = "$" + TT;
            label6.Text = "$" + TA;
            label7.Text = "$" + TC;
        }

        private void radioButton3_CheckedChanged(object sender, EventArgs e)
        {
            int T = int.Parse(textBox1.Text);
            double TT = T * 10;
            double TA = TT * .06;
            double TC = TT + TA;
            label5.Text = "$" + TT;
            label6.Text = "$" + TA;
            label7.Text = "$" + TC;
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Form1 origin = new Form1();
            origin.Show();
            this.Close();

        }
    }
}
