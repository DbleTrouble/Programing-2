
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MealPlans(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(13, 13)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(161, 24)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "7 meals per week"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(13, 64)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(161, 24)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "14 meals per week"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(13, 114)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(161, 24)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Unlimited meals"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(215, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(166, 43)
        self._button1.TabIndex = 4
        self._button1.Text = "Clear"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(215, 95)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(166, 43)
        self._button2.TabIndex = 5
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MealPlans
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(393, 159)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Name = "MealPlans"
        self.Text = "MealPlans"
        self.FormClosing += self.MealPlansFormClosing
        self.ResumeLayout(False)


    def MPTotal(self):
        fee = 0
        if self._radioButton1.Checked:
            fee = 0
            fee += 560
        elif self._radioButton2.Checked:
            fee = 0
            fee += 1095
        elif self._radioButton3.Checked:
            fee = 0
            fee += 1500
        
        self.myparent.Total += fee
        
    def Button1Click(self, sender, e):
        self._radioButton1.Checked = False
        self._radioButton2.Checked = False
        self._radioButton3.Checked = False

    def Button2Click(self, sender, e):
        self.MPTotal()
        self.myparent.Show()
        self.Close()

    def MealPlansFormClosing(self, sender, e):
        self.myparent._label2.Text = "$" + str(self.myparent.Total) + " per semester"
        self.myparent.Show()