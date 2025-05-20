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

    }
}
