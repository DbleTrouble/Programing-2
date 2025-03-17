import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._menuStrip1 = System.Windows.Forms.MenuStrip()
        self._fileToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._exitToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._colorToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._redToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._greenToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._blueToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._blackToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._toolStripMenuItem2 = System.Windows.Forms.ToolStripMenuItem()
        self._visibleToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._helpToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._aboutToolStripMenuItem = System.Windows.Forms.ToolStripMenuItem()
        self._label1 = System.Windows.Forms.Label()
        self._menuStrip1.SuspendLayout()
        self.SuspendLayout()
        # 
        # menuStrip1
        # 
        self._menuStrip1.Items.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._fileToolStripMenuItem,
            self._colorToolStripMenuItem,
            self._helpToolStripMenuItem]))
        self._menuStrip1.Location = System.Drawing.Point(0, 0)
        self._menuStrip1.Name = "menuStrip1"
        self._menuStrip1.Size = System.Drawing.Size(405, 24)
        self._menuStrip1.TabIndex = 0
        self._menuStrip1.Text = "menuStrip1"
        # 
        # fileToolStripMenuItem
        # 
        self._fileToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._exitToolStripMenuItem]))
        self._fileToolStripMenuItem.Name = "fileToolStripMenuItem"
        self._fileToolStripMenuItem.Size = System.Drawing.Size(37, 20)
        self._fileToolStripMenuItem.Text = "File"
        # 
        # exitToolStripMenuItem
        # 
        self._exitToolStripMenuItem.Name = "exitToolStripMenuItem"
        self._exitToolStripMenuItem.Size = System.Drawing.Size(92, 22)
        self._exitToolStripMenuItem.Text = "Exit"
        self._exitToolStripMenuItem.Click += self.ExitToolStripMenuItemClick
        # 
        # colorToolStripMenuItem
        # 
        self._colorToolStripMenuItem.CheckOnClick = True
        self._colorToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._redToolStripMenuItem,
            self._greenToolStripMenuItem,
            self._blueToolStripMenuItem,
            self._blackToolStripMenuItem,
            self._toolStripMenuItem2,
            self._visibleToolStripMenuItem]))
        self._colorToolStripMenuItem.Name = "colorToolStripMenuItem"
        self._colorToolStripMenuItem.Size = System.Drawing.Size(48, 20)
        self._colorToolStripMenuItem.Text = "Color"
        # 
        # redToolStripMenuItem
        # 
        self._redToolStripMenuItem.Name = "redToolStripMenuItem"
        self._redToolStripMenuItem.Size = System.Drawing.Size(239, 22)
        self._redToolStripMenuItem.Text = "Red"
        self._redToolStripMenuItem.Click += self.RedToolStripMenuItemClick
        # 
        # greenToolStripMenuItem
        # 
        self._greenToolStripMenuItem.Name = "greenToolStripMenuItem"
        self._greenToolStripMenuItem.Size = System.Drawing.Size(239, 22)
        self._greenToolStripMenuItem.Text = "Green"
        self._greenToolStripMenuItem.Click += self.GreenToolStripMenuItemClick
        # 
        # blueToolStripMenuItem
        # 
        self._blueToolStripMenuItem.Name = "blueToolStripMenuItem"
        self._blueToolStripMenuItem.Size = System.Drawing.Size(239, 22)
        self._blueToolStripMenuItem.Text = "Blue"
        self._blueToolStripMenuItem.Click += self.BlueToolStripMenuItemClick
        # 
        # blackToolStripMenuItem
        # 
        self._blackToolStripMenuItem.Name = "blackToolStripMenuItem"
        self._blackToolStripMenuItem.Size = System.Drawing.Size(239, 22)
        self._blackToolStripMenuItem.Text = "Black"
        self._blackToolStripMenuItem.Click += self.BlackToolStripMenuItemClick
        # 
        # toolStripMenuItem2
        # 
        self._toolStripMenuItem2.Name = "toolStripMenuItem2"
        self._toolStripMenuItem2.Size = System.Drawing.Size(239, 22)
        self._toolStripMenuItem2.Text = "---------------------------------"
        # 
        # visibleToolStripMenuItem
        # 
        self._visibleToolStripMenuItem.Name = "visibleToolStripMenuItem"
        self._visibleToolStripMenuItem.Size = System.Drawing.Size(239, 22)
        self._visibleToolStripMenuItem.Text = "Visible"
        self._visibleToolStripMenuItem.Click += self.VisibleToolStripMenuItemClick
        # 
        # helpToolStripMenuItem
        # 
        self._helpToolStripMenuItem.DropDownItems.AddRange(System.Array[System.Windows.Forms.ToolStripItem](
            [self._aboutToolStripMenuItem]))
        self._helpToolStripMenuItem.Name = "helpToolStripMenuItem"
        self._helpToolStripMenuItem.Size = System.Drawing.Size(44, 20)
        self._helpToolStripMenuItem.Text = "Help"
        # 
        # aboutToolStripMenuItem
        # 
        self._aboutToolStripMenuItem.Name = "aboutToolStripMenuItem"
        self._aboutToolStripMenuItem.Size = System.Drawing.Size(107, 22)
        self._aboutToolStripMenuItem.Text = "About"
        self._aboutToolStripMenuItem.Click += self.AboutToolStripMenuItemClick
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 150)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(381, 115)
        self._label1.TabIndex = 1
        self._label1.Text = "Help Yourself!!!"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(405, 347)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._menuStrip1)
        self.MainMenuStrip = self._menuStrip1
        self.Name = "MainForm"
        self.Text = "Pg447 MenuDemo"
        self._menuStrip1.ResumeLayout(False)
        self._menuStrip1.PerformLayout()
        self.ResumeLayout(False)
        self.PerformLayout()


    def ExitToolStripMenuItemClick(self, sender, e):
        Application.Exit()

    def RedToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Red

    def GreenToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Green

    def BlueToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Blue

    def BlackToolStripMenuItemClick(self, sender, e):
        self._label1.ForeColor = Color.Black

    def VisibleToolStripMenuItemClick(self, sender, e):
        if self._visibleToolStripMenuItem.Checked == True:
            self._label1.Visible = True
        else:
            self._label1.Visible = False
            

    def AboutToolStripMenuItemClick(self, sender, e):
        MessageBox.Show("Menu System Demo\n"    \
                   "Designed for Starting Out " \
                   "with Windows Form Applications",
                   "About Menu Demo")