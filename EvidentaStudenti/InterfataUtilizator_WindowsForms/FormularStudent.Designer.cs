
namespace InterfataUtilizator_WindowsForms
{
    partial class FormularStudent
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
            this.lblNote = new System.Windows.Forms.Label();
            this.btnAdauga = new System.Windows.Forms.Button();
            this.txtNume = new System.Windows.Forms.TextBox();
            this.txtPrenume = new System.Windows.Forms.TextBox();
            this.txtNote = new System.Windows.Forms.TextBox();
            this.btnAfiseaza = new System.Windows.Forms.Button();
            this.btnCauta = new System.Windows.Forms.Button();
            this.lblMesaj = new System.Windows.Forms.Label();
            this.btnModifica = new System.Windows.Forms.Button();
            this.gpbProgrameStudiu = new System.Windows.Forms.GroupBox();
            this.rdbInginerieE = new System.Windows.Forms.RadioButton();
            this.rdbElectronica = new System.Windows.Forms.RadioButton();
            this.rdbElectrotehnica = new System.Windows.Forms.RadioButton();
            this.rdbCalculatoare = new System.Windows.Forms.RadioButton();
            this.rdbAutomatica = new System.Windows.Forms.RadioButton();
            this.lblSpecializare = new System.Windows.Forms.Label();
            this.ckbPIU = new System.Windows.Forms.CheckBox();
            this.ckbPOO = new System.Windows.Forms.CheckBox();
            this.ckbPCLP = new System.Windows.Forms.CheckBox();
            this.lblDiscipline = new System.Windows.Forms.Label();
            this.ckbDEEA2 = new System.Windows.Forms.CheckBox();
            this.ckbED = new System.Windows.Forms.CheckBox();
            this.ckbMEST = new System.Windows.Forms.CheckBox();
            this.gpbDiscipline = new System.Windows.Forms.GroupBox();
            this.lstStudenti = new System.Windows.Forms.ListBox();
            this.dataGridStudenti = new System.Windows.Forms.DataGridView();
            this.btnStudPromovati = new System.Windows.Forms.Button();
            this.gpbProgrameStudiu.SuspendLayout();
            this.gpbDiscipline.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridStudenti)).BeginInit();
            this.SuspendLayout();
            // 
            // lblNume
            // 
            this.lblNume.AutoSize = true;
            this.lblNume.Location = new System.Drawing.Point(19, 31);
            this.lblNume.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblNume.Name = "lblNume";
            this.lblNume.Size = new System.Drawing.Size(35, 13);
            this.lblNume.TabIndex = 0;
            this.lblNume.Text = "Nume";
            // 
            // lblPrenume
            // 
            this.lblPrenume.AutoSize = true;
            this.lblPrenume.Location = new System.Drawing.Point(19, 60);
            this.lblPrenume.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblPrenume.Name = "lblPrenume";
            this.lblPrenume.Size = new System.Drawing.Size(49, 13);
            this.lblPrenume.TabIndex = 1;
            this.lblPrenume.Text = "Prenume";
            // 
            // lblNote
            // 
            this.lblNote.AutoSize = true;
            this.lblNote.Location = new System.Drawing.Point(3, 256);
            this.lblNote.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.lblNote.Name = "lblNote";
            this.lblNote.Size = new System.Drawing.Size(30, 13);
            this.lblNote.TabIndex = 2;
            this.lblNote.Text = "Note";
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
            // txtNote
            // 
            this.txtNote.Location = new System.Drawing.Point(97, 253);
            this.txtNote.Margin = new System.Windows.Forms.Padding(2);
            this.txtNote.Name = "txtNote";
            this.txtNote.Size = new System.Drawing.Size(209, 20);
            this.txtNote.TabIndex = 6;
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
            // gpbProgrameStudiu
            // 
            this.gpbProgrameStudiu.Controls.Add(this.rdbInginerieE);
            this.gpbProgrameStudiu.Controls.Add(this.rdbElectronica);
            this.gpbProgrameStudiu.Controls.Add(this.rdbElectrotehnica);
            this.gpbProgrameStudiu.Controls.Add(this.rdbCalculatoare);
            this.gpbProgrameStudiu.Controls.Add(this.rdbAutomatica);
            this.gpbProgrameStudiu.Location = new System.Drawing.Point(97, 87);
            this.gpbProgrameStudiu.Name = "gpbProgrameStudiu";
            this.gpbProgrameStudiu.Size = new System.Drawing.Size(208, 100);
            this.gpbProgrameStudiu.TabIndex = 18;
            this.gpbProgrameStudiu.TabStop = false;
            // 
            // rdbInginerieE
            // 
            this.rdbInginerieE.AutoSize = true;
            this.rdbInginerieE.Location = new System.Drawing.Point(15, 56);
            this.rdbInginerieE.Name = "rdbInginerieE";
            this.rdbInginerieE.Size = new System.Drawing.Size(121, 17);
            this.rdbInginerieE.TabIndex = 12;
            this.rdbInginerieE.TabStop = true;
            this.rdbInginerieE.Text = "Inginerie Economica";
            this.rdbInginerieE.UseVisualStyleBackColor = true;
            // 
            // rdbElectronica
            // 
            this.rdbElectronica.AutoSize = true;
            this.rdbElectronica.Location = new System.Drawing.Point(15, 32);
            this.rdbElectronica.Name = "rdbElectronica";
            this.rdbElectronica.Size = new System.Drawing.Size(78, 17);
            this.rdbElectronica.TabIndex = 10;
            this.rdbElectronica.TabStop = true;
            this.rdbElectronica.Text = "Electronica";
            this.rdbElectronica.UseVisualStyleBackColor = true;
            // 
            // rdbElectrotehnica
            // 
            this.rdbElectrotehnica.AutoSize = true;
            this.rdbElectrotehnica.Location = new System.Drawing.Point(105, 32);
            this.rdbElectrotehnica.Name = "rdbElectrotehnica";
            this.rdbElectrotehnica.Size = new System.Drawing.Size(93, 17);
            this.rdbElectrotehnica.TabIndex = 11;
            this.rdbElectrotehnica.TabStop = true;
            this.rdbElectrotehnica.Text = "Electrotehnica";
            this.rdbElectrotehnica.UseVisualStyleBackColor = true;
            // 
            // rdbCalculatoare
            // 
            this.rdbCalculatoare.AutoSize = true;
            this.rdbCalculatoare.Location = new System.Drawing.Point(15, 9);
            this.rdbCalculatoare.Name = "rdbCalculatoare";
            this.rdbCalculatoare.Size = new System.Drawing.Size(84, 17);
            this.rdbCalculatoare.TabIndex = 8;
            this.rdbCalculatoare.TabStop = true;
            this.rdbCalculatoare.Text = "Calculatoare";
            this.rdbCalculatoare.UseVisualStyleBackColor = true;
            // 
            // rdbAutomatica
            // 
            this.rdbAutomatica.AutoSize = true;
            this.rdbAutomatica.Location = new System.Drawing.Point(105, 9);
            this.rdbAutomatica.Name = "rdbAutomatica";
            this.rdbAutomatica.Size = new System.Drawing.Size(78, 17);
            this.rdbAutomatica.TabIndex = 9;
            this.rdbAutomatica.TabStop = true;
            this.rdbAutomatica.Text = "Automatica";
            this.rdbAutomatica.UseVisualStyleBackColor = true;
            // 
            // lblSpecializare
            // 
            this.lblSpecializare.AutoSize = true;
            this.lblSpecializare.Location = new System.Drawing.Point(19, 98);
            this.lblSpecializare.Name = "lblSpecializare";
            this.lblSpecializare.Size = new System.Drawing.Size(70, 13);
            this.lblSpecializare.TabIndex = 17;
            this.lblSpecializare.Text = "Specializarea";
            // 
            // ckbPIU
            // 
            this.ckbPIU.AutoSize = true;
            this.ckbPIU.Location = new System.Drawing.Point(174, 11);
            this.ckbPIU.Name = "ckbPIU";
            this.ckbPIU.Size = new System.Drawing.Size(44, 17);
            this.ckbPIU.TabIndex = 22;
            this.ckbPIU.Text = "PIU";
            this.ckbPIU.UseVisualStyleBackColor = true;
            this.ckbPIU.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbPOO
            // 
            this.ckbPOO.AutoSize = true;
            this.ckbPOO.Location = new System.Drawing.Point(90, 12);
            this.ckbPOO.Name = "ckbPOO";
            this.ckbPOO.Size = new System.Drawing.Size(49, 17);
            this.ckbPOO.TabIndex = 21;
            this.ckbPOO.Text = "POO";
            this.ckbPOO.UseVisualStyleBackColor = true;
            this.ckbPOO.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbPCLP
            // 
            this.ckbPCLP.AutoSize = true;
            this.ckbPCLP.Location = new System.Drawing.Point(12, 11);
            this.ckbPCLP.Name = "ckbPCLP";
            this.ckbPCLP.Size = new System.Drawing.Size(53, 17);
            this.ckbPCLP.TabIndex = 20;
            this.ckbPCLP.Text = "PCLP";
            this.ckbPCLP.UseVisualStyleBackColor = true;
            this.ckbPCLP.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // lblDiscipline
            // 
            this.lblDiscipline.AutoSize = true;
            this.lblDiscipline.Location = new System.Drawing.Point(19, 194);
            this.lblDiscipline.Name = "lblDiscipline";
            this.lblDiscipline.Size = new System.Drawing.Size(52, 13);
            this.lblDiscipline.TabIndex = 19;
            this.lblDiscipline.Text = "Discipline";
            // 
            // ckbDEEA2
            // 
            this.ckbDEEA2.AutoSize = true;
            this.ckbDEEA2.Location = new System.Drawing.Point(12, 35);
            this.ckbDEEA2.Name = "ckbDEEA2";
            this.ckbDEEA2.Size = new System.Drawing.Size(61, 17);
            this.ckbDEEA2.TabIndex = 23;
            this.ckbDEEA2.Text = "DEEA2";
            this.ckbDEEA2.UseVisualStyleBackColor = true;
            this.ckbDEEA2.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbED
            // 
            this.ckbED.AutoSize = true;
            this.ckbED.Location = new System.Drawing.Point(90, 36);
            this.ckbED.Name = "ckbED";
            this.ckbED.Size = new System.Drawing.Size(41, 17);
            this.ckbED.TabIndex = 24;
            this.ckbED.Text = "ED";
            this.ckbED.UseVisualStyleBackColor = true;
            this.ckbED.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // ckbMEST
            // 
            this.ckbMEST.AutoSize = true;
            this.ckbMEST.Location = new System.Drawing.Point(172, 36);
            this.ckbMEST.Name = "ckbMEST";
            this.ckbMEST.Size = new System.Drawing.Size(56, 17);
            this.ckbMEST.TabIndex = 25;
            this.ckbMEST.Text = "MEST";
            this.ckbMEST.UseVisualStyleBackColor = true;
            this.ckbMEST.CheckedChanged += new System.EventHandler(this.ckbDiscipline_CheckedChanged);
            // 
            // gpbDiscipline
            // 
            this.gpbDiscipline.Controls.Add(this.ckbMEST);
            this.gpbDiscipline.Controls.Add(this.ckbPCLP);
            this.gpbDiscipline.Controls.Add(this.ckbED);
            this.gpbDiscipline.Controls.Add(this.ckbPOO);
            this.gpbDiscipline.Controls.Add(this.ckbDEEA2);
            this.gpbDiscipline.Controls.Add(this.ckbPIU);
            this.gpbDiscipline.Location = new System.Drawing.Point(97, 193);
            this.gpbDiscipline.Margin = new System.Windows.Forms.Padding(2);
            this.gpbDiscipline.Name = "gpbDiscipline";
            this.gpbDiscipline.Padding = new System.Windows.Forms.Padding(2);
            this.gpbDiscipline.Size = new System.Drawing.Size(231, 56);
            this.gpbDiscipline.TabIndex = 26;
            this.gpbDiscipline.TabStop = false;
            // 
            // lstStudenti
            // 
            this.lstStudenti.FormattingEnabled = true;
            this.lstStudenti.Location = new System.Drawing.Point(376, 24);
            this.lstStudenti.Margin = new System.Windows.Forms.Padding(2);
            this.lstStudenti.Name = "lstStudenti";
            this.lstStudenti.Size = new System.Drawing.Size(336, 160);
            this.lstStudenti.TabIndex = 27;
            this.lstStudenti.SelectedIndexChanged += new System.EventHandler(this.lstStudenti_SelectedIndexChanged);
            // 
            // dataGridStudenti
            // 
            this.dataGridStudenti.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridStudenti.Location = new System.Drawing.Point(376, 203);
            this.dataGridStudenti.Name = "dataGridStudenti";
            this.dataGridStudenti.Size = new System.Drawing.Size(335, 115);
            this.dataGridStudenti.TabIndex = 28;
            this.dataGridStudenti.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridStudenti_CellContentClick);
            // 
            // btnStudPromovati
            // 
            this.btnStudPromovati.Location = new System.Drawing.Point(472, 331);
            this.btnStudPromovati.Name = "btnStudPromovati";
            this.btnStudPromovati.Size = new System.Drawing.Size(147, 23);
            this.btnStudPromovati.TabIndex = 29;
            this.btnStudPromovati.Text = "Afisare Studenti Promovati";
            this.btnStudPromovati.UseVisualStyleBackColor = true;
            this.btnStudPromovati.Click += new System.EventHandler(this.btnStudPromovati_Click);
            // 
            // FormularStudent
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(742, 383);
            this.Controls.Add(this.btnStudPromovati);
            this.Controls.Add(this.dataGridStudenti);
            this.Controls.Add(this.lstStudenti);
            this.Controls.Add(this.gpbDiscipline);
            this.Controls.Add(this.lblDiscipline);
            this.Controls.Add(this.gpbProgrameStudiu);
            this.Controls.Add(this.lblSpecializare);
            this.Controls.Add(this.btnModifica);
            this.Controls.Add(this.lblMesaj);
            this.Controls.Add(this.btnCauta);
            this.Controls.Add(this.btnAfiseaza);
            this.Controls.Add(this.txtNote);
            this.Controls.Add(this.txtPrenume);
            this.Controls.Add(this.txtNume);
            this.Controls.Add(this.btnAdauga);
            this.Controls.Add(this.lblNote);
            this.Controls.Add(this.lblPrenume);
            this.Controls.Add(this.lblNume);
            this.Margin = new System.Windows.Forms.Padding(2);
            this.Name = "FormularStudent";
            this.Text = "Administrare studenti";
            this.Load += new System.EventHandler(this.FormularStudent_Load);
            this.gpbProgrameStudiu.ResumeLayout(false);
            this.gpbProgrameStudiu.PerformLayout();
            this.gpbDiscipline.ResumeLayout(false);
            this.gpbDiscipline.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridStudenti)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Label lblPrenume;
        private System.Windows.Forms.Label lblNote;
        private System.Windows.Forms.Button btnAdauga;
        private System.Windows.Forms.Label lblNume;
        private System.Windows.Forms.TextBox txtNume;
        private System.Windows.Forms.TextBox txtPrenume;
        private System.Windows.Forms.TextBox txtNote;
        private System.Windows.Forms.Button btnAfiseaza;
        private System.Windows.Forms.Button btnCauta;
        private System.Windows.Forms.Label lblMesaj;
        private System.Windows.Forms.Button btnModifica;
        private System.Windows.Forms.GroupBox gpbProgrameStudiu;
        private System.Windows.Forms.RadioButton rdbCalculatoare;
        private System.Windows.Forms.RadioButton rdbAutomatica;
        private System.Windows.Forms.Label lblSpecializare;
        private System.Windows.Forms.CheckBox ckbPIU;
        private System.Windows.Forms.CheckBox ckbPOO;
        private System.Windows.Forms.CheckBox ckbPCLP;
        private System.Windows.Forms.Label lblDiscipline;
        private System.Windows.Forms.RadioButton rdbInginerieE;
        private System.Windows.Forms.RadioButton rdbElectronica;
        private System.Windows.Forms.RadioButton rdbElectrotehnica;
        private System.Windows.Forms.CheckBox ckbDEEA2;
        private System.Windows.Forms.CheckBox ckbED;
        private System.Windows.Forms.CheckBox ckbMEST;
        private System.Windows.Forms.GroupBox gpbDiscipline;
        private System.Windows.Forms.ListBox lstStudenti;
        private System.Windows.Forms.DataGridView dataGridStudenti;
        private System.Windows.Forms.Button btnStudPromovati;
    }
}

