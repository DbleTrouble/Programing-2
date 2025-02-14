﻿
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Form1(Form):
    def __init__(self, parent, msg):
        self.InitializeComponent()
        self.myparent = parent
        self.msg = msg
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 191)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(259, 58)
        self._button1.TabIndex = 1
        self._button1.Text = "Show Home Form"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(259, 141)
        self._label1.TabIndex = 2
        self._label1.Text = "label1"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # Form1
        # 
        self.ClientSize = System.Drawing.Size(284, 261)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button1)
        self.Name = "Form1"
        self.Text = "Form1"
        self.FormClosing += self.Form1FormClosing
        self.Load += self.Form1Load
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self.myparent.Show()
        self.Close()
        

    def Form1Load(self, sender, e):
        self._label1.Text = self.msg

    def Form1FormClosing(self, sender, e):
        self.myparent.Show()
        