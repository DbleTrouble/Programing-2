namespace Prog54a
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.lblMiles = new System.Windows.Forms.Label();
            this.lblGallons = new System.Windows.Forms.Label();
            this.lblMpg = new System.Windows.Forms.Label();
            this.comboBox1 = new System.Windows.Forms.ComboBox();
            this.SuspendLayout();
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(32, 277);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(110, 48);
            this.button1.TabIndex = 0;
            this.button1.Text = "Calculate";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(218, 277);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(96, 47);
            this.button2.TabIndex = 1;
            this.button2.Text = "Clear";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label1.Location = new System.Drawing.Point(13, 13);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(138, 44);
            this.label1.TabIndex = 2;
            this.label1.Text = "Car";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label2
            // 
            this.label2.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label2.Location = new System.Drawing.Point(13, 84);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(138, 44);
            this.label2.TabIndex = 3;
            this.label2.Text = "Miles";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label3
            // 
            this.label3.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label3.Location = new System.Drawing.Point(13, 143);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(138, 44);
            this.label3.TabIndex = 4;
            this.label3.Text = "Gallons";
            this.label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label4
            // 
            this.label4.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.label4.Location = new System.Drawing.Point(13, 210);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(138, 44);
            this.label4.TabIndex = 5;
            this.label4.Text = "MPG";
            this.label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblMiles
            // 
            this.lblMiles.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblMiles.Location = new System.Drawing.Point(211, 84);
            this.lblMiles.Name = "lblMiles";
            this.lblMiles.Size = new System.Drawing.Size(138, 44);
            this.lblMiles.TabIndex = 6;
            this.lblMiles.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblGallons
            // 
            this.lblGallons.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblGallons.Location = new System.Drawing.Point(211, 143);
            this.lblGallons.Name = "lblGallons";
            this.lblGallons.Size = new System.Drawing.Size(138, 44);
            this.lblGallons.TabIndex = 7;
            this.lblGallons.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // lblMpg
            // 
            this.lblMpg.BackColor = System.Drawing.SystemColors.ActiveCaption;
            this.lblMpg.Location = new System.Drawing.Point(211, 210);
            this.lblMpg.Name = "lblMpg";
            this.lblMpg.Size = new System.Drawing.Size(138, 44);
            this.lblMpg.TabIndex = 8;
            this.lblMpg.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // comboBox1
            // 
            this.comboBox1.FormattingEnabled = true;
            this.comboBox1.Items.AddRange(new object[] {
            "1970 VW Bug",
            "1979 Firebird",
            "1980 Subaru",
            "1975 Cutlass"});
            this.comboBox1.Location = new System.Drawing.Point(214, 13);
            this.comboBox1.Name = "comboBox1";
            this.comboBox1.Size = new System.Drawing.Size(135, 21);
            this.comboBox1.TabIndex = 9;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(361, 360);
            this.Controls.Add(this.comboBox1);
            this.Controls.Add(this.lblMpg);
            this.Controls.Add(this.lblGallons);
            this.Controls.Add(this.lblMiles);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label lblMiles;
        private System.Windows.Forms.Label lblGallons;
        private System.Windows.Forms.Label lblMpg;
        private System.Windows.Forms.ComboBox comboBox1;
    }
}

