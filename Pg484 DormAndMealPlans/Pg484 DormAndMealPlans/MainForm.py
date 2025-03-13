import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.Total = 0
        
    def InitializeComponent(self):
        self._label2 = System.Windows.Forms.Label()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(18, 321)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(467, 47)
        self._label2.TabIndex = 9
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(18, 237)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(467, 47)
        self._label1.TabIndex = 8
        self._label1.Text = "Total Price"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(18, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(467, 51)
        self._button1.TabIndex = 10
        self._button1.Text = "Dorm Halls"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(18, 78)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(467, 51)
        self._button2.TabIndex = 11
        self._button2.Text = "Meal Plans"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(18, 146)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(467, 51)
        self._button3.TabIndex = 12
        self._button3.Text = "Reset"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(497, 399)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Pg484 DormAndMealPlans"
        self.ResumeLayout(False)



   
        
    def Button1Click(self, sender, e):
        from DormHalls import *
        DH = DormHalls(self)
        DH.Show()
        self.Hide()

    def Button2Click(self, sender, e):
        from MealPlans import *
        MP = MealPlans(self)
        MP.Show()
        self.Hide()

    def Button3Click(self, sender, e):
        self._label2.Text = ""