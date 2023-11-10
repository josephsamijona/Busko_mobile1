import sqlite3
import os
 

# Obtenir le chemin absolu du répertoire "database" en utilisant os.path
database_dir = os.path.join(os.path.dirname(__file__), "..", "database")

# Spécifiez le chemin absolu de la base de données dans le dossier "database"
db_path = os.path.join(database_dir, "clinique.db")

# Ouvrez la connexion vers la base de données
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Définir la structure de la table Utilisateurs (Login)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Utilisateurs (
        User_Id TEXT PRIMARY KEY,
        First_Name TEXT,
        Last_Name TEXT,
        Username TEXT,
        Email TEXT,
        Phone INTEGER,
        Password TEXT,
        Date_of_Creation DATE,
        Account_Type TEXT
    )
''')

# Définir la structure de la table Table de Connexion
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Connexion (
        Connexion_Id TEXT PRIMARY KEY,
        User_Id TEXT,
        Date_Time TEXT,
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Définir la structure de la table Table du Dossier Médical
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Dossier_Medical (
        Patient_Id TEXT PRIMARY KEY,
        Date_Ouverture_Dossier DATE,
        Nom TEXT,
        Prenom TEXT,
        Date_Naissance DATE,
        Genre TEXT,
        Statut_Marital TEXT,
        Email TEXT,
        Telephone INTEGER,
        Telephone2 INTEGER,
        Adresse TEXT,
        Religion TEXT,
        Nationalite TEXT,
        Groupe_Sanguin TEXT,
        Hauteur REAL,
        Poids REAL,
        Methode_Paiement TEXT,
        Tension_Arterielle REAL,
        Rythme_Cardiaque REAL
    )
''')

# Définir la structure de la table Table de l'Historique du Patient
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Historique_Patient (
        Historique_Patient_Id INTEGER PRIMARY KEY,
        Patient_Id TEXT,
        Date_Heure_Modification DATE,
        User_Id TEXT,
        Champ_Modifie TEXT,
        Valeur_Avant_Modification TEXT,
        Nouvelle_Valeur TEXT,
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id),
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id)
    )
''')

# Définir la structure de la table Table de l'Inventaire
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Inventaire (
        Article_Id TEXT PRIMARY KEY,
        Nom_Article TEXT,
        Description_Article TEXT,
        Categorie_Id TEXT,
        Quantite_Stock INTEGER,
        Quantite_Minimale_Souhaitee INTEGER,
        Prix_Unitaire REAL,
        Date_Expiration TEXT
    )
''')

# Définir la structure de la table Table des Mouvements d'Inventaire
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Mouvements_Inventaire (
        Mouvement_Id INTEGER PRIMARY KEY,
        Article_Id TEXT,
        Type_Mouvement TEXT,
        Date_Heure_Mouvement DATETIME,
        Quantite_Impliquee INTEGER,
        User_Id TEXT,
        Raison_Mouvement TEXT,
        Nouvelle_Quantite_Stock INTEGER,
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id),
        FOREIGN KEY (Article_Id) REFERENCES Inventaire (Article_Id)
    )
''')

# Définir la structure de la table Table des Fournisseurs
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fournisseurs (
        Fournisseur_Id TEXT PRIMARY KEY,
        Nom_Fournisseur TEXT,
        Adresse TEXT,
        Numero_Telephone INTEGER,
        Adresse_Email TEXT,
        Produits_Fournis TEXT
    )
''')

# Définir la structure de la table Table des Alertes de Réapprovisionnement
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alertes_Reapprovisionnement (
        Alerte_Id TEXT PRIMARY KEY,
        Article_Id TEXT,
        Quantite_Minimale_Souhaitee INTEGER,
        Quantite_Actuelle_Stock INTEGER,
        Date_Alerte DATE,
        Statut_Alerte TEXT,
        Numero_Lot_Medicament TEXT,
        Fournisseur_Id TEXT,
        Medicament_Commander TEXT,
        Quantite_Commander INTEGER,
        Date_Commande DATE,
        User_Id TEXT,
        Remarques_Alerte TEXT,
        Statut_Traitement_Commande TEXT,
        Date_Reception_Medicaments DATE,
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id),
        FOREIGN KEY (Fournisseur_Id) REFERENCES Fournisseurs  (Fournisseur_Id)
    )
