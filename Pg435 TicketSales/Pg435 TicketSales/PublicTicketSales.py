
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class PublicTicketSales(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Controls.Add(self._textBox1)
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
        self._groupBox3.Controls.Add(self._label7)
        self._groupBox3.Controls.Add(self._label6)
        self._groupBox3.Controls.Add(self._label5)
        self._groupBox3.Controls.Add(self._label4)
        self._groupBox3.Controls.Add(self._label2)
        self._groupBox3.Controls.Add(self._label3)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(244, 132)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(206, 193)
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
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(322, 47)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(109, 26)
        self._textBox1.TabIndex = 0
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label1.Location = System.Drawing.Point(96, 49)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(193, 23)
        self._label1.TabIndex = 1
        self._label1.Text = "Number of Tickets:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label2.Location = System.Drawing.Point(6, 94)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(98, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Tax:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._label3.Location = System.Drawing.Point(6, 46)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(98, 23)
        self._label3.TabIndex = 3
        self._label3.Text = "Tickets:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
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
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 331)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(206, 41)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(244, 331)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(206, 41)
        self._button2.TabIndex = 3
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Location = System.Drawing.Point(123, 46)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(77, 23)
        self._label5.TabIndex = 5
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Location = System.Drawing.Point(123, 94)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(77, 23)
        self._label6.TabIndex = 6
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Location = System.Drawing.Point(123, 145)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(77, 23)
        self._label7.TabIndex = 7
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # PublicTicketSales
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(462, 383)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox1)
        self.Name = "PublicTicketSales"
        self.Text = "PublicTicketSales"
        self.FormClosing += self.PublicTicketSalesFormClosing
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        NumT = int(self._textBox1.Text)
        if self._radioButton1.Checked:
            A = NumT * 20
        elif self._radioButton2.Checked:
            B = NumT *30
        elif self._radioButton2.Checked:
            pass

    def Button2Click(self, sender, e):
        self.myparent.Show()
        self.Close()

    def PublicTicketSalesFormClosing(self, sender, e):
        self.myparent.Show()