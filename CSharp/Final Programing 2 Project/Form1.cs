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
    public partial class Main : Form
    {

        Notesheet ns;
        public Main()
        {
            InitializeComponent(); 
            ns = new Notesheet(this);

        }

        public void GetSettings() 
        {
            // string project = Properties.Settings.Default.Name;
            MessageBox.Show(Properties.Settings.Default.NoteTitle);

           
        }
            
        private void button1_Click(object sender, EventArgs e)
        {
           
        }

        private void newproject_Click(object sender, EventArgs e)
        {
            ns.Show();
            this.Hide();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void loadproject_Click(object sender, EventArgs e)
        {
            GetSettings();
            ns.UpdateText(Properties.Settings.Default.NoteTitle,Properties.Settings.Default.NoteText);
            ns.Show();
        }
    }
}