''')

# Définir la structure de la table Table des Rendez-vous
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Rendezvous (
        Rendezvous_Id TEXT PRIMARY KEY,
        Nom TEXT,
        Prenom TEXT,
        Patient_Id TEXT,
        Date_Heure_Rendezvous DATETIME,
        Duree_Rendezvous INTEGER,
        Motif_Rendezvous TEXT,
        User_Id TEXT,
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
        
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Définir la structure de la table Table des Factures (Finances)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Factures (
        Facture_Id TEXT PRIMARY KEY,
        User_Id TEXT,
        Patient_Id TEXT,
        Nom TEXT,
        Prenom TEXT,
        Adresse TEXT,
        Date_Facture DATE,
        Montant_Total REAL,
        Statut_Facture TEXT,
        Date_Paiement DATE,
        Methode_Paiement TEXT,
        Description_Services_Produits TEXT,
        Numero_Facture TEXT,
        Coordonnees_Clinique TEXT,
        Taxes REAL,
        Remises REAL,
        Details_Assurance TEXT,
        Numero_Reference_Paiement TEXT,
        Notes_Commentaires TEXT,
        Type_Service_Produit TEXT,
        Modes_Paiement_Acceptes TEXT,
        Documents_Attaches BLOB,
        Statut_Remboursement TEXT,
        Responsable_Facturation TEXT,
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
        FOREIGN KEY (Nom) REFERENCES Dossier_Medical (Nom),
        FOREIGN KEY (Prenom) REFERENCES Dossier_Medical (Prenom),
        FOREIGN KEY (Adresse) REFERENCES Dossier_Medical (Adresse),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Définir la structure de la table Table des Revenus (Finances)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Revenus (
        Revenu_Id INTEGER PRIMARY KEY,
        Source_Revenu TEXT,
        Date_Revenu DATE,
        Montant_Revenu REAL,
        Type_Paiement TEXT,
        Reference_Facture TEXT,
        Responsable_Paiement TEXT,
        Details_Transaction TEXT,
        Statut_Transaction TEXT,
        Reference_Patient TEXT,
        Mode_Facturation TEXT,
        Categorie_Revenu TEXT,
        Date_Saisie DATETIME,
        Reference_Compte_Bancaire TEXT,
        Methode_Facturation TEXT,
        Heure_Transaction TIME,
        Devise TEXT,
        Taxes REAL,
        Remises REAL,
        Rapprochement_Bancaire TEXT
    )
''')

# Définir la structure de la table Table des Dépenses (Finances)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Depenses (
        Depense_Id TEXT PRIMARY KEY,
        Categorie_Depense TEXT,
        Date_Depense DATE,
        Montant_Depense REAL,
        Description_Depense TEXT,
        Numero_Facture_Reçu TEXT,
        Methode_Paiement TEXT,
        Responsable_Depense TEXT,
        Devise TEXT,
        Taxes REAL,
        Remises REAL,
        Lieu_Depense TEXT,
        Fournisseur_ID TEXT,
        Numero_Bon_Commande TEXT,
        Statut_Depense TEXT,
        Notes_Commentaires TEXT,
        Rapprochement_Comptable TEXT,
        Type_Depense TEXT,
        Date_Saisie DATETIME,
        Nom_Fournisseur  TEXT,
        FOREIGN KEY (Fournisseur_Id) REFERENCES Fournisseurs  (Fournisseur_Id),
        FOREIGN KEY (Nom_Fournisseur ) REFERENCES Fournisseurs  (Nom_Fournisseur)
    )
