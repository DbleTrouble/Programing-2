
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class ConferenceOptions(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(239, 122)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Conference"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(280, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(239, 122)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Preconference Workshops"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 151)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(240, 38)
        self._button1.TabIndex = 2
        self._button1.Text = "Reset"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(280, 151)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(240, 38)
        self._button2.TabIndex = 3
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # ConferenceOptions
        # 
        self.BackColor = System.Drawing.Color.Turquoise
        self.ClientSize = System.Drawing.Size(531, 201)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "ConferenceOptions"
        self.Text = "ConferenceOptions"
        self.FormClosing += self.ConferenceOptionsFormClosing
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        pass

    def ConferenceOptionsFormClosing(self, sender, e):
        pass