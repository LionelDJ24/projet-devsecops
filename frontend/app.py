from flask import Flask
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    # URL du backend via le service Kubernetes
    backend_url = os.getenv('BACKEND_URL', 'http://localhost:5000/api/data')
    try:
        response = requests.get(backend_url)
        return f"<h1>Frontend</h1><p>Réponse du Backend : {response.text}</p>"
    except Exception as e:
        return f"Erreur de connexion au backend : {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