''')

# Définir la structure de la table Table des Examens de L'hemogramme
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Examens_Hemogramme (
        Examen_Id TEXT PRIMARY KEY,
        Nom TEXT,
        Prenom TEXT,
        Adresse TEXT,
        Patient_Id TEXT,
        Date_Test DATE,
        User_Id TEXT,
        Telephone INTEGER,
        Globules_Rouges TEXT,
        Globules_Blancs TEXT,
        Hematocrite TEXT,
        Hemoglobine TEXT,
        MCV TEXT,
        MCH TEXT,
        MCHC TEXT,
        Polynucleaires TEXT,
        Lymphocytes TEXT,
        Monocytes TEXT,
        Eosinophiles TEXT,
        Basophiles TEXT,
        Reticulocytes TEXT,
        Plaquettes TEXT,
        Groupe_Sanguin TEXT,
        Test_Malaria TEXT,
        Test_Falciformation TEXT,
        Electrophorese_Hemoglobine TEXT,
        Phenotype_Groupe_Sanguin TEXT,
        Vitesse_Sedimentation TEXT,
        Temps_Saignement TEXT,
        Temps_Coagulation TEXT,
        PT TEXT,
        PTT TEXT,
        IRN TEXT,
        D_Dimeres TEXT,
        Fibrinogene TEXT,
        Troponine TEXT,
        CRP TEXT,
        Procalcitonine TEXT,
        Bilirubine_Totale TEXT,
        Bilirubine_Directe TEXT,
        Bilirubine_Indirecte TEXT,
        Lipides_Sanguins TEXT,
        Electrolytes TEXT,
        Marqueurs_Hormonaux TEXT,
        Tests_Allergies TEXT,
        Tests_Fonction_Renale TEXT,
        Tests_Coagulation TEXT,
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
        FOREIGN KEY (Nom) REFERENCES Dossier_Medical (Nom),
        FOREIGN KEY (Prenom) REFERENCES Dossier_Medical (Prenom),
        FOREIGN KEY (Adresse) REFERENCES Dossier_Medical (Adresse),
        FOREIGN KEY (Telephone) REFERENCES Dossier_Medical (Telephone),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Définir la structure de la table Table des Examens de l'urine
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ExamenUrine (
      Examen_Id  TEXT PRIMARY KEY,
      User_Id TEXT,
      Nom TEXT,
      Prenom TEXT,
      Adresse TEXT,
      Patient_Id TEXT,
      Couleur TEXT,
      Telephone INTEGER,
      Aspect TEXT,
      Densite REAL,
      pH REAL,
      Glucose TEXT,
      Proteinurie TEXT,
      Cetone TEXT,
      Bilirubinurie TEXT,
      Nitrites TEXT,
      Urobilinogene TEXT,
      Microscopie TEXT,
      Leucocytes TEXT,
      Hematies TEXT,
      CellulesEpitheliales TEXT,
      Bacteries TEXT,
      LevuresSimples TEXT,
      LevuresBourgeonnantes TEXT,
      CristauxOxalateCalcium TEXT,
      CylindresLeucocytaires TEXT,
      CylindresGranuleux TEXT,
      TrichomonasVaginalis TEXT,
      FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
      FOREIGN KEY (Nom) REFERENCES Dossier_Medical (Nom),
      FOREIGN KEY (Prenom) REFERENCES Dossier_Medical (Prenom),
      FOREIGN KEY (Adresse) REFERENCES Dossier_Medical (Adresse),
      FOREIGN KEY (Telephone) REFERENCES Dossier_Medical (Telephone),
      FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
       
   )
''')

# Définir la structure de la table Table des Examens de La biochimie
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Examens_Biochimie (
        Examen_Id TEXT PRIMARY KEY,
        Nom TEXT,
        Prenom TEXT,
        Adresse TEXT,
        Patient_Id TEXT,
        Date_Test DATE,
        User_Id TEXT,
        Telephone TEXT,
        Glycemie TEXT,
        Azote_Uree TEXT,
        Uree TEXT,
        Creatinine TEXT,
        BUN_Creatinine TEXT,
        Proteines_Totales TEXT,
        Albumine TEXT,
        Globuline TEXT,
        Rapport_Albumine_Globuline TEXT,
        Acide_Urique TEXT,
        Sodium TEXT,
        Potassium TEXT,
        Calcium TEXT,
        CO2 TEXT,
        Magnesium TEXT,
        Chlorure TEXT,
        Bilirubine_Totale TEXT,
        Bilirubine_Directe TEXT,
        Bilirubine_Indirecte TEXT,
        SGOT TEXT,
        SGPT TEXT,
        Phosphore TEXT,
        Cholesterol TEXT,
        HDL_Cholesterol TEXT,
        Triglycerides TEXT,
        VLDL_Cholesterol TEXT,
        LDL_Cholesterol TEXT,
        Phosphatase_Alcaline TEXT,
        Prolactine TEXT,
        Insuline TEXT,
        Hemoglobine_Glyquee TEXT,
        Fer_Serique TEXT,
        Ferritine TEXT,
        TLBC TEXT,
        FSH_LH TEXT,
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
        FOREIGN KEY (Nom) REFERENCES Dossier_Medical (Nom),
        FOREIGN KEY (Prenom) REFERENCES Dossier_Medical (Prenom),
        FOREIGN KEY (Adresse) REFERENCES Dossier_Medical (Adresse),
        FOREIGN KEY (Telephone) REFERENCES Dossier_Medical (Telephone),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
         
    )
