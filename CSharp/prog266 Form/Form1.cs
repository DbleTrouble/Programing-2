using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog266_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
            double num1 = double.Parse(textBox1.Text);
            double num2 = double.Parse(textBox2.Text);

            if (num1 > num2)
            {
                label1.Text = "Number 1 is greater than Number 2";
            }
            else if (num1 == num2)
            {
                label1.Text = "Number 1 = Number 2";
            }
            else
            {
                label1.Text = "Number 2 is greater than Number 1";
            }
        }
    }
}
