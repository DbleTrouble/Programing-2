
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class StudentTicketSales(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label7 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(262, 193)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "How Many Tickets?"
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label1.Location = System.Drawing.Point(6, 43)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(141, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Number of tickets:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label2.Location = System.Drawing.Point(6, 108)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(250, 60)
        self._label2.TabIndex = 1
        self._label2.Text = "Student tickets are for seating in the student section only."
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(153, 41)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 26)
        self._textBox1.TabIndex = 2
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._groupBox3.Controls.Add(self._label7)
        self._groupBox3.Controls.Add(self._label6)
        self._groupBox3.Controls.Add(self._label8)
        self._groupBox3.Controls.Add(self._label4)
        self._groupBox3.Controls.Add(self._label3)
        self._groupBox3.Controls.Add(self._label5)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(304, 13)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(206, 193)
        self._groupBox3.TabIndex = 2
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Total Cost"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label4.Location = System.Drawing.Point(6, 145)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(98, 23)
        self._label4.TabIndex = 4
        self._label4.Text = "Total:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label3.Location = System.Drawing.Point(6, 94)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(98, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "Tax:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label5.Location = System.Drawing.Point(6, 46)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(98, 23)
        self._label5.TabIndex = 3
        self._label5.Text = "Tickets:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 212)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(235, 45)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(275, 212)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(235, 45)
        self._button2.TabIndex = 4
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = True
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Location = System.Drawing.Point(123, 145)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(77, 23)
        self._label7.TabIndex = 10
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(123, 94)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(77, 23)
        self._label6.TabIndex = 9
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Location = System.Drawing.Point(123, 46)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(77, 23)
        self._label8.TabIndex = 8
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # StudentTicketSales
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(522, 269)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox1)
        self.Name = "StudentTicketSales"
        self.Text = "StudentTicketSales"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self._groupBox3.ResumeLayout(False)
        self.ResumeLayout(False)


    

