namespace Tietovisa
{
    partial class Ohjeistus
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Ohjeistus));
            this.ohjeistus_Label = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // ohjeistus_Label
            // 
            this.ohjeistus_Label.AutoSize = true;
            this.ohjeistus_Label.Font = new System.Drawing.Font("Microsoft Sans Serif", 11.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ohjeistus_Label.Location = new System.Drawing.Point(1, 1);
            this.ohjeistus_Label.Name = "ohjeistus_Label";
            this.ohjeistus_Label.Size = new System.Drawing.Size(514, 1548);
            this.ohjeistus_Label.TabIndex = 0;
            this.ohjeistus_Label.Text = resources.GetString("ohjeistus_Label.Text");
            // 
            // Ohjeistus
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.AutoScroll = true;
            this.BackColor = System.Drawing.SystemColors.Info;
            this.ClientSize = new System.Drawing.Size(539, 502);
            this.Controls.Add(this.ohjeistus_Label);
            this.MaximumSize = new System.Drawing.Size(555, 540);
            this.MinimumSize = new System.Drawing.Size(555, 540);
            this.Name = "Ohjeistus";
            this.Text = "Tietovisa - Ohje";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label ohjeistus_Label;
    }
}