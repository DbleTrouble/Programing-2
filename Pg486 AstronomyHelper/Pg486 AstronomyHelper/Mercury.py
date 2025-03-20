
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Mercury(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(198, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 50)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(198, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "label2"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 91)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(198, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "label3"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 132)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(198, 23)
        self._label4.TabIndex = 3
        self._label4.Text = "label4"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 225)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(326, 52)
        self._button1.TabIndex = 5
        self._button1.Text = "Close"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(216, 9)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(123, 23)
        self._label6.TabIndex = 6
        self._label6.Text = "Terrestial"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(216, 50)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(123, 23)
        self._label7.TabIndex = 7
        self._label7.Text = "0.387 AU"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(216, 91)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(123, 23)
        self._label8.TabIndex = 8
        self._label8.Text = "3.31 * 10^23 kg"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(216, 132)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(123, 23)
        self._label9.TabIndex = 9
        self._label9.Text = "-173 C to 430 C"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # Mercury
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(351, 289)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "Mercury"
        self.Text = "Mercury"
        self.FormClosing += self.MercuryFormClosing
        self.Load += self.MercuryLoad
        self.ResumeLayout(False)


    def MercuryLoad(self, sender, e):
        self._label1.Text = "Type"
        self._label2.Text = "Average distance from the sun"
        self._label3.Text = "Mass"
        self._label4.Text = "Surface temperature"

    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Close()

    def MercuryFormClosing(self, sender, e):
        self.myparent.Show()
