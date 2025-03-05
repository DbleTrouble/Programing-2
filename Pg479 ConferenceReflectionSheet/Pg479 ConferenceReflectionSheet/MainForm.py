import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label8 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._textBox5 = System.Windows.Forms.TextBox()
        self._textBox6 = System.Windows.Forms.TextBox()
        self._textBox7 = System.Windows.Forms.TextBox()
        self._textBox8 = System.Windows.Forms.TextBox()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox1.Controls.Add(self._textBox5)
        self._groupBox1.Controls.Add(self._textBox6)
        self._groupBox1.Controls.Add(self._textBox7)
        self._groupBox1.Controls.Add(self._textBox8)
        self._groupBox1.Controls.Add(self._textBox4)
        self._groupBox1.Controls.Add(self._textBox3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label8)
        self._groupBox1.Controls.Add(self._label7)
        self._groupBox1.Controls.Add(self._label6)
        self._groupBox1.Controls.Add(self._label5)
        self._groupBox1.Controls.Add(self._label4)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(525, 176)
        self._groupBox1.TabIndex = 1
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Registrant"
        # 
        # textBox4
        # 
        self._textBox4.Location = System.Drawing.Point(129, 141)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(100, 22)
        self._textBox4.TabIndex = 11
        # 
        # textBox3
        # 
        self._textBox3.Location = System.Drawing.Point(129, 100)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 22)
        self._textBox3.TabIndex = 10
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(129, 60)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 22)
        self._textBox2.TabIndex = 9
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(129, 22)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 22)
        self._textBox1.TabIndex = 8
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label8.Location = System.Drawing.Point(253, 141)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(100, 23)
        self._label8.TabIndex = 7
        self._label8.Text = "label8"
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label7.Location = System.Drawing.Point(253, 100)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(100, 23)
        self._label7.TabIndex = 6
        self._label7.Text = "label7"
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label6.Location = System.Drawing.Point(253, 60)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 23)
        self._label6.TabIndex = 5
        self._label6.Text = "label6"
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label5.Location = System.Drawing.Point(253, 22)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 4
        self._label5.Text = "label5"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label4.Location = System.Drawing.Point(7, 141)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(100, 23)
        self._label4.TabIndex = 3
        self._label4.Text = "label4"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Location = System.Drawing.Point(7, 100)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 2
        self._label3.Text = "label3"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label2.Location = System.Drawing.Point(7, 60)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 1
        self._label2.Text = "label2"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label1.Location = System.Drawing.Point(7, 22)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "label1"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleRight
        # 
        # textBox5
        # 
        self._textBox5.Location = System.Drawing.Point(390, 141)
        self._textBox5.Name = "textBox5"
        self._textBox5.Size = System.Drawing.Size(100, 22)
        self._textBox5.TabIndex = 15
        # 
        # textBox6
        # 
        self._textBox6.Location = System.Drawing.Point(390, 100)
        self._textBox6.Name = "textBox6"
        self._textBox6.Size = System.Drawing.Size(100, 22)
        self._textBox6.TabIndex = 14
        # 
        # textBox7
        # 
        self._textBox7.Location = System.Drawing.Point(390, 60)
        self._textBox7.Name = "textBox7"
        self._textBox7.Size = System.Drawing.Size(100, 22)
        self._textBox7.TabIndex = 13
        # 
        # textBox8
        # 
        self._textBox8.Location = System.Drawing.Point(390, 22)
        self._textBox8.Name = "textBox8"
        self._textBox8.Size = System.Drawing.Size(100, 22)
        self._textBox8.TabIndex = 12
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(226, 212)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(139, 37)
        self._label9.TabIndex = 16
        self._label9.Text = "Total"
        self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label10.Location = System.Drawing.Point(402, 212)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(100, 37)
        self._label10.TabIndex = 17
        self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 262)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(140, 52)
        self._button1.TabIndex = 18
        self._button1.Text = "Select Conference Options"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(202, 262)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(140, 52)
        self._button2.TabIndex = 19
        self._button2.Text = "Reset"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(397, 262)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(140, 52)
        self._button3.TabIndex = 20
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Turquoise
        self.ClientSize = System.Drawing.Size(549, 326)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._label9)
        self.Name = "MainForm"
        self.Text = "Pg479 ConferenceReflectionSheet"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        from ConferenceOptions import *
        CO = ConferenceOptions(self)
        CO.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        self._label10.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""
        self._textBox3.Text = ""
        self._textBox4.Text = ""
        self._textBox5.Text = ""
        self._textBox6.Text = ""
        self._textBox7.Text = ""
        self._textBox8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()