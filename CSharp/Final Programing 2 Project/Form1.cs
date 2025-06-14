﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Collections.Specialized;
using System.Configuration;
using System.IO;

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

        private void NewNote()
        {
            ns.ClearNote();  // We'll create this method in Notesheet form
            ns.Show();
            this.Hide();
        }

        private void newproject_Click(object sender, EventArgs e)
        {
            NewNote();
        }

        private void exitToolStripMenuItem_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void ResetUserSettings()
        {
            try
            {
                var dummy = Properties.Settings.Default.NoteTitle;
            }
            catch (ConfigurationErrorsException ex)
            {
                string configPath = ex.Filename;
                if (File.Exists(configPath))
                {
                    File.Delete(configPath);
                }
                Properties.Settings.Default.Reset();
                Properties.Settings.Default.Save();

                MessageBox.Show("Settings were reset due to corruption.");
            }
        }


        private void loadToolStripMenuItem_Click(object sender, EventArgs e)
        {
            try
            {
                var titles = Properties.Settings.Default.NoteTitle;
                if (titles != null && titles.Count > 0)
                {
                    toolStripComboBox1.Items.Clear();
                    foreach (string title in titles)
                    {
                        toolStripComboBox1.Items.Add(title);
                    }
                }
            }
            catch (ConfigurationErrorsException ex)
            {
                MessageBox.Show(string.Format("Settings file is corrupted: {0}", ex.Message));
                ResetUserSettings();

                // Optionally clear combo box after resetting
                toolStripComboBox1.Items.Clear();
            }
        }

        private void toolStripComboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            int index = toolStripComboBox1.SelectedIndex;

            try
            {
                var titles = Properties.Settings.Default.NoteTitle;
                var texts = Properties.Settings.Default.NoteText;

                if (index >= 0 && titles != null && texts != null &&
                    index < titles.Count && index < texts.Count)
                {
                    ns.UpdateText(titles[index], texts[index]);
                    ns.Show();
                }
                else
                {
                    MessageBox.Show("Invalid note selection.", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch (ConfigurationErrorsException ex)
            {
                MessageBox.Show(string.Format("Settings file is corrupted: {0}", ex.Message));
                ResetUserSettings();
                toolStripComboBox1.Items.Clear();
            }
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            int index = toolStripComboBox1.SelectedIndex;
            var titles = Properties.Settings.Default.NoteTitle;
            var texts = Properties.Settings.Default.NoteText;
            var backColors = Properties.Settings.Default.NoteBackColors;
            var foreColors = Properties.Settings.Default.NoteForeColors;
            var fonts = Properties.Settings.Default.NoteFonts;

            if (index >= 0 && titles != null && texts != null &&
                backColors != null && foreColors != null && fonts != null &&
                index < titles.Count && index < texts.Count &&
                index < backColors.Count && index < foreColors.Count && index < fonts.Count)
            {
                ns.UpdateText(
                    titles[index], texts[index],
                    backColors[index], foreColors[index], fonts[index]);
                ns.Show();
            }
            else
            {
                MessageBox.Show("Invalid note selection.", "Warning", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }

        public void DeleteAllNotes()
        {
            var result = MessageBox.Show("Are you sure you want to delete all saved notes?",
                                 "Confirm Deletion",
                                 MessageBoxButtons.YesNo,
                                 MessageBoxIcon.Warning);

            if (result == DialogResult.Yes)
            {
                // Clear saved data
                Properties.Settings.Default.NoteTitle = new System.Collections.Specialized.StringCollection();
                Properties.Settings.Default.NoteText = new System.Collections.Specialized.StringCollection();
                Properties.Settings.Default.Save();

                // Clear combo box
                toolStripComboBox1.Items.Clear();

                MessageBox.Show("All notes have been deleted.", "Success", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }

        private void deleteAllNotesToolStripMenuItem_Click(object sender, EventArgs e)
        {
            DeleteAllNotes();
        }

        /*private void loadToolStripMenuItem_Click(object sender, EventArgs e)
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
         */
    }
}
