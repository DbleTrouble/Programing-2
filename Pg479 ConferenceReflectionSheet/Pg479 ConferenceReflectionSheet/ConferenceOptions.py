
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class ConferenceOptions(Form):
    def __init__(self, parent,):
        self.InitializeComponent()
        self.myparent = parent
        
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox1.Controls.Add(self._checkBox2)
        self._groupBox1.Controls.Add(self._checkBox1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(247, 122)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Conference"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox2.Controls.Add(self._comboBox1)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(266, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(253, 122)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Preconference Workshops"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 151)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(248, 38)
        self._button1.TabIndex = 2
        self._button1.Text = "Reset"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(266, 151)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(254, 38)
        self._button2.TabIndex = 3
        self._button2.Text = "Close"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # checkBox1
        # 
        self._checkBox1.Location = System.Drawing.Point(6, 32)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(227, 24)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Conference Registrantion: $895"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Location = System.Drawing.Point(7, 71)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(240, 24)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Opening Night Dinner & Keynote: $30"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # comboBox1
        # 
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Intro to E-Commerce",
            "The Future of the Web",
            "Advanced Visual Basic",
            "Network Security"]))
        self._comboBox1.Location = System.Drawing.Point(6, 54)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(241, 24)
        self._comboBox1.TabIndex = 0
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
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)


    def ConferenceFee(self):
        fee = 0
        CB = self._comboBox1.Text
        
        if self._checkBox1.Checked == True:
            fee += 895
        elif self._checkBox2.Checked == True:
            fee += 30
        
        if CB == "Intro to E-Commerce":
            fee += 295
        elif CB == "The Future of the Web":
            fee += 295
        elif CB == "Advanced Visual Basic":
            fee += 395
        elif CB == "Network Security":
            fee += 395
        
        self.myparent.Total += fee
        
    
    def Button1Click(self, sender, e):
        self._checkBox1.Checked = False
        self._checkBox2.Checked = False
        self._comboBox1.Text = ""

    def Button2Click(self, sender, e):
        self.ConferenceFee()
        self.myparent.Show()
        self.Close()

    def ConferenceOptionsFormClosing(self, sender, e):
        self.myparent._label10.Text = "$" + str(self.myparent.Total)
        self.myparent.Show()