''')
# Définir la structure de la table Table des Examens des selles
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Examens_Selles (
        Examen_Id TEXT PRIMARY KEY,
        Nom TEXT,
        Prenom TEXT,
        Adresse TEXT,
        Patient_Id TEXT,
        Date_Test DATE,
        User_Id TEXT,
        Telephone TEXT,
        Apparence_Selles TEXT,
        Consistance_Selles TEXT,
        Sang_Occulte TEXT,
        Oeufs_Parasites TEXT,
        Bleu_Methylene TEXT,
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
        FOREIGN KEY (Nom) REFERENCES Dossier_Medical (Nom),
        FOREIGN KEY (Prenom) REFERENCES Dossier_Medical (Prenom),
        FOREIGN KEY (Adresse) REFERENCES Dossier_Medical (Adresse),
        FOREIGN KEY (Telephone) REFERENCES Dossier_Medical (Telephone),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Définir la structure de la table Table des Examens de serologie
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Serologie (
        Examen_Id TEXT PRIMARY KEY,
        Patient_Id TEXT,
        Date_Examen DATE,
        User_Id TEXT,
        Nom TEXT,
        Prenom TEXT,
        Adresse TEXT, 
        Telephone INTEGER,
        BHCG TEXT,
        RPR TEXT,
        HIV TEXT,
        CRP TEXT,
        ASO TEXT,
        PSA TEXT,
        Salmonella_O TEXT,
        Salmonella_H TEXT,
        H_Pyloric TEXT,
        Toxoplasma_IGG TEXT,
        Toxoplasma_IGM TEXT,
        Rubella_IGM TEXT,
        TPHA TEXT,
        Chlamydia_ICG TEXT,
        Chlamydia_IGM TEXT,
        Facteur_Rhumatoide TEXT,
        Mantoux_Test TEXT,
        Herpes_Type_I_IGG TEXT,
        Herpes_Type_II_IGG TEXT,
        Herpes_Type_II_IGM TEXT,
        Hbs_Ag TEXT,
        Hepatite_C TEXT,
        Mono_Test TEXT,
        Virus_Hepatite_B TEXT,
        Virus_Hepatite_C TEXT,
        Anticorps_VIH TEXT,
        Virus_Dengue TEXT,
        Virus_Zika TEXT,
        Virus_Fievre_Jaune TEXT,
        Virus_Rubeole TEXT,
        Anticorps_Toxoplasme TEXT,
        Virus_Grippe TEXT,
        Virus_Rougeole TEXT,
        Virus_Oreillons TEXT,
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
        FOREIGN KEY (Nom) REFERENCES Dossier_Medical (Nom),
        FOREIGN KEY (Prenom) REFERENCES Dossier_Medical (Prenom),
        FOREIGN KEY (Adresse) REFERENCES Dossier_Medical (Adresse),
        FOREIGN KEY (Telephone) REFERENCES Dossier_Medical (Telephone),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
         
    )
''')

# Définir la structure de la table Table des Fiches de Prescription (Pharmacie)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Fiches_Prescription (
        Fiche_Prescription_Id TEXT PRIMARY KEY,
        Patient_Id TEXT,
        User_Id TEXT,
        Date_Prescription TEXT,
        Medicament_Prescrit TEXT,
        Quantite_Prescrite INTEGER,
        Frequence_Prise TEXT,
        Instructions_Speciales TEXT,
        Statut_Prescription TEXT,
        Numero_Lot TEXT,
        Date_Debut_Traitement TEXT,
        Date_Fin_Traitement TEXT,
        Renouvellement_Prescription TEXT,
        Notes_Medecin TEXT,
        Statut_Validation TEXT,
        Rappels_Prescription TEXT,
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
         
    )
''')

# Définir la structure de la table Table des Ventes (Pharmacie)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ventes (
        Vente_Id TEXT PRIMARY KEY,
        Article_Id TEXT,
        Patient_Id TEXT,
        User_Id TEXT,
        Date_Vente TEXT,
        Quantite_Vendue INTEGER,
        Prix_Unitaire_Vente REAL,
        Montant_Total_Vente REAL,
        Numero_Lot_Medicament TEXT,
        Heure_Vente TEXT,
        Mode_Paiement TEXT,
        Remarques_Vente TEXT,
        Statut_Vente TEXT,
        Fournisseur_Id TEXT,
        Prescription_Requise TEXT,
        Statut_Livraison TEXT,
        FOREIGN KEY (Article_Id) REFERENCES Inventaire  (Article_Id),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id),
        FOREIGN KEY (Fournisseur_Id) REFERENCES Fournisseurs  (Fournisseur_Id),
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id)
         
    )
''')

