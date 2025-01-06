import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="user",       
        password="password",  
        database="universite"
    )

def create_and_populate_table(cursor):

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS etudiants (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nom VARCHAR(50) NOT NULL,
            age INT NOT NULL,
            moyenne FLOAT NOT NULL
        );
    """)

    etudiants = [
        ("Alice", 20, 15.5),
        ("Bob", 22, 12.3),
        ("Charlie", 19, 16.8),
        ("Diana", 21, 10.0)
    ]

    query = "INSERT INTO etudiants (nom, age, moyenne) VALUES (%s, %s, %s)"
    cursor.executemany(query, etudiants)
    print(f"{cursor.rowcount} enregistrements insérés.")
    
def retrieve_students(cursor, moyenne_limite):
    query = "SELECT id, nom, age, moyenne FROM etudiants WHERE moyenne > %s"
    cursor.execute(query, (moyenne_limite,))
    return cursor.fetchall()

def main():
    try:
        db = connect_to_db()
        cursor = db.cursor()

        create_and_populate_table(cursor)
        db.commit()

        moyenne_limite = float(input("Entrez la moyenne limite : "))

        etudiants = retrieve_students(cursor, moyenne_limite)
        if etudiants:
            print(f"Étudiants ayant une moyenne supérieure à {moyenne_limite}:")
            for etudiant in etudiants:
                print(f"ID: {etudiant[0]}, Nom: {etudiant[1]}, Âge: {etudiant[2]}, Moyenne: {etudiant[3]:.2f}")
        else:
            print("Aucun étudiant trouvé.")

    except mysql.connector.Error as err:
        print(f"Erreur : {err}")
    finally:
        cursor.close()
        db.close()

if __name__ == "__main__":
    main()
