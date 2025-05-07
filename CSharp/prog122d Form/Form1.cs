using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog122d_Form
{
    public partial class Form1 : Form
    {
        static double f(double x) { return (double)Math.Pow(x, 6) - (3 * Math.Pow(x, 5)) - (93 * Math.Pow(x, 4)) + (87 * Math.Pow(x, 3)) + (1596 * Math.Pow(x, 2)) - (1380 * x) - 2800; 
        }

        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            listBox1.Items.Clear();
            listBox1.Items.Add("x\t\ty");
            for (int x = -12; x <= 16; x++) {
                double y = (int)f(x);
                listBox1.Items.Add(x + "\t\t" + y);
            }
        }
    }
}
