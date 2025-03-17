import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label2 = System.Windows.Forms.Label()
        self._comboBox3 = System.Windows.Forms.ComboBox()
        self._label1 = System.Windows.Forms.Label()
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._comboBox2 = System.Windows.Forms.ComboBox()
        self._button1 = System.Windows.Forms.Button()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._comboBox4 = System.Windows.Forms.ComboBox()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self.SuspendLayout()
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(23, 305)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(460, 47)
        self._label2.TabIndex = 9
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # comboBox3
        # 
        self._comboBox3.FormattingEnabled = True
        self._comboBox3.Items.AddRange(System.Array[System.Object](
            ["51 mm",
            "55 mm",
            "58 mm",
            "61 mm"]))
        self._comboBox3.Location = System.Drawing.Point(6, 39)
        self._comboBox3.Name = "comboBox3"
        self._comboBox3.Size = System.Drawing.Size(188, 24)
        self._comboBox3.TabIndex = 2
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(23, 248)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(460, 47)
        self._label1.TabIndex = 8
        self._label1.Text = "Total Price"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._groupBox1.Controls.Add(self._comboBox1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(23, 27)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(200, 100)
        self._groupBox1.TabIndex = 5
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Decks:"
        # 
        # comboBox1
        # 
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["The Master Thrasher",
            "The Dictator of Grind",
            "The Street King"]))
        self._comboBox1.Location = System.Drawing.Point(6, 43)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(188, 24)
        self._comboBox1.TabIndex = 0
        # 
        # comboBox2
        # 
        self._comboBox2.FormattingEnabled = True
        self._comboBox2.Items.AddRange(System.Array[System.Object](
            ["7.75 Axle",
            "8 Axle ",
            "8.5 Axle"]))
        self._comboBox2.Location = System.Drawing.Point(6, 38)
        self._comboBox2.Name = "comboBox2"
        self._comboBox2.Size = System.Drawing.Size(188, 24)
        self._comboBox2.TabIndex = 1
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(23, 365)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(460, 39)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._groupBox2.Controls.Add(self._comboBox2)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(283, 27)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(200, 100)
        self._groupBox2.TabIndex = 6
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Truck Assemblies:"
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._groupBox3.Controls.Add(self._comboBox3)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(23, 133)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(200, 100)
        self._groupBox3.TabIndex = 7
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Wheel Sets:"
        # 
        # groupBox4
        # 
        self._groupBox4.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._groupBox4.Controls.Add(self._comboBox4)
        self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox4.Location = System.Drawing.Point(283, 133)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.Size = System.Drawing.Size(200, 100)
        self._groupBox4.TabIndex = 8
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Miscellaneous:"
        # 
        # comboBox4
        # 
        self._comboBox4.FormattingEnabled = True
        self._comboBox4.Items.AddRange(System.Array[System.Object](
            ["Grip Tape",
            "Bearings",
            "Riser Pads",
            "Nuts & Bolts Kit",
            "Assembly"]))
        self._comboBox4.Location = System.Drawing.Point(6, 39)
        self._comboBox4.Name = "comboBox4"
        self._comboBox4.Size = System.Drawing.Size(188, 24)
        self._comboBox4.TabIndex = 2
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(507, 431)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._groupBox1)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox3)
        self.Name = "MainForm"
        self.Text = "Pg485 SkateboardDesigner"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self._groupBox4.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        T = 0
        S1 = self._comboBox1.Text
        S2 = self._comboBox2.Text
        S3 = self._comboBox3.Text
        S4 = self._comboBox4.Text
        
        if S1 == "The Master Thrasher":
            T += 60
        elif S1 == "The Dictator of Grind":
            T += 45
        elif S1 == "The Street King":
            T += 50
            
        if S2 == "7.75 Axle":
            T += 35
        elif S2 == "8 Axle":
            T += 40
        elif S2 == "8.5 Axle":
            T += 45
        
        if S3 == "51 mm":
            T += 20
        elif S3 == "55 mm":
            T += 22
        elif S3 == "58 mm":
            T += 24
        elif S3 == "61 mm":
            T += 28
        
        if S4 == "Grip Tape":
            T += 10
        elif S4 == "Bearings":
            T += 30
        elif S4 == "Riser Pads":
            T += 2
        elif S4 == "Nuts & Bolts Kit":
            T += 3
        elif S4 == "Assembly":
            T += 10

        self._label2.Text = "$" + str(T)