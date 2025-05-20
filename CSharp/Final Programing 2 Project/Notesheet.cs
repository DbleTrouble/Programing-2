using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Final_Programing_2_Project
{
    public partial class Notesheet : Form
    {
        public Notesheet()
        {
            InitializeComponent();
        }

        private void toolStripLabel1_Click(object sender, EventArgs e)
        {
            
            SaveSetting();
        }

        private void toolStripLabel2_Click(object sender, EventArgs e)
        {
            Main main = new Main();
            main.Show();
            this.Close();
        }

        
        public void SaveSetting() 
        {
            Properties.Settings.Default.Name = txtTitle.Text;

            Properties.Settings.Default.Save();
            
            MessageBox.Show(Properties.Settings.Default.Name);
        }

        private void redToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Red;
        }

        private void yellowToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Yellow;
        }

        private void blueToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Blue;
        }

        private void greenToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Green;
        }

        private void orangeToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Orange;
        }

        private void purpleToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Purple;
        }

        private void blackToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.Black;
        }

        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Red;
        }

    }
}
