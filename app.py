# pip install flask
from flask import Flask, jsonify, request
# Importazione delle componenti principali di Flask:
# - Flask: per creare l'applicazione web
# - jsonify: per restituire risposte JSON
# - request: per accedere ai dati delle richieste HTTP

app = Flask(__name__)

# Database simulato
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]
# Simulazione di un database in memoria con due utenti predefiniti.

# Endpoint per ottenere tutti gli utenti
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)
# Risponde a una richiesta GET sull'endpoint /users restituendo la lista completa degli utenti.

# Endpoint per ottenere un utente specifico
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("Utente non trovato", 404)
# Restituisce i dati dell'utente corrispondente all'ID specificato, oppure un errore 404 se non trovato.

# Endpoint per aggiungere un nuovo utente
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.json
    users.append(new_user)
    return jsonify(new_user), 201
# Riceve i dati di un nuovo utente in formato JSON e li aggiunge alla lista. Restituisce lo stesso utente con codice 201 (Created).

# Endpoint per aggiornare un utente
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        user.update(request.json)
        return jsonify(user)
    return ("Utente non trovato", 404)
# Modifica i dati di un utente esistente. Se l'utente è presente, aggiorna i suoi dati. Altrimenti restituisce errore 404.

# Endpoint per eliminare un utente
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return ("Utente eliminato", 200)
# Rimuove un utente dalla lista basandosi sull'ID. Restituisce messaggio di conferma con codice 200.

if __name__ == '__main__':
    app.run(debug=True)
# Avvia il server Flask in modalità debug (utile per sviluppo e testing).
