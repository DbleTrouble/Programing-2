namespace prog435_TicketSales_Form
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
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.btnGeneral = new System.Windows.Forms.Button();
            this.btnStudent = new System.Windows.Forms.Button();
            this.btnExit = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.SuspendLayout();
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.btnStudent);
            this.groupBox1.Controls.Add(this.btnGeneral);
            this.groupBox1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.groupBox1.Location = new System.Drawing.Point(13, 13);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(332, 179);
            this.groupBox1.TabIndex = 0;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "groupBox1";
            // 
            // btnGeneral
            // 
            this.btnGeneral.Location = new System.Drawing.Point(226, 19);
            this.btnGeneral.Name = "btnGeneral";
            this.btnGeneral.Size = new System.Drawing.Size(100, 51);
            this.btnGeneral.TabIndex = 1;
            this.btnGeneral.Text = "General Sales";
            this.btnGeneral.UseVisualStyleBackColor = true;
            this.btnGeneral.Click += new System.EventHandler(this.button1_Click);
            // 
            // btnStudent
            // 
            this.btnStudent.Location = new System.Drawing.Point(226, 108);
            this.btnStudent.Name = "btnStudent";
            this.btnStudent.Size = new System.Drawing.Size(100, 51);
            this.btnStudent.TabIndex = 2;
            this.btnStudent.Text = "Student Sales";
            this.btnStudent.UseVisualStyleBackColor = true;
            this.btnStudent.Click += new System.EventHandler(this.button2_Click);
            // 
            // btnExit
            // 
            this.btnExit.Location = new System.Drawing.Point(245, 198);
            this.btnExit.Name = "btnExit";
            this.btnExit.Size = new System.Drawing.Size(100, 51);
            this.btnExit.TabIndex = 3;
            this.btnExit.Text = "Exit";
            this.btnExit.UseVisualStyleBackColor = true;
            this.btnExit.Click += new System.EventHandler(this.button3_Click);
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
            this.label1.Location = new System.Drawing.Point(6, 19);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(214, 51);
            this.label1.TabIndex = 3;
            this.label1.Text = "Select General Sales for all ticket sales to the general public.";
            this.label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // label2
            // 
            this.label2.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(192)))), ((int)(((byte)(192)))));
            this.label2.Location = new System.Drawing.Point(6, 108);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(214, 51);
            this.label2.TabIndex = 4;
            this.label2.Text = "Select Student Sales for student ticket sales.";
            this.label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(357, 261);
            this.Controls.Add(this.btnExit);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Form1";
            this.groupBox1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button btnStudent;
        private System.Windows.Forms.Button btnGeneral;
        private System.Windows.Forms.Button btnExit;
    }
}

