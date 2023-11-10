import sqlite3
import tkinter as tk
from tkinter import messagebox
import random
import string
from datetime import date
import os

class CliniqueApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Formulaire de la Clinique")

        # Obtenez le chemin absolu de la base de données dans le même répertoire que votre code
        db_path = os.path.join(os.path.dirname(__file__), "clinique.db")

        # Connexion à la base de données
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()

        # Création de l'interface utilisateur
        self.label_first_name = tk.Label(root, text="Prénom :")
        self.label_first_name.pack()
        self.entry_first_name = tk.Entry(root)
        self.entry_first_name.pack()

        self.label_last_name = tk.Label(root, text="Nom :")
        self.label_last_name.pack()
        self.entry_last_name = tk.Entry(root)
        self.entry_last_name.pack()

        self.label_username = tk.Label(root, text="Nom d'utilisateur :")
        self.label_username.pack()
        self.entry_username = tk.Entry(root)
        self.entry_username.pack()

        self.label_email = tk.Label(root, text="Email :")
        self.label_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.label_phone = tk.Label(root, text="Téléphone :")
        self.label_phone.pack()
        self.entry_phone = tk.Entry(root)
        self.entry_phone.pack()

        self.label_password = tk.Label(root, text="Mot de passe :")
        self.label_password.pack()
        self.entry_password = tk.Entry(root, show="*")  # Afficher les caractères comme des étoiles
        self.entry_password.pack()

        self.label_account_type = tk.Label(root, text="Type de compte :")
        self.label_account_type.pack()

        # Options du menu déroulant pour le type de compte
        account_type_options = ["Doctor", "Nurse", "Admin", "Patient"]
        self.selected_account_type = tk.StringVar()
        self.selected_account_type.set(account_type_options[0])  # Sélectionnez le premier élément par défaut
        account_type_menu = tk.OptionMenu(root, self.selected_account_type, *account_type_options)
        account_type_menu.pack()

        self.button_submit = tk.Button(root, text="Soumettre", command=self.submit_data)
        self.button_submit.pack()

    def submit_data(self):
        first_name = self.entry_first_name.get()
        last_name = self.entry_last_name.get()
        username = self.entry_username.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        password = self.entry_password.get()
        account_type = self.selected_account_type.get()  # Récupérer la valeur sélectionnée du menu déroulant

        # Générer User ID
        random_letters = ''.join(random.choice(string.ascii_letters) for _ in range(2))
        random_numbers = ''.join(random.choice(string.digits) for _ in range(5))
        user_id = f"{last_name[:2]}{random_letters}{random_numbers}"

        # Date de création
        date_of_creation = date.today()

        # Insertion des données dans la base de données
        self.cursor.execute("INSERT INTO Utilisateurs (User_Id, First_Name, Last_Name, Username, Email, Phone, Password, Date_of_Creation, Account_Type) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                            (user_id, first_name, last_name, username, email, phone, password, date_of_creation, account_type))
        self.conn.commit()

        messagebox.showinfo("Succès", "Données insérées avec succès!")

    def __del__(self):
        self.conn.close()

if __name__ == "__main__":
    root = tk.Tk()
    app = CliniqueApp(root)
    root.mainloop()
