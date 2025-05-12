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

namespace prog514_SalesData_Form
{
    public partial class Form1 : Form
    {
        private bool GetSalesData(ref decimal[] decSales)
        {
            decimal[] decSalesData;
            int intNumDays = 0;
            int intCount;
            bool blnSuccess;

            string strNumDays = Interaction.InputBox("For how many days" + "do you have sales?");

            if (!int.TryParse(strNumDays, out intNumDays))
            {
                MessageBox.Show("You entered a non-numeric value", "Error");
            }
        }
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            
        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }
    }
}
