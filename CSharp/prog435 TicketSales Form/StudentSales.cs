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
    public partial class StudentSales : Form
    {
        public StudentSales()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int T = int.Parse(textBox1.Text);
            double TT = T * 7;
            double TA = TT * .06;
            double TC = TT + TA;
            label6.Text = "$" + TT;
            label7.Text = "$" + TA;
            label8.Text = "$" + TC;
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Form1 origin = new Form1();
            origin.Show();
            this.Close();
        }
    }
}
