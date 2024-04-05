from flask import Flask, render_template, request, jsonify
from datetime import datetime
# Cria a instância do Flask no App
app = Flask(__name__)

# Banco em memória
banco = []

@app.route('/info')
def home():
    return render_template('index.html')

# Rota de teste
@app.route('/ping')
def ping_pong():
    banco.append({
        "dados" : "pong",
        "metodo": request.method,
        "hora":datetime.now()
    })
    return "<div id='pong'>{'resposta': 'pong'}</div>"


@app.route('/echo', methods=['POST'])
def echo():
    data = request.form
    texto = data.get('texto')
    banco.append({
        "dados": texto,
        "metodo": request.method,
        "hora":datetime.now()
    })
    return render_template('index.html')


@app.route('/dash')
def retorna_dash():
    return render_template('log.html', itens=banco)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)