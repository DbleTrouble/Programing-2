using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Microsoft.VisualBasic;

namespace prog498_Payroll_Form
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        const int intMax_Employees = 5;
        const decimal decHourly_Pay_Rate = 6.0m;

        private void btnCalcPay_Click(object sender, EventArgs e)
        {
            // Calc & Display Gross Pay Earned by Employees
            int[] intHours = new int[intMax_Employees]; // an array [0,0,0,0,0]
            // <type>[] varName = new <type>[capacity];
            int Count = 0;
            int EmpHours = 0;
            decimal EmpPay = 0.0m;

            for (Count = 0; Count < intMax_Employees; Count++)
            {
                while (int.TryParse(Interaction.InputBox("Enter number of hours worked by employee number" + (Count + 1).ToString(), "Need Hours Worked"), out EmpHours) == false)
                {
                    MessageBox.Show("Please enter an integer for hours worked");
                }
                intHours[Count] = EmpHours;
            }
            // Calculate and display each employee's gross pay.
            lstOutput.Items.Clear();
            for (Count = 0; Count < intMax_Employees; Count++) {
                EmpPay = intHours[Count] * decHourly_Pay_Rate; 
                lstOutput.Items.Add("Employee " + (Count + 1).ToString() + " earned " + EmpPay.ToString("$.00"));
            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
