import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self._comboBox2 = System.Windows.Forms.ComboBox()
        self._comboBox3 = System.Windows.Forms.ComboBox()
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._groupBox1.Controls.Add(self._comboBox1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(200, 100)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Styles:"
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._groupBox2.Controls.Add(self._comboBox2)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(273, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(200, 100)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Sizes:"
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self._groupBox3.Controls.Add(self._comboBox3)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(144, 119)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(200, 100)
        self._groupBox3.TabIndex = 1
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Colors:"
        # 
        # comboBox1
        # 
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["Regular shades",
            "Folding shades",
            "Roman shades"]))
        self._comboBox1.Location = System.Drawing.Point(6, 43)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(188, 24)
        self._comboBox1.TabIndex = 0
        # 
        # comboBox2
        # 
        self._comboBox2.FormattingEnabled = True
        self._comboBox2.Items.AddRange(System.Array[System.Object](
            ["25 inches wide",
            "27 inches wide",
            "32 inches wide",
            "40 inches wide"]))
        self._comboBox2.Location = System.Drawing.Point(6, 38)
        self._comboBox2.Name = "comboBox2"
        self._comboBox2.Size = System.Drawing.Size(188, 24)
        self._comboBox2.TabIndex = 1
        # 
        # comboBox3
        # 
        self._comboBox3.FormattingEnabled = True
        self._comboBox3.Items.AddRange(System.Array[System.Object](
            ["Natural",
            "Blue",
            "Teal",
            "Red",
            "Green"]))
        self._comboBox3.Location = System.Drawing.Point(6, 39)
        self._comboBox3.Name = "comboBox3"
        self._comboBox3.Size = System.Drawing.Size(188, 24)
        self._comboBox3.TabIndex = 2
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 234)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(460, 47)
        self._label1.TabIndex = 2
        self._label1.Text = "Total Price"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(255, 255, 128)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(13, 291)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(460, 47)
        self._label2.TabIndex = 3
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 351)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(460, 39)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self.ClientSize = System.Drawing.Size(485, 402)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "Pg485 ShadeDesigner"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox3.ResumeLayout(False)
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        T = 0
        S1 = self._comboBox1.Text
        S2 = self._comboBox2.Text
        S3 = self._comboBox3.Text
        
        if S1 == "Regular shades":
            T += 0
        elif S1 == "Folding shades":
            T += 10
        elif S1 == "Roman shades":
            T += 15
            
        if S2 == "25 inches wide":
            T += 0
        elif S2 == "27 inches wide":
            T += 2
        elif S2 == "32 inches wide":
            T += 4
        elif S2 == "40 inches wide":
            T += 6
        
        if S3 == "Natural":
            T += 5
        elif S3 == "Blue":
            T += 0
        elif S3 == "Teal":
            T += 0
        elif S3 == "Red":
            T += 0
        elif S3 == "Green":
            T += 0
        
        self._label2.Text = "$" + str(T)