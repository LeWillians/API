from flask import Flask

app = Flask(__name__)

@app.route("/pagar")
def exibir_mensagem():
    return "<h1>Pagar as pessoas, faz bem as pessoas!!!</h1>"

@app.route("/femandaopix")
def manda_o_pix():
    return "<h2>Se a tela apagou, tá devendo</h2>"

@app.route("/comida")
def comida():
    return "<h2>Tomato à milanesa</h2>"

@app.route("/livro")
def livros():
    return "<h2>Doe um livro!</h2>"

# Se o arquivo app.py for o arquivo principal da nossa aplicação, rode a api no modo de depuração
if __name__ == "__main__":
    app.run(debug=True)