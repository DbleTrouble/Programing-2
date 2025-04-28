using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace prog535_CatchMe_Form
{
    public partial class Form1 : Form
    {
        private string[] strCaption = {"Click here", "Try harder!", "Try again", "Not even close", "Where are you?", "I'm over here!", "Slow, aren't you?"};
        private Random rand = new Random();
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            MessageBox.Show("You got me!", "", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);
            Application.Exit();
        }

        private void button1_MouseEnter(object sender, EventArgs e)
        {
            int intIndex = rand.Next(strCaption.Length);
            button1.Text = strCaption[intIndex];

            button1.Left = rand.Next(this.Width - button1.Width);
            button1.Top = rand.Next(this.Height - button1.Height - 30);
        }
    }
}
