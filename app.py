import os
from flask import Flask, render_template, json, request, jsonify

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/jogador', methods=['POST'])
def jogador():

    json = request.get_json()
    nome = json['nome']
    time = json['time']
    combo = json['combo']
    return jsonify(nome=nome,time=time, combo=combo)



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)