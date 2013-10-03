namespace Testeri
{
    partial class VastausIkkuna
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
            this.A_Nappi = new System.Windows.Forms.Button();
            this.B_nappi = new System.Windows.Forms.Button();
            this.C_Nappi = new System.Windows.Forms.Button();
            this.D_Nappi = new System.Windows.Forms.Button();
            this.KysymysLabel = new System.Windows.Forms.Label();
            this.shapeContainer1 = new Microsoft.VisualBasic.PowerPacks.ShapeContainer();
            this.rectangleShape1 = new Microsoft.VisualBasic.PowerPacks.RectangleShape();
            this.SuspendLayout();
            // 
            // A_Nappi
            // 
            this.A_Nappi.Location = new System.Drawing.Point(18, 103);
            this.A_Nappi.Name = "A_Nappi";
            this.A_Nappi.Size = new System.Drawing.Size(168, 23);
            this.A_Nappi.TabIndex = 0;
            this.A_Nappi.Text = "A";
            this.A_Nappi.UseVisualStyleBackColor = true;
            this.A_Nappi.Click += new System.EventHandler(this.A_Nappi_Click);
            // 
            // B_nappi
            // 
            this.B_nappi.Location = new System.Drawing.Point(18, 142);
            this.B_nappi.Name = "B_nappi";
            this.B_nappi.Size = new System.Drawing.Size(168, 23);
            this.B_nappi.TabIndex = 1;
            this.B_nappi.Text = "B";
            this.B_nappi.UseVisualStyleBackColor = true;
            this.B_nappi.Click += new System.EventHandler(this.B_nappi_Click);
            // 
            // C_Nappi
            // 
            this.C_Nappi.Location = new System.Drawing.Point(192, 103);
            this.C_Nappi.Name = "C_Nappi";
            this.C_Nappi.Size = new System.Drawing.Size(167, 23);
            this.C_Nappi.TabIndex = 2;
            this.C_Nappi.Text = "C";
            this.C_Nappi.UseVisualStyleBackColor = true;
            this.C_Nappi.Click += new System.EventHandler(this.C_Nappi_Click);
            // 
            // D_Nappi
            // 
            this.D_Nappi.Location = new System.Drawing.Point(192, 142);
            this.D_Nappi.Name = "D_Nappi";
            this.D_Nappi.Size = new System.Drawing.Size(167, 23);
            this.D_Nappi.TabIndex = 3;
            this.D_Nappi.Text = "D";
            this.D_Nappi.UseVisualStyleBackColor = true;
            this.D_Nappi.Click += new System.EventHandler(this.D_Nappi_Click);
            // 
            // KysymysLabel
            // 
            this.KysymysLabel.AutoSize = true;
            this.KysymysLabel.BackColor = System.Drawing.Color.White;
            this.KysymysLabel.Cursor = System.Windows.Forms.Cursors.Default;
            this.KysymysLabel.ForeColor = System.Drawing.Color.Black;
            this.KysymysLabel.Location = new System.Drawing.Point(19, 18);
            this.KysymysLabel.MaximumSize = new System.Drawing.Size(338, 72);
            this.KysymysLabel.MinimumSize = new System.Drawing.Size(338, 72);
            this.KysymysLabel.Name = "KysymysLabel";
            this.KysymysLabel.Size = new System.Drawing.Size(338, 72);
            this.KysymysLabel.TabIndex = 4;
            this.KysymysLabel.Text = "Tässä on kysymys";
            this.KysymysLabel.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // shapeContainer1
            // 
            this.shapeContainer1.Location = new System.Drawing.Point(0, 0);
            this.shapeContainer1.Margin = new System.Windows.Forms.Padding(0);
            this.shapeContainer1.Name = "shapeContainer1";
            this.shapeContainer1.Shapes.AddRange(new Microsoft.VisualBasic.PowerPacks.Shape[] {
            this.rectangleShape1});
            this.shapeContainer1.Size = new System.Drawing.Size(378, 171);
            this.shapeContainer1.TabIndex = 5;
            this.shapeContainer1.TabStop = false;
            // 
            // rectangleShape1
            // 
            this.rectangleShape1.BackColor = System.Drawing.SystemColors.ControlLightLight;
            this.rectangleShape1.FillColor = System.Drawing.SystemColors.ControlLightLight;
            this.rectangleShape1.FillGradientColor = System.Drawing.Color.White;
            this.rectangleShape1.FillStyle = Microsoft.VisualBasic.PowerPacks.FillStyle.Solid;
            this.rectangleShape1.Location = new System.Drawing.Point(18, 17);
            this.rectangleShape1.Name = "rectangleShape1";
            this.rectangleShape1.Size = new System.Drawing.Size(340, 74);
            // 
            // VastausIkkuna
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(378, 171);
            this.Controls.Add(this.KysymysLabel);
            this.Controls.Add(this.D_Nappi);
            this.Controls.Add(this.C_Nappi);
            this.Controls.Add(this.B_nappi);
            this.Controls.Add(this.A_Nappi);
            this.Controls.Add(this.shapeContainer1);
            this.Name = "VastausIkkuna";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button A_Nappi;
        private System.Windows.Forms.Button B_nappi;
        private System.Windows.Forms.Button C_Nappi;
        private System.Windows.Forms.Button D_Nappi;
        private System.Windows.Forms.Label KysymysLabel;
        private Microsoft.VisualBasic.PowerPacks.ShapeContainer shapeContainer1;
        private Microsoft.VisualBasic.PowerPacks.RectangleShape rectangleShape1;
    }
}

