import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Controls.Add(self._button2)
        self._groupBox1.Controls.Add(self._button1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(425, 213)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Select the Type of Ticket Sales"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(299, 25)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(120, 55)
        self._button1.TabIndex = 0
        self._button1.Text = "General Sales"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(299, 123)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(120, 55)
        self._button2.TabIndex = 1
        self._button2.Text = "Student Sales"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(13, 258)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(425, 55)
        self._button3.TabIndex = 1
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(6, 25)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(259, 55)
        self._label1.TabIndex = 2
        self._label1.Text = "Select General Sales for all ticket sales to the general public."
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(6, 123)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(259, 55)
        self._label2.TabIndex = 3
        self._label2.Text = "Select Student Sales for all student ticket sales."
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(450, 325)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg435 TicketSales"
        self._groupBox1.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        from PublicTicketSales import *
        GT = PublicTicketSales()
        GT.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        from StudentTicketSales import *
        ST = StudentTicketSales()
        ST.Show()
        self.Hide()

    def Button3Click(self, sender, e):
        Application.Exit()