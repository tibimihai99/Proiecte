using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;


namespace Joc_de_memorie
{
    public partial class Form1 : Form
    {
        Random random = new Random();

        List<string> imagini = new List<string>()
        {
            "1", "1", "2", "2", "3", "3", "4", "4",
            "5", "5", "6", "6", "7", "7", "8", "8"
        };

        Label clickp, clicks;

        public Form1()
        {
            InitializeComponent();
            Numerechenar();
        }

        private void Numerechenar()
        {
            Label label;
            int randomNR, i;

            for(i=0;i<tableLayoutPanel1.Controls.Count;i++)
            {
                if (tableLayoutPanel1.Controls[i] is Label)
                    label = (Label)tableLayoutPanel1.Controls[i];
                else
                    continue;

                randomNR = random.Next(0, imagini.Count);
                label.Text = imagini[randomNR];

                imagini.RemoveAt(randomNR);


            }


        }

        public void label_Click(object sender, EventArgs e)
        {
         
            if (clickp != null && clicks != null)
                return;

            Label clickimagine = sender as Label;
            if (clickimagine == null)
                return;
            if (clickimagine.ForeColor == Color.Black)
                return;
            if(clickp == null)
            {
                clickp = clickimagine;
                clickp.ForeColor = Color.Black;
                return;
            }
            clicks = clickimagine;
            clicks.ForeColor = Color.Black;

            Castigator();

            if(clickp.Text==clicks.Text)
            {
                clickp = null;
                clicks = null;
            }
            else
            timer1.Start();

            
        }


        private void Castigator()
        {
            Label imagine;
            int i, nr = 0;
            for (i = 0; i < tableLayoutPanel1.Controls.Count; i++)
            {
                imagine = tableLayoutPanel1.Controls[i] as Label;

              


                if (imagine != null && imagine.ForeColor == imagine.BackColor)
                    nr++;
                    return;
            }

            


            MessageBox.Show("Ai completat jocul! Felicitari.Ai reusit sa termini jocul din "+nr+" incercari");

            Close();

        }

        private void timer1_Tick(object sender, EventArgs e)
        {
            timer1.Stop();
            clickp.ForeColor = clickp.BackColor;
            clicks.ForeColor = clicks.BackColor;
            clickp = null;
            clicks = null;
        }

        private void tableLayoutPanel1_Paint(object sender, PaintEventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }
    }

}





