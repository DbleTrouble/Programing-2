
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class Pluto(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
        self._label1.Text = "Type"
        self._label2.Text = "Average distance from the sun"
        self._label3.Text = "Mass"
        self._label4.Text = "Surface temperature"
        
    def InitializeComponent(self):
        self.SuspendLayout()
        # 
        # Pluto
        # 
        self.ClientSize = System.Drawing.Size(379, 309)
        self.Name = "Pluto"
        self.Text = "Pluto"
        self.ResumeLayout(False)

