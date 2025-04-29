from flask import Flask, jsonify
import json

app = Flask(__name__)


# products.json içinden verileri döndürüyoruz.
def load_products():
    try:
        with open('/app/data/products.json', 'r', encoding='utf-8') as f:
            products = json.load(f)
            return products
    except FileNotFoundError:
        return []


# load_products() fonksiyonundan gelen verileri json formatında endpoint ile yolluyoruz.
@app.route('/api/products', methods=['GET'])
def get_products():
    products = load_products()
    return jsonify({
        'count': len(products),
        'products': products
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
