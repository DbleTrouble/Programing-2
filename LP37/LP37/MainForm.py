import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label1 = System.Windows.Forms.Label()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 191)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(125, 52)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(37, 29)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 26)
        self._textBox1.TabIndex = 1
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(37, 73)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(408, 107)
        self._label1.TabIndex = 2
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(175, 191)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(125, 52)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(345, 191)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(125, 52)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(345, 29)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 26)
        self._textBox2.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(482, 255)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "LP37"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        n1 = int(self._textBox1.Text)
        n2 = int(self._textBox2.Text)
        from DivAndMod import *
        dm1 = DivAndMod(n1, n2)
        dm2 = DivAndMod(n2, n1)
        dm1.calc()
        dm2.calc()
        div1 = dm1.get_div()
        mod1 = dm1.get_mod()
        div2, mod2 = dm2.get_divmod()
        
        self._label1.Text =  str(n1) + "/" + str(n2) + "=" + str(div1) + "\n"
        self._label1.Text += str(n1) + "%" + str(n2) + "=" + str(mod1) + "\n\n"
        
        self._label1.Text += str(n2) + "/" + str(n1) + "=" + str(div1) + "\n"
        self._label1.Text += str(n2) + "%" + str(n1) + "=" + str(mod2)

    def Button2Click(self, sender, e):
        self._label1.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()