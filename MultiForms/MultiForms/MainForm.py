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
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(48, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(137, 97)
        self._button1.TabIndex = 0
        self._button1.Text = "Show New Form"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(12, 144)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(210, 20)
        self._textBox1.TabIndex = 1
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(234, 214)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "MultiForms"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        from Form1 import *
        msg = self._textBox1.Text
        form1 = Form1(self, msg)
        form1.Show()
        self.Hide()