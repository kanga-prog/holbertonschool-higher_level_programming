from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/items')
def items():
    # Lire les données depuis le fichier JSON
    with open('items.json', 'r') as file:
        data = json.load(file)
    
    # Passer les éléments à la template
    return render_template('items.html', items=data['items'])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
