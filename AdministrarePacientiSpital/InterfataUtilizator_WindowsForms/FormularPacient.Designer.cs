
namespace InterfataUtilizator_WindowsForms
{
    partial class FormularPacient
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
            this.lblNume = new System.Windows.Forms.Label();
            this.lblPrenume = new System.Windows.Forms.Label();
            this.lblCodulcamerei = new System.Windows.Forms.Label();
            this.btnAdauga = new System.Windows.Forms.Button();
            this.txtNume = new System.Windows.Forms.TextBox();
            this.txtPrenume = new System.Windows.Forms.TextBox();
            this.txtNumarulcamerei = new System.Windows.Forms.TextBox();
            this.btnAfiseaza = new System.Windows.Forms.Button();
            this.btnCauta = new System.Windows.Forms.Button();
            this.lblMesaj = new System.Windows.Forms.Label();
            this.btnModifica = new System.Windows.Forms.Button();
            this.gpbAfectiuni = new System.Windows.Forms.GroupBox();
            this.rdbScoliozasevera = new System.Windows.Forms.RadioButton();
            this.rdbGastrita = new System.Windows.Forms.RadioButton();
            this.rdbOtita = new System.Windows.Forms.RadioButton();
            this.rdbPietrelafiere = new System.Windows.Forms.RadioButton();
            this.rdbManarupta = new System.Windows.Forms.RadioButton();
            this.lblAfectiune = new System.Windows.Forms.Label();
            this.ckbPapucAna = new System.Windows.Forms.CheckBox();
            this.ckbMotocVasile = new System.Windows.Forms.CheckBox();
            this.ckbIonescuMaria = new System.Windows.Forms.CheckBox();
            this.lblDoctori = new System.Windows.Forms.Label();
            this.ckbMorozanGabriela = new System.Windows.Forms.CheckBox();
            this.ckbMirciucConstantin = new System.Windows.Forms.CheckBox();
            this.ckbValeriuIon = new System.Windows.Forms.CheckBox();
            this.gpbDoctori = new System.Windows.Forms.GroupBox();
            this.lstPacienti = new System.Windows.Forms.ListBox();
            this.dataGridPacienti = new System.Windows.Forms.DataGridView();
            this.btnPacientiVindecati = new System.Windows.Forms.Button();
            this.gpbAfectiuni.SuspendLayout();
            this.gpbDoctori.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridPacienti)).BeginInit();
            this.SuspendLayout();
            // 
            // lblNume
            // 
            this.lblNume.AutoSize = true;
            this.lblNume.Location = new System.Drawing.Point(33, 27);
            this.lblNume.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblNume.Name = "lblNume";
            this.lblNume.Size = new System.Drawing.Size(35, 13);
            this.lblNume.TabIndex = 0;
            this.lblNume.Text = "Nume";
            this.lblNume.Click += new System.EventHandler(this.lblNume_Click);
            // 
            // lblPrenume
            // 
            this.lblPrenume.AutoSize = true;
            this.lblPrenume.Location = new System.Drawing.Point(27, 56);
            this.lblPrenume.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblPrenume.Name = "lblPrenume";
            this.lblPrenume.Size = new System.Drawing.Size(49, 13);
            this.lblPrenume.TabIndex = 1;
            this.lblPrenume.Text = "Prenume";
            // 
            // lblCodulcamerei
            // 
            this.lblCodulcamerei.AutoSize = true;
            this.lblCodulcamerei.Location = new System.Drawing.Point(2, 256);
            this.lblCodulcamerei.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblCodulcamerei.Name = "lblCodulcamerei";
            this.lblCodulcamerei.Size = new System.Drawing.Size(74, 13);
            this.lblCodulcamerei.TabIndex = 2;
            this.lblCodulcamerei.Text = "Codul camerei";
            // 
            // btnAdauga
            // 
            this.btnAdauga.Location = new System.Drawing.Point(97, 295);
            this.btnAdauga.Margin = new System.Windows.Forms.Padding(2);
            this.btnAdauga.Name = "btnAdauga";
            this.btnAdauga.Size = new System.Drawing.Size(93, 23);
            this.btnAdauga.TabIndex = 3;
            this.btnAdauga.Text = "Adauga";
            this.btnAdauga.UseVisualStyleBackColor = true;
            this.btnAdauga.Click += new System.EventHandler(this.btnAdauga_Click);
            // 
            // txtNume
            // 
            this.txtNume.Location = new System.Drawing.Point(97, 24);
            this.txtNume.Margin = new System.Windows.Forms.Padding(2);
            this.txtNume.Name = "txtNume";
            this.txtNume.Size = new System.Drawing.Size(209, 20);
            this.txtNume.TabIndex = 4;
            // 
            // txtPrenume
            // 
            this.txtPrenume.Location = new System.Drawing.Point(97, 53);
            this.txtPrenume.Margin = new System.Windows.Forms.Padding(2);
            this.txtPrenume.Name = "txtPrenume";
            this.txtPrenume.Size = new System.Drawing.Size(209, 20);
            this.txtPrenume.TabIndex = 5;
            // 
            // txtNumarulcamerei
            // 
            this.txtNumarulcamerei.Location = new System.Drawing.Point(97, 253);
            this.txtNumarulcamerei.Margin = new System.Windows.Forms.Padding(2);
            this.txtNumarulcamerei.Name = "txtNumarulcamerei";
            this.txtNumarulcamerei.Size = new System.Drawing.Size(209, 20);
            this.txtNumarulcamerei.TabIndex = 6;
            // 
            // btnAfiseaza
            // 
            this.btnAfiseaza.Location = new System.Drawing.Point(202, 295);
            this.btnAfiseaza.Margin = new System.Windows.Forms.Padding(2);
            this.btnAfiseaza.Name = "btnAfiseaza";
            this.btnAfiseaza.Size = new System.Drawing.Size(104, 23);
            this.btnAfiseaza.TabIndex = 10;
            this.btnAfiseaza.Text = "Afiseaza";
            this.btnAfiseaza.UseVisualStyleBackColor = true;
            this.btnAfiseaza.Click += new System.EventHandler(this.btnAfiseaza_Click);
            // 
            // btnCauta
            // 
            this.btnCauta.Location = new System.Drawing.Point(97, 331);
            this.btnCauta.Margin = new System.Windows.Forms.Padding(2);
            this.btnCauta.Name = "btnCauta";
            this.btnCauta.Size = new System.Drawing.Size(93, 23);
            this.btnCauta.TabIndex = 12;
            this.btnCauta.Text = "Cauta";
            this.btnCauta.UseVisualStyleBackColor = true;
            this.btnCauta.Click += new System.EventHandler(this.btnCauta_Click);
            // 
            // lblMesaj
            // 
            this.lblMesaj.AutoSize = true;
            this.lblMesaj.Location = new System.Drawing.Point(88, 360);
            this.lblMesaj.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblMesaj.Name = "lblMesaj";
            this.lblMesaj.Size = new System.Drawing.Size(0, 13);
            this.lblMesaj.TabIndex = 13;
            // 
            // btnModifica
            // 
            this.btnModifica.Location = new System.Drawing.Point(202, 331);
            this.btnModifica.Margin = new System.Windows.Forms.Padding(2);
            this.btnModifica.Name = "btnModifica";
            this.btnModifica.Size = new System.Drawing.Size(104, 23);
            this.btnModifica.TabIndex = 14;
            this.btnModifica.Text = "Modifica";
            this.btnModifica.UseVisualStyleBackColor = true;
            this.btnModifica.Click += new System.EventHandler(this.btnModifica_Click);
            // 
            // gpbAfectiuni
            // 
            this.gpbAfectiuni.Controls.Add(this.rdbScoliozasevera);
            this.gpbAfectiuni.Controls.Add(this.rdbGastrita);
            this.gpbAfectiuni.Controls.Add(this.rdbOtita);
            this.gpbAfectiuni.Controls.Add(this.rdbPietrelafiere);
            this.gpbAfectiuni.Controls.Add(this.rdbManarupta);
            this.gpbAfectiuni.Location = new System.Drawing.Point(97, 87);
            this.gpbAfectiuni.Name = "gpbAfectiuni";
            this.gpbAfectiuni.Size = new System.Drawing.Size(208, 100);
            this.gpbAfectiuni.TabIndex = 18;
            this.gpbAfectiuni.TabStop = false;
            this.gpbAfectiuni.Enter += new System.EventHandler(this.gpbProgrameStudiu_Enter);
            // 
            // rdbScoliozasevera
            // 
            this.rdbScoliozasevera.AutoSize = true;
            this.rdbScoliozasevera.Location = new System.Drawing.Point(15, 56);
            this.rdbScoliozasevera.Name = "rdbScoliozasevera";
            this.rdbScoliozasevera.Size = new System.Drawing.Size(100, 17);
            this.rdbScoliozasevera.TabIndex = 12;
            this.rdbScoliozasevera.TabStop = true;
            this.rdbScoliozasevera.Text = "Scolioza severa";
            this.rdbScoliozasevera.UseVisualStyleBackColor = true;
            // 
            // rdbGastrita
            // 
            this.rdbGastrita.AutoSize = true;
            this.rdbGastrita.Location = new System.Drawing.Point(15, 32);
            this.rdbGastrita.Name = "rdbGastrita";
            this.rdbGastrita.Size = new System.Drawing.Size(61, 17);
            this.rdbGastrita.TabIndex = 10;
            this.rdbGastrita.TabStop = true;
            this.rdbGastrita.Text = "Gastrita";
            this.rdbGastrita.UseVisualStyleBackColor = true;
            // 
            // rdbOtita
            // 
            this.rdbOtita.AutoSize = true;
            this.rdbOtita.Location = new System.Drawing.Point(105, 32);
            this.rdbOtita.Name = "rdbOtita";
            this.rdbOtita.Size = new System.Drawing.Size(47, 17);
            this.rdbOtita.TabIndex = 11;
            this.rdbOtita.TabStop = true;
            this.rdbOtita.Text = "Otita";
            this.rdbOtita.UseVisualStyleBackColor = true;
            // 
            // rdbPietrelafiere
            // 
            this.rdbPietrelafiere.AutoSize = true;
            this.rdbPietrelafiere.Location = new System.Drawing.Point(15, 9);
            this.rdbPietrelafiere.Name = "rdbPietrelafiere";
            this.rdbPietrelafiere.Size = new System.Drawing.Size(86, 17);
            this.rdbPietrelafiere.TabIndex = 8;
            this.rdbPietrelafiere.TabStop = true;
            this.rdbPietrelafiere.Text = "Pietre la fiere";
            this.rdbPietrelafiere.UseVisualStyleBackColor = true;
            // 
            // rdbManarupta
            // 
            this.rdbManarupta.AutoSize = true;
            this.rdbManarupta.Location = new System.Drawing.Point(105, 9);
            this.rdbManarupta.Name = "rdbManarupta";
            this.rdbManarupta.Size = new System.Drawing.Size(79, 17);
            this.rdbManarupta.TabIndex = 9;
            this.rdbManarupta.TabStop = true;
            this.rdbManarupta.Text = "Mana rupta";
            this.rdbManarupta.UseVisualStyleBackColor = true;
            // 
            // lblAfectiune
            // 
            this.lblAfectiune.AutoSize = true;
            this.lblAfectiune.Location = new System.Drawing.Point(19, 98);
            this.lblAfectiune.Name = "lblAfectiune";
            this.lblAfectiune.Size = new System.Drawing.Size(52, 13);
            this.lblAfectiune.TabIndex = 17;
            this.lblAfectiune.Text = "Afectiune";
            // 
            // ckbPapucAna
            // 
            this.ckbPapucAna.AutoSize = true;
            this.ckbPapucAna.Location = new System.Drawing.Point(241, 13);
            this.ckbPapucAna.Name = "ckbPapucAna";
            this.ckbPapucAna.Size = new System.Drawing.Size(79, 17);
            this.ckbPapucAna.TabIndex = 22;
            this.ckbPapucAna.Text = "Papuc Ana";
            this.ckbPapucAna.UseVisualStyleBackColor = true;
            this.ckbPapucAna.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbMotocVasile
            // 
            this.ckbMotocVasile.AutoSize = true;
            this.ckbMotocVasile.Location = new System.Drawing.Point(125, 13);
            this.ckbMotocVasile.Name = "ckbMotocVasile";
            this.ckbMotocVasile.Size = new System.Drawing.Size(87, 17);
            this.ckbMotocVasile.TabIndex = 21;
            this.ckbMotocVasile.Text = "Motoc Vasile";
            this.ckbMotocVasile.UseVisualStyleBackColor = true;
            this.ckbMotocVasile.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbIonescuMaria
            // 
            this.ckbIonescuMaria.AutoSize = true;
            this.ckbIonescuMaria.Location = new System.Drawing.Point(12, 11);
            this.ckbIonescuMaria.Name = "ckbIonescuMaria";
            this.ckbIonescuMaria.Size = new System.Drawing.Size(93, 17);
            this.ckbIonescuMaria.TabIndex = 20;
            this.ckbIonescuMaria.Text = "Ionescu Maria";
            this.ckbIonescuMaria.UseVisualStyleBackColor = true;
            this.ckbIonescuMaria.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // lblDoctori
            // 
            this.lblDoctori.AutoSize = true;
            this.lblDoctori.Location = new System.Drawing.Point(2, 193);
            this.lblDoctori.Name = "lblDoctori";
            this.lblDoctori.Size = new System.Drawing.Size(41, 13);
            this.lblDoctori.TabIndex = 19;
            this.lblDoctori.Text = "Doctori";
            // 
            // ckbMorozanGabriela
            // 
            this.ckbMorozanGabriela.AutoSize = true;
            this.ckbMorozanGabriela.Location = new System.Drawing.Point(12, 35);
            this.ckbMorozanGabriela.Name = "ckbMorozanGabriela";
            this.ckbMorozanGabriela.Size = new System.Drawing.Size(109, 17);
            this.ckbMorozanGabriela.TabIndex = 23;
            this.ckbMorozanGabriela.Text = "Morozan Gabriela";
            this.ckbMorozanGabriela.UseVisualStyleBackColor = true;
            this.ckbMorozanGabriela.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbMirciucConstantin
            // 
            this.ckbMirciucConstantin.AutoSize = true;
            this.ckbMirciucConstantin.Location = new System.Drawing.Point(125, 36);
            this.ckbMirciucConstantin.Name = "ckbMirciucConstantin";
            this.ckbMirciucConstantin.Size = new System.Drawing.Size(113, 17);
            this.ckbMirciucConstantin.TabIndex = 24;
            this.ckbMirciucConstantin.Text = "Mirciuc Constantin";
            this.ckbMirciucConstantin.UseVisualStyleBackColor = true;
            this.ckbMirciucConstantin.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbValeriuIon
            // 
            this.ckbValeriuIon.AutoSize = true;
            this.ckbValeriuIon.Location = new System.Drawing.Point(244, 36);
            this.ckbValeriuIon.Name = "ckbValeriuIon";
            this.ckbValeriuIon.Size = new System.Drawing.Size(76, 17);
            this.ckbValeriuIon.TabIndex = 25;
            this.ckbValeriuIon.Text = "Valeriu Ion";
            this.ckbValeriuIon.UseVisualStyleBackColor = true;
            this.ckbValeriuIon.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // gpbDoctori
            // 
            this.gpbDoctori.Controls.Add(this.ckbValeriuIon);
            this.gpbDoctori.Controls.Add(this.ckbIonescuMaria);
            this.gpbDoctori.Controls.Add(this.ckbMirciucConstantin);
            this.gpbDoctori.Controls.Add(this.ckbMotocVasile);
            this.gpbDoctori.Controls.Add(this.ckbMorozanGabriela);
            this.gpbDoctori.Controls.Add(this.ckbPapucAna);
            this.gpbDoctori.Location = new System.Drawing.Point(42, 193);
            this.gpbDoctori.Margin = new System.Windows.Forms.Padding(2);
            this.gpbDoctori.Name = "gpbDoctori";
            this.gpbDoctori.Padding = new System.Windows.Forms.Padding(2);
            this.gpbDoctori.Size = new System.Drawing.Size(329, 56);
            this.gpbDoctori.TabIndex = 26;
            this.gpbDoctori.TabStop = false;
            // 
            // lstPacienti
            // 
            this.lstPacienti.FormattingEnabled = true;
            this.lstPacienti.Location = new System.Drawing.Point(376, 24);
            this.lstPacienti.Margin = new System.Windows.Forms.Padding(2);
            this.lstPacienti.Name = "lstPacienti";
            this.lstPacienti.Size = new System.Drawing.Size(336, 160);
            this.lstPacienti.TabIndex = 27;
            this.lstPacienti.SelectedIndexChanged += new System.EventHandler(this.lstPacienti_SelectedIndexChanged);
            // 
            // dataGridPacienti
            // 
            this.dataGridPacienti.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridPacienti.Location = new System.Drawing.Point(376, 203);
            this.dataGridPacienti.Name = "dataGridPacienti";
            this.dataGridPacienti.Size = new System.Drawing.Size(335, 115);
            this.dataGridPacienti.TabIndex = 28;
            this.dataGridPacienti.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridPacienti_CellContentClick);
            // 
            // btnPacientiVindecati
            // 
            this.btnPacientiVindecati.Location = new System.Drawing.Point(472, 331);
            this.btnPacientiVindecati.Name = "btnPacientiVindecati";
            this.btnPacientiVindecati.Size = new System.Drawing.Size(147, 23);
            this.btnPacientiVindecati.TabIndex = 29;
            this.btnPacientiVindecati.Text = "Afisare Pacienti Vindecati";
            this.btnPacientiVindecati.UseVisualStyleBackColor = true;
            this.btnPacientiVindecati.Click += new System.EventHandler(this.btnStudPromovati_Click);
            // 
            // FormularPacient
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch;
            this.ClientSize = new System.Drawing.Size(742, 383);
            this.Controls.Add(this.btnPacientiVindecati);
            this.Controls.Add(this.dataGridPacienti);
            this.Controls.Add(this.lstPacienti);
            this.Controls.Add(this.gpbDoctori);
            this.Controls.Add(this.lblDoctori);
            this.Controls.Add(this.gpbAfectiuni);
            this.Controls.Add(this.lblAfectiune);
            this.Controls.Add(this.btnModifica);
            this.Controls.Add(this.lblMesaj);
            this.Controls.Add(this.btnCauta);
            this.Controls.Add(this.btnAfiseaza);
            this.Controls.Add(this.txtNumarulcamerei);
            this.Controls.Add(this.txtPrenume);
            this.Controls.Add(this.txtNume);
            this.Controls.Add(this.btnAdauga);
            this.Controls.Add(this.lblCodulcamerei);
            this.Controls.Add(this.lblPrenume);
            this.Controls.Add(this.lblNume);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "FormularPacient";
            this.Text = "Administrare pacienti";
            this.Load += new System.EventHandler(this.FormularStudent_Load);
            this.gpbAfectiuni.ResumeLayout(false);
            this.gpbAfectiuni.PerformLayout();
            this.gpbDoctori.ResumeLayout(false);
            this.gpbDoctori.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridPacienti)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label lblPrenume;
        private System.Windows.Forms.Label lblCodulcamerei;
        private System.Windows.Forms.Button btnAdauga;
        private System.Windows.Forms.Label lblNume;
        private System.Windows.Forms.TextBox txtNume;
        private System.Windows.Forms.TextBox txtPrenume;
        private System.Windows.Forms.TextBox txtNumarulcamerei;
        private System.Windows.Forms.Button btnAfiseaza;
        private System.Windows.Forms.Button btnCauta;
        private System.Windows.Forms.Label lblMesaj;
        private System.Windows.Forms.Button btnModifica;
        private System.Windows.Forms.GroupBox gpbAfectiuni;
        private System.Windows.Forms.RadioButton rdbPietrelafiere;
        private System.Windows.Forms.RadioButton rdbManarupta;
        private System.Windows.Forms.Label lblAfectiune;
        private System.Windows.Forms.CheckBox ckbPapucAna;
        private System.Windows.Forms.CheckBox ckbMotocVasile;
        private System.Windows.Forms.CheckBox ckbIonescuMaria;
        private System.Windows.Forms.Label lblDoctori;
        private System.Windows.Forms.RadioButton rdbScoliozasevera;
        private System.Windows.Forms.RadioButton rdbGastrita;
        private System.Windows.Forms.RadioButton rdbOtita;
        private System.Windows.Forms.CheckBox ckbMorozanGabriela;
        private System.Windows.Forms.CheckBox ckbMirciucConstantin;
        private System.Windows.Forms.CheckBox ckbValeriuIon;
        private System.Windows.Forms.GroupBox gpbDoctori;
        private System.Windows.Forms.ListBox lstPacienti;
        private System.Windows.Forms.DataGridView dataGridPacienti;
        private System.Windows.Forms.Button btnPacientiVindecati;
    }
}

