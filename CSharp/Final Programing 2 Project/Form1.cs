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
            
            //ns.UpdateText(Properties.Settings.Default.NoteTitle[0],Properties.Settings.Default.NoteText[0]);
            //ns.Show();
        }

        private void loadToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                foreach (string title in Properties.Settings.Default.NoteTitle)
                {
                    toolStripComboBox1.Items.Add(title);
                }
            }
            catch (Exception) { }
        }

        private void toolStripComboBox1_Click(object sender, EventArgs e)
        {
            int index = toolStripComboBox1.SelectedIndex;
            ns.UpdateText(Properties.Settings.Default.NoteTitle[index], Properties.Settings.Default.NoteText[index]);
            ns.Show();
        }
    }
}