# Définir la structure de la table Table des Mouvements de Médicaments (Pharmacie)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Mouvements_Medicaments (
        Mouvement_Id TEXT PRIMARY KEY,
        Article_Id TEXT,
        Type_Mouvement TEXT,
        Date_Heure_Mouvement DATETIME,
        Quantite_Impliquee INTEGER,
        User_Id TEXT,
        Raison_Mouvement TEXT,
        Nouvelle_Quantite_Stock INTEGER,
        Numero_Lot_Medicament TEXT,
        Reference_Commande TEXT,
        Cout_Unitaire REAL,
        Cout_Total REAL,
        Stock_Minimum INTEGER,
        Statut_Validation TEXT,
        Fournisseur_Id TEXT,
        Commande_Client_Id TEXT,
        Reference_Patient TEXT,
        Emplacement_Stockage TEXT,
        Methode_Stockage TEXT,
        Date_Expiration_Medicament TEXT,
        FOREIGN KEY (Article_Id) REFERENCES Inventaire  (Article_Id),
        FOREIGN KEY (Fournisseur_Id) REFERENCES Fournisseurs  (Fournisseur_Id),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Définir la structure de la table Table des Alertes de Réapprovisionnement (Pharmacie)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Alertes_Reapprovisionnement_Pharmacie (
        Alerte_Id TEXT PRIMARY KEY,
        Article_Id TEXT,
        Quantite_Minimale_Souhaitee INTEGER,
        Quantite_Actuelle_Stock INTEGER,
        Date_Alerte DATE,
        Statut_Alerte TEXT,
        Pharmacie_Id TEXT,
        Numero_Lot_Medicament TEXT,
        Reference_Fournisseur TEXT,
        Medicament_Commander TEXT,
        Quantite_Commander INTEGER,
        Date_Commande DATE,
        User_Id TEXT,
        Remarques_Alerte TEXT,
        Statut_Traitement_Commande TEXT,
        Date_Reception_Medicaments DATE,
        FOREIGN KEY (Article_Id) REFERENCES Inventaire  (Article_Id),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
       
    )
''')

# Définir la structure de la table Table de l'Histoire des Rendez-vous
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Historique_Rendezvous (
        Historique_Rendezvous_Id TEXT PRIMARY KEY,
        Rendezvous_Id TEXT,
        Date_Heure_Modification DATETIME,
        User_Id TEXT,
        Nouvelle_Date_Heure_Rendezvous DATETIME,
        Motif_Modification TEXT,
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id),
        FOREIGN KEY (Rendezvous_Id) REFERENCES Rendezvous (Rendezvous_Id)
        
    )
''')

# Définir la structure de la table Table de l'Histoire des Dossiers Médicaux
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Historique_Dossiers_Medicaux (
        Historique_Dossiers_Medicaux_Id TEXT PRIMARY KEY,
        Patient_Id TEXT,
        Date_Heure_Modification DATETIME,
        User_Id TEXT,
        Champ_Modifie TEXT,
        Valeur_Avant_Modification TEXT,
        Nouvelle_Valeur TEXT,
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id),
        FOREIGN KEY (Patient_Id) REFERENCES Dossier_Medical (Patient_Id)
    )
''')

# Définir la structure de la table Table de l'Histoire des Factures
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Historique_Factures (
        Historique_Factures_Id TEXT PRIMARY KEY,
        Facture_Id TEXT,
        Date_Heure_Modification DATETIME,
        User_Id TEXT,
        Montant_Modifie REAL,
        Motif_Modification TEXT,
        FOREIGN KEY (Facture_Id) REFERENCES Factures (Facture_Id),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Définir la structure de la table Table de l'Histoire des Médicaments (Pharmacie)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Historique_Medicaments_Pharmacie (
        Historique_Medicaments_Pharmacie_Id TEXT PRIMARY KEY,
        Article_Id TEXT,
        Date_Heure_Modification DATETIME,
        User_Id TEXT,
        Champ_Modifie TEXT,
        Valeur_Avant_Modification TEXT,
        Nouvelle_Valeur TEXT,
        FOREIGN KEY (Article_Id) REFERENCES Inventaire  (Article_Id),
        FOREIGN KEY (User_Id) REFERENCES Utilisateurs (User_Id)
    )
''')

# Valider et enregistrer les modifications dans la base de données
conn.commit()

# Fermer la connexion
conn.close()

 


