from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Fonction pour lire les données JSON
def read_json_data():
    with open('products.json', 'r') as file:
        return json.load(file)

# Fonction pour lire les données CSV
def read_csv_data():
    products = []
    with open('products.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Convertir les types appropriés
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Fonction pour lire les données depuis la base de données SQLite
def read_sql_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()

    # Conversion des lignes récupérées en format de liste de dictionnaires
    products = []
    for row in rows:
        products.append({
            'id': row[0],
            'name': row[1],
            'category': row[2],
            'price': row[3]
        })
    return products

@app.route('/products')
def products():
    source = request.args.get('source')  # Récupère le paramètre source
    product_id = request.args.get('id', type=int)  # Récupère l'id si spécifié

    # Récupérer les données selon la source
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    elif source == 'sql':
        products = read_sql_data()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtrer les produits si un id est spécifié
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
