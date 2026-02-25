from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Configuration des logs très verbeux (DEBUG) comme demandé 
logging.basicConfig(level=logging.DEBUG)

@app.route('/api/data')
def get_data():
    app.logger.debug("Requête reçue sur /api/data")
    # On simule l'utilisation d'une variable d'env pour la DB 
    db_host = os.getenv('DB_HOST', 'localhost')
    return jsonify({"status": "success", "message": f"Infos de la DB à {db_host}", "data": [1, 2, 3]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
