using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog273_MassAndWeight_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            double mass = double.Parse(textBox1.Text);
            double weight = mass * 9.8;
            if (weight >= 1000)
            {
                MessageBox.Show("The Object Is Too Heavy!");
            }
            else if (weight <= 10)
            {
                MessageBox.Show("The Object Is Too Light!");
            }
            label3.Text = weight.ToString();
        }
    }
}
