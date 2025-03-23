import sqlite3

def create_database():
    # Connexion à la base de données SQLite (elle sera créée si elle n'existe pas)
    conn = sqlite3.connect('products.db')  # Le fichier 'products.db' sera créé dans le même dossier
    cursor = conn.cursor()

    # Créer une table Products si elle n'existe pas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')

    # Insérer des données exemple dans la table Products
    cursor.execute('''
        INSERT INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    ''')

    # Sauvegarder les changements dans la base de données et fermer la connexion
    conn.commit()
    conn.close()

# Appeler la fonction pour créer la base de données et insérer des données
if __name__ == '__main__':
    create_database()
