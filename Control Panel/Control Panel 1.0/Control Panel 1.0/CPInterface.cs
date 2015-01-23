using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Diagnostics;

namespace Control_Panel_1._0
{
    public partial class CPInterface : Form
    {
        public CPInterface()
        {
            InitializeComponent();
        }

        private void goBTN_Click(object sender, EventArgs e)
        {
            //Connect/Excecute
            Process.Start("pythonw.exe", "controlpanel_client.py "+PortTB.Text+" "+commandTB.Text);
            //change to python.exe
        }

        private void label4_Click(object sender, EventArgs e)
        {

        }

        private void securitySystemToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }
    }
}
