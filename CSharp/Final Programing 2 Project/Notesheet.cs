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
    public partial class Notesheet : Form
    {
        Form myparent;
        
        public Notesheet(Form myparent)
        {
            this.myparent = myparent;
            InitializeComponent();
        }

        public void SaveSetting()
        {
            try
            {
                var titles = Properties.Settings.Default.NoteTitle ?? new System.Collections.Specialized.StringCollection();
                var texts = Properties.Settings.Default.NoteText ?? new System.Collections.Specialized.StringCollection();
                var backColors = Properties.Settings.Default.NoteBackColors ?? new System.Collections.Specialized.StringCollection();
                var foreColors = Properties.Settings.Default.NoteForeColors ?? new System.Collections.Specialized.StringCollection();
                var fonts = Properties.Settings.Default.NoteFonts ?? new System.Collections.Specialized.StringCollection();

                string title = txtTitle.Text;
                string content = textBox1.Text;

                if (!string.IsNullOrWhiteSpace(title) && !string.IsNullOrWhiteSpace(content))
                {
                    int existingIndex = titles.IndexOf(title);
                    var fontConverter = new FontConverter();

                    string backColorString = ColorTranslator.ToHtml(textBox1.BackColor);
                    string foreColorString = ColorTranslator.ToHtml(textBox1.ForeColor);
                    string fontString = fontConverter.ConvertToString(textBox1.Font);

                    if (existingIndex >= 0 &&
                        existingIndex < texts.Count &&
                        existingIndex < backColors.Count &&
                        existingIndex < foreColors.Count &&
                        existingIndex < fonts.Count)
                    {
                        // Overwrite existing
                        texts[existingIndex] = content;
                        backColors[existingIndex] = backColorString;
                        foreColors[existingIndex] = foreColorString;
                        fonts[existingIndex] = fontString;
                    }
                    else
                    {
                        // Add new
                        titles.Add(title);
                        texts.Add(content);
                        backColors.Add(backColorString);
                        foreColors.Add(foreColorString);
                        fonts.Add(fontString);
                    }

                    Properties.Settings.Default.NoteTitle = titles;
                    Properties.Settings.Default.NoteText = texts;
                    Properties.Settings.Default.NoteBackColors = backColors;
                    Properties.Settings.Default.NoteForeColors = foreColors;
                    Properties.Settings.Default.NoteFonts = fonts;

                    Properties.Settings.Default.Save();
                    MessageBox.Show("Your Note Sheet has been saved");
                }
                else
                {
                    MessageBox.Show("Title and content must not be empty.", "Validation Error", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                }
            }
            catch (ConfigurationErrorsException ex)
            {
                MessageBox.Show(string.Format("Settings file is corrupted: {0}", ex.Message));
                ResetUserSettings();
            }
        }


        public void ResetUserSettings()
        {
            try
            {
                // Access setting to trigger exception and get file path
                var titles = Properties.Settings.Default.NoteTitle;
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

                // Optionally clear your UI controls after reset
                txtTitle.Text = string.Empty;
                textBox1.Text = string.Empty;
            }
            catch (Exception ex)
            {
                MessageBox.Show(string.Format("Settings file is corrupted: {0}", ex.Message));
            }
        }

        public void ClearNote()
        {
            if (txtTitle == null || textBox1 == null)
            {
                MessageBox.Show("Form controls not initialized properly.", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            txtTitle.Text = "Untitled Notesheet";
            textBox1.Text = "";
            textBox1.ForeColor = Color.Black;
            textBox1.BackColor = Color.White;
            textBox1.Font = new Font("Microsoft Sans Serif", 8, textBox1.Font.Style);
        }

        public void toolStripLabel1_Click(object sender, EventArgs e)
        {
            SaveSetting();
        }

        public void toolStripLabel2_Click(object sender, EventArgs e)
        {
            myparent.Show();
            this.Hide();
        }
        
        public void UpdateText(string title, string text, string backColorString = null, string foreColorString = null, string fontString = null)
        {
            txtTitle.Text = title;
            textBox1.Text = text;

            if (!string.IsNullOrEmpty(backColorString))
                textBox1.BackColor = ColorTranslator.FromHtml(backColorString);

            if (!string.IsNullOrEmpty(foreColorString))
                textBox1.ForeColor = ColorTranslator.FromHtml(foreColorString);

            if (!string.IsNullOrEmpty(fontString))
            {
                var fontConverter = new FontConverter();
                try
                {
                    Font font = (Font)fontConverter.ConvertFromString(fontString);
                    textBox1.Font = font;
                }
                catch
                {
                    // Fallback to default font if conversion fails
                }
            }
        }

        // Text Color
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
        private void whiteToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.ForeColor = Color.White;
        }
        // Background Color
        private void toolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Red;
        }
        private void toolStripMenuItem8_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Yellow;
        }
        private void blueToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Blue;
        }
        private void greenToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Green;
        }
        private void orangeToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Orange;
        }
        private void purpleToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Purple;
        }
        private void blackToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.Black;
        }
        private void whiteToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.BackColor = Color.White;
        }
        // Fonts
        // Agency FB
        private void agencyFBToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Agency FB", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem10_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Agency FB", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem11_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Agency FB", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem12_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Agency FB", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem13_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Agency FB", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem14_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Agency FB", 18, textBox1.Font.Style);
        }
        // Algerian
        private void algerianToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Algerian", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem15_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Algerian", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem16_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Algerian", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem17_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Algerian", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem18_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Algerian", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem19_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Algerian", 18, textBox1.Font.Style);
        }
        // Arial
        private void arialToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Arial", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem20_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Arial", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem21_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Arial", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem22_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Arial", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem23_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Arial", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem24_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Arial", 18, textBox1.Font.Style);
        }
        // Baskerville Old Face
        private void baskervilleOldFaceToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Baskerville Old Face", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem25_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Baskerville Old Face", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem26_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Baskerville Old Face", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem27_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Baskerville Old Face", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem28_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Baskerville Old Face", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem29_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Baskerville Old Face", 18, textBox1.Font.Style);
        }
        // Blackadder ITC
        private void blackadderITCToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Blackadder ITC", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem30_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Blackadder ITC", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem31_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Blackadder ITC", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem32_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Blackadder ITC", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem33_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Blackadder ITC", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem34_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Blackadder ITC", 18, textBox1.Font.Style);
        }
        // Calibri
        private void calibriToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Calibri", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem35_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Calibri", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem36_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Calibri", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem37_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Calibri", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem38_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Calibri", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem39_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Calibri", 18, textBox1.Font.Style);
        }
        // Castellar
        private void castellarToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Castellar", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem40_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Castellar", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem41_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Castellar", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem42_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Castellar", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem43_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Castellar", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem44_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Castellar", 18, textBox1.Font.Style);
        }
        // Edwardian Script ITC
        private void edwardianScriptITCToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Edwardian Script ITC", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem45_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Edwardian Script ITC", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem46_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Edwardian Script ITC", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem47_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Edwardian Script ITC", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem48_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Edwardian Script ITC", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem49_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Edwardian Script ITC", 18, textBox1.Font.Style);
        }
        // Microsoft Sans Serif
        private void microsoftSansSerifToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Microsoft Sans Serif", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem3_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Microsoft Sans Serif", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem4_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Microsoft Sans Serif", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem5_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Microsoft Sans Serif", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem6_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Microsoft Sans Serif", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem7_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Microsoft Sans Serif", 18, textBox1.Font.Style);
        }
        // Old English Text MT
        private void oldEnglishTextMTToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Old English Text MT", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem50_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Old English Text MT", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem51_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Old English Text MT", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem52_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Old English Text MT", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem53_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Old English Text MT", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem54_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Old English Text MT", 18, textBox1.Font.Style);
        }
        // Times New Roman
        private void timesNewRomanToolStripMenuItem_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Times New Roman", 8, textBox1.Font.Style);
        }
        private void toolStripMenuItem55_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Times New Roman", 10, textBox1.Font.Style);
        }
        private void toolStripMenuItem56_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Times New Roman", 12, textBox1.Font.Style);
        }
        private void toolStripMenuItem57_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Times New Roman", 14, textBox1.Font.Style);
        }
        private void toolStripMenuItem58_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Times New Roman", 16, textBox1.Font.Style);
        }
        private void toolStripMenuItem59_Click(object sender, EventArgs e)
        {
            textBox1.Font = new Font("Times New Roman", 18, textBox1.Font.Style);
        }
    }
}
