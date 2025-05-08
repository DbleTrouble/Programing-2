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

namespace prog334_LoanCalculator_Form
{
    public partial class Form1 : Form
    {
        // Valid Months Ranges
        const int intMin_Months = 6;
        const int intMax_Months = 48;
        const float sngMonths_Year = 12.0f;

        // Annual Interest Rates for New and Used Cars
        const double dblNew_Rate = 0.089;
        const double dblUsed_Rate = 0.095;

        double dblAnnualRate = dblNew_Rate;
        public Form1()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            txtCost.CausesValidation = false;
            txtDownPayment.CausesValidation = false;
            txtMonths.CausesValidation = false;
            radNew.Checked = true;
            dblAnnualRate = dblNew_Rate;
            lblAnnInt.Text = dblNew_Rate.ToString(".00%");
            txtCost.Clear();
            txtDownPayment.Clear();
            txtMonths.Clear();
            lstOutput.Items.Clear();
            // Reset the focus
            txtCost.Focus();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            txtCost.CausesValidation = false;
            txtDownPayment.CausesValidation = false;
            txtMonths.CausesValidation = false;

            Application.Exit();
        }

        private void btnCalculate_Click(object sender, EventArgs e)
        {
            // Calculate and display the loan payment information
            int intCount = 0;
            int intMonths = 0;
            double dblLoan = 0.0;
            double dblPayment = 0.0;
            double dblInterest = 0.0;
            double dblPrincipal = 0.0;

            // Get the number of months and calculate the loan amount
            try
            {
                intMonths = int.Parse(txtMonths.Text);
                dblLoan = double.Parse(txtCost.Text) - double.Parse(txtDownPayment.Text);
            }
            catch (Exception ex)
            {
                MessageBox.Show("Please enter numeric values");
                return;
            }

            // Calculate the monthly
            dblPayment = Financial.Pmt(dblAnnualRate / sngMonths_Year, intMonths, -dblLoan);

            // Clear the list box
            lstOutput.Items.Clear();

            for (intCount = 1; intCount <= intMonths; intCount++)
            {
                // Holds the list box output
                string strOut = string.Empty;

                // Calculate the interest rate for the period
                dblInterest = Financial.IPmt(dblAnnualRate / sngMonths_Year, intCount, intMonths, -dblLoan);

                // Calculate and displat the principal for the period
                dblPrincipal = Financial.PPmt(dblAnnualRate / sngMonths_Year, intCount, intMonths, -dblLoan);

                // Add the month to the ouput string
                strOut += "Month: " + intCount;
                // Add the payment amount to the output string
                strOut += " Payment: " + dblPayment.ToString("$.00");
                // Add the interest amount to the output string
                strOut += " Interest: " + dblInterest.ToString("$.00");
                // Add the principal amount to the output string
                strOut += " Principal: " + dblPrincipal.ToString("$.00");

                // Add the output string to the list box
                lstOutput.Items.Add(strOut);
            }
        }

        private void radNew_CheckedChanged(object sender, EventArgs e)
        {
            // if the New radio button is checked, then the user has selected a new car loan.
            if (radNew.Checked == true)
            {
                dblAnnualRate = dblNew_Rate;
                lblAnnInt.Text = dblNew_Rate.ToString(".00%");
            }
        }

        private void radUsed_CheckedChanged(object sender, EventArgs e)
        {
            // User selected the Used Car radio button
            // Set the interest rate accordingly
            if (radUsed.Checked == true)
            {
                dblAnnualRate = dblUsed_Rate;
                lblAnnInt.Text = dblUsed_Rate.ToString(".00%");
            }
        }

        private void txtCost_Validating(object sender, CancelEventArgs e)
        {
            // Validates that a number has been entered int txtCost
            double _x = 0;
            if (!double.TryParse(txtCost.Text, out _x))
            {
                MessageBox.Show("Cost must be a number.", "Invalid Vehicle Cost");

                // Select the existing text in the text box.
                txtCost.SelectAll();
                //Set e.Cancel to true so the focus will stay in this control
                e.Cancel = true;
            }
            else
            {
                e.Cancel = false;
            }
        }

        private void txtDownPayment_Validating(object sender, CancelEventArgs e)
        {
            // Validates that a number has been entered int txtCost
            double _x = 0;
            if (!double.TryParse(txtCost.Text, out _x))
            {
                MessageBox.Show("Cost must be a number.", "Invalid Vehicle Cost");

                // Select the existing text in the text box.
                txtCost.SelectAll();
                //Set e.Cancel to true so the focus will stay in this control
                e.Cancel = true;
            }
            else
            {
                e.Cancel = false;
            }
        }

        private void txtMonths_Validating(object sender, CancelEventArgs e)
        {
            // Validates that a number has been entered int txtCost
            double _x = 0;
            if (!double.TryParse(txtCost.Text, out _x))
            {
                MessageBox.Show("Cost must be a number.", "Invalid Vehicle Cost");

                // Select the existing text in the text box.
                txtCost.SelectAll();
                //Set e.Cancel to true so the focus will stay in this control
                e.Cancel = true;
            }
            else
            {
                int intMonths = int.Parse(txtMonths.Text);

                if (intMonths < intMin_Months || intMonths > intMax_Months)
                {
                    MessageBox.Show("Months must be in the range " + intMin_Months + " - " + intMax_Months, "Error");

                    // Select the existing text in the text box
                    txtMonths.SelectAll();

                    // Set e.Cancel to true so the focus will stay in this control
                    e.Cancel = true;
                }
                else
                {
                    e.Cancel = false;
                }

            }
        }
    }
}

