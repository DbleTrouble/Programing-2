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
        private string currentNotePath = null;

        Notesheet ns;
        public Main()
        {
            InitializeComponent(); 
            ns = new Notesheet(this);
        }

        private void NewNote()
        {
            textBox1.Clear();
            currentNotePath = null;
            
        }

        private void newproject_Click(object sender, EventArgs e)
        {
            NewNote();
            ns.Show();
            this.Hide();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void loadproject_Click(object sender, EventArgs e)
        {
            ns.UpdateText(Properties.Settings.Default.NoteTitle,Properties.Settings.Default.NoteText);
            ns.Show();
        }
    }
}
