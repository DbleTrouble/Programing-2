﻿using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace prog347_Sum_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int num = int.Parse(Interaction.InputBox("Enter a positive integer value.", "Input Needed"));
            int sum = 0;
            for (int lcv = 0; lcv < num; lcv++)
            {
                sum += lcv + 1;
            }
            MessageBox.Show("The sum of the numbers 1 through " + num +" is " + sum, "Sum of Numbers");
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
