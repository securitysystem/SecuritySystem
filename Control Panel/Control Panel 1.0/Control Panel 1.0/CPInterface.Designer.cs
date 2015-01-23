namespace Control_Panel_1._0
{
    partial class CPInterface
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
            this.label1 = new System.Windows.Forms.Label();
            this.menuStrip1 = new System.Windows.Forms.MenuStrip();
            this.securitySystemToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.controlPanelToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.optionsToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.helpToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.aboutToolStripMenuItem = new System.Windows.Forms.ToolStripMenuItem();
            this.PortTB = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.goBTN = new System.Windows.Forms.Button();
            this.commandTB = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.webBrowser1 = new System.Windows.Forms.WebBrowser();
            this.menuStrip1.SuspendLayout();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Lato", 15.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(169, 24);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(397, 25);
            this.label1.TabIndex = 0;
            this.label1.Text = "Security System - Control Panel Interface";
            // 
            // menuStrip1
            // 
            this.menuStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.securitySystemToolStripMenuItem,
            this.controlPanelToolStripMenuItem,
            this.optionsToolStripMenuItem,
            this.helpToolStripMenuItem,
            this.aboutToolStripMenuItem});
            this.menuStrip1.Location = new System.Drawing.Point(0, 0);
            this.menuStrip1.Name = "menuStrip1";
            this.menuStrip1.Size = new System.Drawing.Size(742, 24);
            this.menuStrip1.TabIndex = 1;
            this.menuStrip1.Text = "menuStrip1";
            // 
            // securitySystemToolStripMenuItem
            // 
            this.securitySystemToolStripMenuItem.Name = "securitySystemToolStripMenuItem";
            this.securitySystemToolStripMenuItem.Size = new System.Drawing.Size(102, 20);
            this.securitySystemToolStripMenuItem.Text = "Security System";
            this.securitySystemToolStripMenuItem.Click += new System.EventHandler(this.securitySystemToolStripMenuItem_Click);
            // 
            // controlPanelToolStripMenuItem
            // 
            this.controlPanelToolStripMenuItem.Name = "controlPanelToolStripMenuItem";
            this.controlPanelToolStripMenuItem.Size = new System.Drawing.Size(91, 20);
            this.controlPanelToolStripMenuItem.Text = "Control Panel";
            // 
            // optionsToolStripMenuItem
            // 
            this.optionsToolStripMenuItem.Name = "optionsToolStripMenuItem";
            this.optionsToolStripMenuItem.Size = new System.Drawing.Size(61, 20);
            this.optionsToolStripMenuItem.Text = "Options";
            // 
            // helpToolStripMenuItem
            // 
            this.helpToolStripMenuItem.Name = "helpToolStripMenuItem";
            this.helpToolStripMenuItem.Size = new System.Drawing.Size(44, 20);
            this.helpToolStripMenuItem.Text = "Help";
            // 
            // aboutToolStripMenuItem
            // 
            this.aboutToolStripMenuItem.Name = "aboutToolStripMenuItem";
            this.aboutToolStripMenuItem.Size = new System.Drawing.Size(52, 20);
            this.aboutToolStripMenuItem.Text = "About";
            // 
            // PortTB
            // 
            this.PortTB.Location = new System.Drawing.Point(355, 64);
            this.PortTB.Name = "PortTB";
            this.PortTB.Size = new System.Drawing.Size(93, 27);
            this.PortTB.TabIndex = 2;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(24, 67);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(261, 19);
            this.label2.TabIndex = 3;
            this.label2.Text = "Security System Control Panel Port";
            // 
            // goBTN
            // 
            this.goBTN.Location = new System.Drawing.Point(174, 204);
            this.goBTN.Name = "goBTN";
            this.goBTN.Size = new System.Drawing.Size(304, 55);
            this.goBTN.TabIndex = 4;
            this.goBTN.Text = "Connect/Execute";
            this.goBTN.UseVisualStyleBackColor = true;
            this.goBTN.Click += new System.EventHandler(this.goBTN_Click);
            // 
            // commandTB
            // 
            this.commandTB.Location = new System.Drawing.Point(28, 140);
            this.commandTB.Name = "commandTB";
            this.commandTB.Size = new System.Drawing.Size(684, 27);
            this.commandTB.TabIndex = 5;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(24, 118);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(462, 19);
            this.label3.TabIndex = 6;
            this.label3.Text = "Command to Excecute (ex. <your password>$send_panic_email)";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(28, 277);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(222, 19);
            this.label4.TabIndex = 7;
            this.label4.Text = "Current Status [Click to View]";
            this.label4.Click += new System.EventHandler(this.label4_Click);
            // 
            // webBrowser1
            // 
            this.webBrowser1.Location = new System.Drawing.Point(32, 300);
            this.webBrowser1.MinimumSize = new System.Drawing.Size(20, 20);
            this.webBrowser1.Name = "webBrowser1";
            this.webBrowser1.Size = new System.Drawing.Size(698, 189);
            this.webBrowser1.TabIndex = 8;
            // 
            // CPInterface
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 19F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(742, 504);
            this.Controls.Add(this.webBrowser1);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.commandTB);
            this.Controls.Add(this.goBTN);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.PortTB);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.menuStrip1);
            this.Font = new System.Drawing.Font("Lato Semibold", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.MainMenuStrip = this.menuStrip1;
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "CPInterface";
            this.Text = "Security System Control Panel Interface";
            this.menuStrip1.ResumeLayout(false);
            this.menuStrip1.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.MenuStrip menuStrip1;
        private System.Windows.Forms.ToolStripMenuItem securitySystemToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem controlPanelToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem optionsToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem helpToolStripMenuItem;
        private System.Windows.Forms.ToolStripMenuItem aboutToolStripMenuItem;
        private System.Windows.Forms.TextBox PortTB;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Button goBTN;
        private System.Windows.Forms.TextBox commandTB;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.WebBrowser webBrowser1;
    }
}

