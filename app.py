from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "LH Shop - Camisas de Times. Segue no Instagram @lh._shop"

if __name__ == '__main__':
    app.run()
