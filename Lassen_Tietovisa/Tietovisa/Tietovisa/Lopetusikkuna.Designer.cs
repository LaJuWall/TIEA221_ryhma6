namespace Tietovisa
{
    partial class Lopetusikkuna
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
            this.Otsikko_Label = new System.Windows.Forms.Label();
            this.Alusta_Nappi = new System.Windows.Forms.Button();
            this.Sulje_Nappi = new System.Windows.Forms.Button();
            this.Tulos_label = new System.Windows.Forms.Label();
            this.Selitys_Label = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // Otsikko_Label
            // 
            this.Otsikko_Label.Font = new System.Drawing.Font("Microsoft Sans Serif", 18F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Otsikko_Label.Location = new System.Drawing.Point(0, 9);
            this.Otsikko_Label.Name = "Otsikko_Label";
            this.Otsikko_Label.Size = new System.Drawing.Size(582, 52);
            this.Otsikko_Label.TabIndex = 0;
            this.Otsikko_Label.Text = "Peli on päättynyt!\r\n";
            this.Otsikko_Label.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Alusta_Nappi
            // 
            this.Alusta_Nappi.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Alusta_Nappi.Location = new System.Drawing.Point(91, 175);
            this.Alusta_Nappi.Name = "Alusta_Nappi";
            this.Alusta_Nappi.Size = new System.Drawing.Size(110, 40);
            this.Alusta_Nappi.TabIndex = 1;
            this.Alusta_Nappi.Text = "&Aloita alusta";
            this.Alusta_Nappi.UseVisualStyleBackColor = true;
            this.Alusta_Nappi.Click += new System.EventHandler(this.Alusta_Nappi_Click);
            // 
            // Sulje_Nappi
            // 
            this.Sulje_Nappi.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Sulje_Nappi.Location = new System.Drawing.Point(383, 175);
            this.Sulje_Nappi.Name = "Sulje_Nappi";
            this.Sulje_Nappi.Size = new System.Drawing.Size(110, 40);
            this.Sulje_Nappi.TabIndex = 2;
            this.Sulje_Nappi.Text = "&Sulje";
            this.Sulje_Nappi.UseVisualStyleBackColor = true;
            this.Sulje_Nappi.Click += new System.EventHandler(this.Sulje_Nappi_Click);
            // 
            // Tulos_label
            // 
            this.Tulos_label.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Tulos_label.Location = new System.Drawing.Point(0, 56);
            this.Tulos_label.Name = "Tulos_label";
            this.Tulos_label.Size = new System.Drawing.Size(582, 23);
            this.Tulos_label.TabIndex = 3;
            this.Tulos_label.Text = "Vastasit oiken X kysymykseen!";
            this.Tulos_label.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Selitys_Label
            // 
            this.Selitys_Label.Font = new System.Drawing.Font("Microsoft Sans Serif", 14.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Selitys_Label.Location = new System.Drawing.Point(32, 102);
            this.Selitys_Label.Name = "Selitys_Label";
            this.Selitys_Label.Size = new System.Drawing.Size(520, 60);
            this.Selitys_Label.TabIndex = 4;
            this.Selitys_Label.Text = "Jos tahdot pelata uuden pelin, paina \"Aloita alusta\" -nappulaa\r\nMikäli tahdot sul" +
    "kea pelin, paina \"sulje\" -nappulaa.";
            this.Selitys_Label.TextAlign = System.Drawing.ContentAlignment.MiddleCenter;
            // 
            // Lopetusikkuna
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(584, 241);
            this.Controls.Add(this.Selitys_Label);
            this.Controls.Add(this.Tulos_label);
            this.Controls.Add(this.Sulje_Nappi);
            this.Controls.Add(this.Alusta_Nappi);
            this.Controls.Add(this.Otsikko_Label);
            this.MaximumSize = new System.Drawing.Size(600, 279);
            this.MinimumSize = new System.Drawing.Size(600, 279);
            this.Name = "Lopetusikkuna";
            this.Text = "Tietovisa";
            this.FormClosed += new System.Windows.Forms.FormClosedEventHandler(this.Lopetusikkuna_FormClosed);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label Otsikko_Label;
        private System.Windows.Forms.Button Alusta_Nappi;
        private System.Windows.Forms.Button Sulje_Nappi;
        private System.Windows.Forms.Label Tulos_label;
        private System.Windows.Forms.Label Selitys_Label;
    }
}