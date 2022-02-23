using System;
using System.Drawing;
using System.Windows.Forms;
using LibrarieModele;
using NivelAccesDate;
using System.Collections.Generic;

namespace InterfataUtilizator_WindowsForms
{
    public partial class FormularStudent : Form
    {
        IStocareData adminStudenti;
        List<string> disciplineSelectate = new List<string>();

        public FormularStudent()
        {
            InitializeComponent();
            adminStudenti = StocareFactory.GetAdministratorStocare();
        }

        private void btnAdauga_Click(object sender, EventArgs e)
        {
            if (!DateIntrareValide())
            {
                lblDiscipline.ForeColor = Color.Red;
                lblNote.ForeColor = Color.Red;

                return;
            }

            Student s = new Student(txtNume.Text, txtPrenume.Text);
            s.SetNote(txtNote.Text);

            //set program studiu
            //verificare radioButton selectat
            ProgramStudiu? specializareSelectata = GetProgramStudiuSelectat();
            if (specializareSelectata.HasValue)
            {
                s.Specializare = specializareSelectata.Value;
            }

            //set Discipline
            s.Discipline = new List<string>();
            s.Discipline.AddRange(disciplineSelectate);

            adminStudenti.AddStudent(s);
            lblMesaj.Text = "Studentul a fost adaugat";

            //resetarea controalelor pentru a introduce datele unui student nou
            ResetareControale();
            btnAfiseaza.PerformClick();
        }

        private bool DateIntrareValide()
        {
            int[] note = Note.ExtrageNoteDinSir(txtNote.Text);
            if (disciplineSelectate.Count != note.Length)
            {
                return false;
            }

            return true;
        }

        private void btnAfiseaza_Click(object sender, EventArgs e)
        {
            lstStudenti.Items.Clear();
            var antetTabel = String.Format("{0,-5}{1,-35}{2,20}{3,10}\n", "Id", "Nume Prenume", "ProgramStudiu", "Medie");
            lstStudenti.Items.Add(antetTabel);

            List<Student> studenti = adminStudenti.GetStudenti();
            foreach (Student s in studenti)
            {
                var linieTabel = String.Format("{0,-5}{1,-35}{2,20}{3,10}\n", s.IdStudent, s.NumeComplet, s.Specializare.ToString(), s.Media.ToString());
                lstStudenti.Items.Add(linieTabel);
            }
        }

        private void btnCauta_Click(object sender, EventArgs e)
        {
        }

        private void btnModifica_Click(object sender, EventArgs e)
        {
            if (!DateIntrareValide())
            {
                lblDiscipline.ForeColor = Color.Red;
                lblNote.ForeColor = Color.Red;

                return;
            }
            Student stud = adminStudenti.GetStudent(lstStudenti.SelectedIndex);
            stud.Nume = txtNume.Text;
            stud.Prenume = txtPrenume.Text;
            adminStudenti.UpdateStudent(stud);
            ResetareControale();
            lblMesaj.Text = "Studentul a fost actualizat";
            btnAfiseaza.PerformClick();
        }

        private void ckbDiscipline_CheckedChanged(object sender, EventArgs e)
        {
            CheckBox checkBoxControl = sender as CheckBox; //operator 'as'
            //sau
            //CheckBox checkBoxControl = (CheckBox)sender;  //operator cast

            string disciplinaSelectata = checkBoxControl.Text;

            //verificare daca checkbox-ul asupra caruia s-a actionat este selectat
            if (checkBoxControl.Checked == true)
                disciplineSelectate.Add(disciplinaSelectata);
            else
                disciplineSelectate.Remove(disciplinaSelectata);
        }

        private void ResetareControale()
        {
            txtNume.Text = txtPrenume.Text = txtNote.Text = string.Empty;
            rdbCalculatoare.Checked = false;
            rdbAutomatica.Checked = false;
            rdbElectronica.Checked = false;
            rdbElectrotehnica.Checked = false;
            rdbInginerieE.Checked = false;
            ckbPCLP.Checked = false;
            ckbPOO.Checked = false;
            ckbPIU.Checked = false;
            ckbDEEA2.Checked = false;
            ckbED.Checked = false;
            ckbMEST.Checked = false;
            disciplineSelectate.Clear();
            lblMesaj.Text = string.Empty;
        }

        private ProgramStudiu? GetProgramStudiuSelectat()
        {
            if (rdbCalculatoare.Checked)
                return ProgramStudiu.Calculatoare;
            if (rdbAutomatica.Checked)
                return ProgramStudiu.Automatica;
            if (rdbElectronica.Checked)
                return ProgramStudiu.Electronica;
            if (rdbElectrotehnica.Checked)
                return ProgramStudiu.Electronica;
            if (rdbInginerieE.Checked)
                return ProgramStudiu.InginerieEconomica;

            return null;
        }

        private void lstStudenti_SelectedIndexChanged(object sender, EventArgs e)
        {
            ResetareControale();
            Student stud = adminStudenti.GetStudent(lstStudenti.SelectedIndex);
            txtNume.Text = stud.Nume;
            txtPrenume.Text = stud.Prenume;
        }

        private void btnStudPromovati_Click(object sender, EventArgs e)
        {
            //reset continut control DataGridView
            dataGridStudenti.DataSource = null;
            //!!!! Controlul de tip DataGridView are ca sursa de date lista de obiecte de tip Student!!!
            dataGridStudenti.DataSource = adminStudenti.GetStudenti();
        }

        private void FormularStudent_Load(object sender, EventArgs e)
        {

        }

        private void dataGridStudenti_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
