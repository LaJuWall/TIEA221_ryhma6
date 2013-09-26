namespace Tietovisa
{
    partial class Aloitusikkuna
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
            this.Tervehdys_Label = new System.Windows.Forms.Label();
            this.Valitsin = new System.Windows.Forms.TrackBar();
            this.Aloitus_Nappi = new System.Windows.Forms.Button();
            this.nimi_boxi = new System.Windows.Forms.TextBox();
            this.Montako_Label = new System.Windows.Forms.Label();
            ((System.ComponentModel.ISupportInitialize)(this.Valitsin)).BeginInit();
            this.SuspendLayout();
            // 
            // Tervehdys_Label
            // 
            this.Tervehdys_Label.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Tervehdys_Label.ImageAlign = System.Drawing.ContentAlignment.TopCenter;
            this.Tervehdys_Label.Location = new System.Drawing.Point(2, 9);
            this.Tervehdys_Label.Name = "Tervehdys_Label";
            this.Tervehdys_Label.Size = new System.Drawing.Size(420, 144);
            this.Tervehdys_Label.TabIndex = 0;
            this.Tervehdys_Label.Text = "Tervetuloa tietovisan pariin!\r\nKirjoita alla olevaan tekstilaatikkoon nimesi, val" +
    "itse\r\nliukuvalitsimella haluamasi pelin pituus ja paina\r\n\'Aloita\' -painiketta al" +
    "oittaaksesi pelin.\r\n\r\nOnnea matkaan!";
            this.Tervehdys_Label.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Valitsin
            // 
            this.Valitsin.Location = new System.Drawing.Point(117, 219);
            this.Valitsin.Minimum = 1;
            this.Valitsin.Name = "Valitsin";
            this.Valitsin.Size = new System.Drawing.Size(190, 45);
            this.Valitsin.TabIndex = 2;
            this.Valitsin.Value = 1;
            this.Valitsin.ValueChanged += new System.EventHandler(this.trackBar1_ValueChanged);
            // 
            // Aloitus_Nappi
            // 
            this.Aloitus_Nappi.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Aloitus_Nappi.Location = new System.Drawing.Point(152, 325);
            this.Aloitus_Nappi.Name = "Aloitus_Nappi";
            this.Aloitus_Nappi.Size = new System.Drawing.Size(120, 31);
            this.Aloitus_Nappi.TabIndex = 3;
            this.Aloitus_Nappi.Text = "&Aloita";
            this.Aloitus_Nappi.UseVisualStyleBackColor = true;
            this.Aloitus_Nappi.Click += new System.EventHandler(this.Aloitus_Nappi_Click);
            // 
            // nimi_boxi
            // 
            this.nimi_boxi.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.nimi_boxi.Location = new System.Drawing.Point(117, 173);
            this.nimi_boxi.Name = "nimi_boxi";
            this.nimi_boxi.Size = new System.Drawing.Size(190, 29);
            this.nimi_boxi.TabIndex = 1;
            this.nimi_boxi.TextAlign = System.Windows.Forms.HorizontalAlignment.Center;
            // 
            // Montako_Label
            // 
            this.Montako_Label.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Montako_Label.Location = new System.Drawing.Point(117, 267);
            this.Montako_Label.Name = "Montako_Label";
            this.Montako_Label.Size = new System.Drawing.Size(190, 20);
            this.Montako_Label.TabIndex = 4;
            this.Montako_Label.Text = "Kysymysten määrä: 1";
            // 
            // Aloitusikkuna
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(424, 367);
            this.Controls.Add(this.Montako_Label);
            this.Controls.Add(this.nimi_boxi);
            this.Controls.Add(this.Aloitus_Nappi);
            this.Controls.Add(this.Valitsin);
            this.Controls.Add(this.Tervehdys_Label);
            this.MaximumSize = new System.Drawing.Size(440, 405);
            this.MinimumSize = new System.Drawing.Size(440, 405);
            this.Name = "Aloitusikkuna";
            this.Text = "Tietovisa";
            ((System.ComponentModel.ISupportInitialize)(this.Valitsin)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label Tervehdys_Label;
        private System.Windows.Forms.TrackBar Valitsin;
        private System.Windows.Forms.Button Aloitus_Nappi;
        private System.Windows.Forms.TextBox nimi_boxi;
        private System.Windows.Forms.Label Montako_Label;
    }
}

