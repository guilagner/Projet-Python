from abc import ABC, abstractmethod
import sqlite3

class Personne(ABC):
    def __init__(self, nom, date_naissance):
        self.nom = nom
        self.date_naissance = date_naissance

    @abstractmethod
    def afficher(self):
        pass

class Etudiant(Personne):
    def __init__(self, nom, date_naissance, matricule):
        super().__init__(nom, date_naissance)
        self.matricule = matricule
        self.notes = []

    def ajouter_note(self, matiere, note):
        self.notes.append((matiere, note))

    def calculer_moyenne_etudiant(self):
        if self.notes:
            total = sum(note for matiere, note in self.notes)
            moyenne = total / len(self.notes)
            return moyenne
        else:
            return 0

    def afficher(self):
        print(f"Nom : {self.nom}")
        print(f"Date de naissance : {self.date_naissance}")
        print(f"Matricule : {self.matricule}")
        print("Notes :")
        for matiere, note in self.notes:
            print(f"{matiere}: {note}")
        print(f"Moyenne : {self.calculer_moyenne_etudiant()}")

class Classe:
    def __init__(self, nom):
        self.nom = nom
        self.etudiants = []
        self.moyenne = 0

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)
        cur.execute('''INSERT INTO Etudiants (matricule, nom, date_naissance) VALUES (?, ?, ?)''', (etudiant.matricule, etudiant.nom, etudiant.date_naissance))
        print("Etudiant ajouté avec succès à la base donnée.")
        conn.commit()

    def supprimer_etudiant(self, matricule):
        etudiant_a_supprimer = None
        for etudiant in self.etudiants:
            if etudiant.matricule == matricule:
                etudiant_a_supprimer = etudiant
                cur.execute("""DELETE FROM Etudiants  WHERE matricule=etudiant.matricule""")
                conn.commit()
                break

        if etudiant_a_supprimer:
            self.etudiants.remove(etudiant_a_supprimer)
            print(f"Etudiant avec matricule {matricule} supprimé.")
        else:
            print("Matricule invalide. Etudiant non trouvé.")

    def modifier_etudiant(self, matricule, nouveau_nom):
        for etudiant in self.etudiants:
            if etudiant.matricule == matricule:
                etudiant.nom = nouveau_nom
                print(f"Etudiant avec matricule {matricule} modifié.")
                cur.execute("""UPDATE Etudiants SET (nom) WHERE matricule = etudiant.matricule""")
                conn.commit()
                return

        print("Matricule invalide. Etudiant non trouvé.")

    def attribuer_note_etudiant(self, matricule):
        for etudiant in self.etudiants:
            if etudiant.matricule == matricule:
                matiere = input("Nom de la matière : ")
                note = float(input("Note de l'étudiant : "))
                etudiant.ajouter_note(matiere, note)
                print("Note attribuée avec succès.")
                for matiere, note in etudiant.notes:
                    cur.execute(''' INSERT INTO Notes (matricule, matiere, note) VALUES (?, ?, ?)''', (etudiant.matricule, matiere, note))
                    conn.commit()
                return

        print("Matricule invalide. Etudiant non trouvé.")

    def calculer_moyenne_classe(self):
        if self.etudiants:
            total_notes = 0
            total_matieres = 0
            for etudiant in self.etudiants:
                total_notes += sum(note for matiere, note in etudiant.notes)
                total_matieres += len(etudiant.notes)
            self.moyenne = total_notes / total_matieres
        else:
            self.moyenne = 0

  
    def afficher_classe(self):
        self.calculer_moyenne_classe()
        print(f"Classe : {self.nom}")
        print(f"Moyenne de la classe : {self.moyenne}")
        print("Liste des étudiants :")
        for etudiant in self.etudiants:
            etudiant.afficher()
            print()

# Programme principal
classe = Classe("Ingénieur IVVQ")
conn = sqlite3.connect('miniproject.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS Etudiants (matricule TEXT PRIMARY KEY,nom TEXT,date_naissance TEXT)''')
cur.execute('''CREATE TABLE IF NOT EXISTS Notes (id INTEGER PRIMARY KEY AUTOINCREMENT, matricule TEXT,matiere TEXT,note REAL,FOREIGN KEY(matricule) REFERENCES Etudiants(matricule) )''')
while True:

    print("\n1. Ajouter un étudiant")
    print("2. Modifier un étudiant")
    print("3. Supprimer un étudiant")
    print("4. Attribuer une note à un étudiant")
    print("5. Afficher la liste des étudiants")
    print("6. Quitter")
    choix = input("\nChoisissez une option : ")

    if choix == "1":
        nom = input("Nom de l'étudiant : ")
        date_naissance = input("Date de naissance de l'étudiant : ")
        matricule = input("Matricule de l'étudiant : ")
        etudiant = Etudiant(nom, date_naissance, matricule)
        classe.ajouter_etudiant(etudiant)
        print("Etudiant ajouté avec succès.")

    elif choix == "2":
        matricule = input("Matricule de l'étudiant à modifier : ")
        nouveau_nom = input("Nouveau nom de l'étudiant : ")
        classe.modifier_etudiant(matricule, nouveau_nom)
        
    elif choix == "3":
        matricule = input("Matricule de l'étudiant à supprimer : ")
        classe.supprimer_etudiant(matricule)
    elif choix == "4":
        matricule = input("Matricule de l'étudiant : ")
        classe.attribuer_note_etudiant(matricule)    
    elif choix == "5":
        classe.afficher_classe()
    elif choix == "6":
        print("Vous avez choisi de fermer le programme. Au revoir !")
        conn.close()
        break
    

