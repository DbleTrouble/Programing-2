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
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(234, 230)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(198, 50)
        self._button2.TabIndex = 11
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(22, 230)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(194, 50)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(214, 21)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(218, 20)
        self._textBox1.TabIndex = 9
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(214, 169)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(218, 41)
        self._label3.TabIndex = 8
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(23, 169)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(146, 41)
        self._label2.TabIndex = 7
        self._label2.Text = "Anagrams:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(23, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(146, 41)
        self._label1.TabIndex = 6
        self._label1.Text = "Enter Text:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.Location = System.Drawing.Point(213, 100)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(218, 20)
        self._textBox2.TabIndex = 13
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(22, 88)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(146, 41)
        self._label4.TabIndex = 12
        self._label4.Text = "Enter Second Text:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.LawnGreen
        self.ClientSize = System.Drawing.Size(454, 304)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "StringInt 2"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        self._label3.Text = ""
        word1 = self._textBox1.Text.lower()
        word2 = self._textBox2.Text.lower()
        
        if len(word1) != len(word2):
            self._label3.Text = "False"
        else:
            for lcv in range(len(word1)):
                c = word1[lcv]
                index = word2.find(c)
                if index == -1:
                    self._label3 .Text = "False"
                else:
                    word2 = word2[:index] + word2[index+1:]
        self._label3.Text = str(len(word2) == 0)

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = ""
        self._textBox2.Text = ""