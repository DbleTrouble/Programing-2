
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class PublicTicketSales(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(437, 105)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "How Many Tickets?"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._groupBox2.Controls.Add(self._radioButton3)
        self._groupBox2.Controls.Add(self._radioButton2)
        self._groupBox2.Controls.Add(self._radioButton1)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(13, 132)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(206, 193)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Section"
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(241, 132)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(209, 193)
        self._groupBox3.TabIndex = 1
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Total Cost"
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._radioButton1.Location = System.Drawing.Point(42, 42)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(122, 31)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Section A"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._radioButton2.Location = System.Drawing.Point(42, 90)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(122, 31)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Section B"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._radioButton3.Location = System.Drawing.Point(42, 141)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(122, 31)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Section C"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # PublicTicketSales
        # 
        self.ClientSize = System.Drawing.Size(462, 409)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox1)
        self.Name = "PublicTicketSales"
        self.Text = "PublicTicketSales"
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)

