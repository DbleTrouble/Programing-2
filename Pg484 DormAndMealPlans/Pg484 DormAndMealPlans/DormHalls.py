
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class DormHalls(Form):
    def __init__(self, parent):
        self.InitializeComponent()
        self.myparent = parent
    
    def InitializeComponent(self):
        self.Name = "DormHalls"
        self.Text = "DormHalls"

