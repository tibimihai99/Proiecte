using System;
using System.Drawing;
using System.Windows.Forms;
using LibrarieModele;
using NivelAccesDate;
using System.Collections.Generic;

namespace InterfataUtilizator_WindowsForms
{
    public partial class FormularPacient : Form
    {
        IStocareData adminPacienti;
        List<string> doctoriSelectati = new List<string>();

        public FormularPacient()
        {
            InitializeComponent();
            this.BackgroundImage = Properties.Resources.descărcare;
            Timer t = new Timer();
            t.Interval = 2000;
            t.Tick += new EventHandler(ChangeImage);
            t.Start();
            adminPacienti = StocareFactory.GetAdministratorStocare();
        }

        private void ChangeImage(object sender, EventArgs e)
        {
            List<Bitmap> b1 = new List<Bitmap>();
            b1.Add(Properties.Resources.descărcare);
            b1.Add(Properties.Resources.descărcare2);
            b1.Add(Properties.Resources.descarcare3);
            b1.Add(Properties.Resources.descarcare4);
            b1.Add(Properties.Resources.descacare5);
            int index = DateTime.Now.Second % b1.Count;
            this.BackgroundImage = b1[index];
        }

        private void btnAdauga_Click(object sender, EventArgs e)
        {
            if (!DateIntrareValide())
            {
                lblDoctori.ForeColor = Color.Red;
                lblCodulcamerei.ForeColor = Color.Red;

                return;
            }

            Pacient p = new Pacient(txtNume.Text, txtPrenume.Text);
            p.SetCamere(txtNumarulcamerei.Text);

            //set afectiuni
            //verificare radioButton selectat
            Afectiuni? afectiuneSelectata = GetAfectiuneSelectat();
            if (afectiuneSelectata.HasValue)
            {
                p.Doctori = doctoriSelectati;
            }

            //set Doctori
            p.Doctori = new List<string>();
            p.Doctori.AddRange(doctoriSelectati);

            adminPacienti.AddPacient(p);
            lblMesaj.Text = "Studentul a fost adaugat";

            //resetarea controalelor pentru a introduce datele unui pacient nou
            ResetareControale();
            btnAfiseaza.PerformClick();
        }

        private bool DateIntrareValide()
        {
            int[] cemere = Camere.ExtrageCamereDinSir(txtNumarulcamerei.Text);
            if (doctoriSelectati.Count !=cemere.Length)
            {
                return false;
            }

            return true;
        }

        private void btnAfiseaza_Click(object sender, EventArgs e)
        {
            lstPacienti.Items.Clear();
            var antetTabel = String.Format("{0,-5}{1,-35}{2,20}{3,10}\n", "Id", "Nume Prenume", "Afectiune", "Doctor","Nr camera");
            lstPacienti.Items.Add(antetTabel);

            List<Pacient> pacienti = adminPacienti.GetPacienti();
            foreach (Pacient p in pacienti)
            {
                var linieTabel = String.Format("{0,-5}{1,-35}{2,20}{3,10}\n", p.IdPacient, p.NumeComplet, p.Afectiuni.ToString(), p.Doctori.ToString(),p.Media.ToString());
                lstPacienti.Items.Add(linieTabel);
            }
        }

        private void btnCauta_Click(object sender, EventArgs e)
        {
        }

        private void btnModifica_Click(object sender, EventArgs e)
        {
            if (!DateIntrareValide())
            {
                lblDoctori.ForeColor = Color.Red;
                lblCodulcamerei.ForeColor = Color.Red;

                return;
            }
            Pacient patc = adminPacienti.GetPacient(lstPacienti.SelectedIndex);
            patc.Nume = txtNume.Text;
            patc.Prenume = txtPrenume.Text;
            adminPacienti.UpdatePacient(patc);
            ResetareControale();
            lblMesaj.Text = "Pacientul a fost actualizat";
            btnAfiseaza.PerformClick();
        }

        private void ckbDiscipline_CheckedChanged(object sender, EventArgs e)
        {
            CheckBox checkBoxControl = sender as CheckBox; //operator 'as'
            //sau
            //CheckBox checkBoxControl = (CheckBox)sender;  //operator cast

            string doctorSelectat = checkBoxControl.Text;

            //verificare daca checkbox-ul asupra caruia s-a actionat este selectat
            if (checkBoxControl.Checked == true)
                doctoriSelectati.Add(doctorSelectat);
            else
                doctoriSelectati.Remove(doctorSelectat);
        }

        private void ResetareControale()
        {
            txtNume.Text = txtPrenume.Text = txtNumarulcamerei.Text = string.Empty;
            rdbPietrelafiere.Checked = false;
            rdbManarupta.Checked = false;
            rdbGastrita.Checked = false;
            rdbOtita.Checked = false;
            rdbScoliozasevera.Checked = false;
            ckbIonescuMaria.Checked = false;
            ckbMotocVasile.Checked = false;
            ckbPapucAna.Checked = false;
            ckbMorozanGabriela.Checked = false;
            ckbMirciucConstantin.Checked = false;
            ckbValeriuIon.Checked = false;
            doctoriSelectati.Clear();
            lblMesaj.Text = string.Empty;
        }

        private Afectiuni? GetAfectiuneSelectat()
        {
            if (rdbPietrelafiere.Checked)
                return Afectiuni.Pietrelafiere;
            if (rdbManarupta.Checked)
                return Afectiuni.Manarupta;
            if (rdbGastrita.Checked)
                return Afectiuni.Gastrita;
            if (rdbOtita.Checked)
                return Afectiuni.Otita;
            if (rdbScoliozasevera.Checked)
                return Afectiuni.Scoliozasevera;

            return null;
        }

        private void lstPacienti_SelectedIndexChanged(object sender, EventArgs e)
        {
            ResetareControale();
            Pacient patc = adminPacienti.GetPacient(lstPacienti.SelectedIndex);
            txtNume.Text = patc.Nume;
            txtPrenume.Text = patc.Prenume;
        }

        private void btnStudPromovati_Click(object sender, EventArgs e)
        {
            //reset continut control DataGridView
            dataGridPacienti.DataSource = null;
            //!!!! Controlul de tip DataGridView are ca sursa de date lista de obiecte de tip Pacient!!!
            dataGridPacienti.DataSource = adminPacienti.GetPacienti();
        }

        private void FormularStudent_Load(object sender, EventArgs e)
        {

        }

        private void dataGridPacienti_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void gpbProgrameStudiu_Enter(object sender, EventArgs e)
        {

        }

        private void lblNume_Click(object sender, EventArgs e)
        {

        }
    }
}
