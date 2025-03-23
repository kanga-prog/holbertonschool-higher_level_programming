from flask import Flask, render_template, request
import json
import csv

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

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    # Lire les données en fonction de la source demandée
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    else:
        return render_template('product_display.html', error="Wrong source")

    # Si un id est spécifié, filtrer les produits
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
