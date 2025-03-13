
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class DormHalls(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(215, 114)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(166, 43)
        self._button2.TabIndex = 11
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(215, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(166, 43)
        self._button1.TabIndex = 10
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # radioButton4
        # 
        self._radioButton4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._radioButton4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton4.Location = System.Drawing.Point(13, 172)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(161, 24)
        self._radioButton4.TabIndex = 9
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "University Suites"
        self._radioButton4.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(13, 114)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(161, 24)
        self._radioButton3.TabIndex = 8
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Farthing Hall"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(13, 64)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(161, 24)
        self._radioButton2.TabIndex = 7
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Pike Hall"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(13, 13)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(161, 24)
        self._radioButton1.TabIndex = 6
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Allen Hall"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # DormHalls
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(429, 225)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._radioButton4)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Name = "DormHalls"
        self.Text = "DormHalls"
        self.FormClosing += self.DormHallsFormClosing
        self.ResumeLayout(False)


    def DHTotal(self):
        fee = 0
        if self._radioButton1.Checked:
            fee = 0
            fee += 1500
        elif self._radioButton2.Checked:
            fee = 0
            fee += 1600
        elif self._radioButton3.Checked:
            fee = 0
            fee += 1200
        elif self._radioButton4.Checked:
            fee = 0
            fee += 1800
            
        self.myparent.Total += fee
        
    def Button1Click(self, sender, e):
        self._radioButton1.Checked = False
        self._radioButton2.Checked = False
        self._radioButton3.Checked = False
        self._radioButton4.Checked = False

    def Button2Click(self, sender, e):
        self.DHTotal()
        self.myparent.Show()
        self.Close()

    def DormHallsFormClosing(self, sender, e):
        self.myparent._label2.Text = "$" + str(self.myparent.Total) + " per semester"
        self.myparent.Show()