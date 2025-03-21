﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button2 = System.Windows.Forms.Button()
        self._button1 = System.Windows.Forms.Button()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(224, 145)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(198, 50)
        self._button2.TabIndex = 17
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 145)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(194, 50)
        self._button1.TabIndex = 16
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(203, 21)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(218, 20)
        self._textBox1.TabIndex = 15
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(203, 78)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(218, 41)
        self._label3.TabIndex = 14
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 78)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(146, 41)
        self._label2.TabIndex = 13
        self._label2.Text = "Duplicates:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(146, 41)
        self._label1.TabIndex = 12
        self._label1.Text = "Enter Text:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(436, 212)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StringInt 4"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label3.Text = ""
        txt = self._textBox1.Text.lower()
        txt2 = txt[::-1]
        self._label3.Text = str(txt2)

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""