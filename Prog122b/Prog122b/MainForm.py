import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._button3 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self.SuspendLayout()
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(244, 384)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(124, 20)
        self._textBox2.TabIndex = 15
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(244, 271)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(124, 20)
        self._textBox1.TabIndex = 14
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.Gold
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(244, 325)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(124, 34)
        self._label2.TabIndex = 13
        self._label2.Text = "Rate of Pay"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Gold
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(244, 209)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(124, 34)
        self._label1.TabIndex = 12
        self._label1.Text = "Hours"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(244, 126)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(124, 32)
        self._button3.TabIndex = 11
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(244, 69)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(124, 32)
        self._button2.TabIndex = 10
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(244, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(124, 32)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(255, 128, 0)
        self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 16
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(225, 436)
        self._listBox1.TabIndex = 8
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(386, 464)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "Prog122b"
        self.ResumeLayout(False)
        self.PerformLayout()


    

    def Button1Click(self, sender, e):
        self._listBox1.Items.Clear()
        H = float(self._textBox1.Text)
        R = float(self._textBox2.Text)
        
        for i in range(1, H + 1):
            P = i * R
            self._listBox1.Items.Add(str(i) + "\t\t" + str(P)) 
        

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()