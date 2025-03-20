
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Venus(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self._label9 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(216, 133)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(123, 23)
        self._label9.TabIndex = 20
        self._label9.Text = "472 C"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(216, 92)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(123, 23)
        self._label8.TabIndex = 19
        self._label8.Text = "4.87 * 10 ^24 kg"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(216, 51)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(123, 23)
        self._label7.TabIndex = 18
        self._label7.Text = "0.7233 AU"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(216, 10)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(123, 23)
        self._label6.TabIndex = 17
        self._label6.Text = "Terrestial"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 226)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(326, 52)
        self._button1.TabIndex = 16
        self._button1.Text = "Close"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(12, 133)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(198, 23)
        self._label4.TabIndex = 14
        self._label4.Text = "label4"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(12, 92)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(198, 23)
        self._label3.TabIndex = 13
        self._label3.Text = "label3"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 51)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(198, 23)
        self._label2.TabIndex = 12
        self._label2.Text = "label2"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 10)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(198, 23)
        self._label1.TabIndex = 11
        self._label1.Text = "label1"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # Venus
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
        self.Name = "Venus"
        self.Text = "Venus"
        self.FormClosing += self.VenusFormClosing
        self.Load += self.VenusLoad
        self.ResumeLayout(False)


    def VenusLoad(self, sender, e):
        self._label1.Text = "Type"
        self._label2.Text = "Average distance from the sun"
        self._label3.Text = "Mass"
        self._label4.Text = "Surface temperature"

    def VenusFormClosing(self, sender, e):
        self.myparent.Show()

    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Close()