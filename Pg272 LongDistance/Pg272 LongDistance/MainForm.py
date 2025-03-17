import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(311, 53)
        self._label1.TabIndex = 2
        self._label1.Text = "Choose Your Category"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # radioButton1
        # 
        self._radioButton1.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._radioButton1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton1.Location = System.Drawing.Point(13, 90)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(218, 30)
        self._radioButton1.TabIndex = 3
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Daytime (6:00 am to 5:59 pm)"
        self._radioButton1.UseVisualStyleBackColor = False
        # 
        # radioButton2
        # 
        self._radioButton2.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._radioButton2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton2.Location = System.Drawing.Point(13, 140)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(218, 30)
        self._radioButton2.TabIndex = 4
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Evening (6:00 pm to 11:59 pm)"
        self._radioButton2.UseVisualStyleBackColor = False
        # 
        # radioButton3
        # 
        self._radioButton3.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._radioButton3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._radioButton3.Location = System.Drawing.Point(13, 189)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(218, 30)
        self._radioButton3.TabIndex = 5
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Off-peak (12:00 am to 5:59 am)"
        self._radioButton3.UseVisualStyleBackColor = False
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Location = System.Drawing.Point(237, 90)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(87, 30)
        self._label2.TabIndex = 6
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Location = System.Drawing.Point(237, 140)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(87, 30)
        self._label3.TabIndex = 7
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Location = System.Drawing.Point(237, 189)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(87, 30)
        self._label4.TabIndex = 8
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label5.Location = System.Drawing.Point(13, 242)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(218, 30)
        self._label5.TabIndex = 9
        self._label5.Text = "Number of Minutes:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(237, 248)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(87, 20)
        self._textBox1.TabIndex = 10
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 286)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(311, 38)
        self._button1.TabIndex = 11
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self.ClientSize = System.Drawing.Size(340, 336)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._radioButton3)
        self.Controls.Add(self._radioButton2)
        self.Controls.Add(self._radioButton1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg272 LongDistance"
        self.ResumeLayout(False)
        self.PerformLayout()


    

    def Button1Click(self, sender, e):
        mins = float(self._textBox1.Text)
        
        if self._radioButton1.Checked:
            A = mins * .07
            self._label2.Text = "$" + str(A)
        elif self._radioButton2.Checked:
            B = mins * .12
            self._label3.Text = "$" + str(B)
        elif self._radioButton3.Checked:
            C = mins * .05
            self._label4.Text = "$" + str(C)